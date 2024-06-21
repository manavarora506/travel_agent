from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain.chains import SimpleSequentialChain, LLMChain
from langchain.prompts import BasePromptTemplate, PromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain_core.tools import Tool
from langchain.agents import create_structured_chat_agent
from langchain.agents import AgentExecutor

app = Flask(__name__)
CORS(app, resources={r"/itinerary": {"origins": "http://localhost:3000"}})
load_dotenv()


# Configure OpenAI API key
openai_key = os.getenv('OPENAI_KEY')
GOOGLE_CSE_ID = os.getenv('GOOGLE_CSE_ID')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

llm=ChatOpenAI(api_key=openai_key, model="gpt-3.5-turbo")

search = GoogleSearchAPIWrapper(google_api_key=GOOGLE_API_KEY, google_cse_id=GOOGLE_CSE_ID)

google_tool = Tool(
    name="google_search",
    description="Search Google for recent results.",
    func=search.run,
)

system_template = """
       
        You are a travel agent who helps users make exciting travel plans.
        Prioritize including events that are happening right now.
        You have access to the following {tools} with the {tool_names} google_search.  You can process your thoughts using the {agent_scratchpad}.

        Convert the user's request into a detailed itinerary describing the places
        they should visit and the things they should do.
    
        **Remember to consider the user's specified destination ( {destination} ) 
        when creating the itinerary.**  Don't suggest locations that are too far away.

        **Return the itinerary as a bulleted list with clear start and end locations**

        If specific start and end locations are not given, choose ones that you think are suitable and give specific addresses.
        Your output must be the list and nothing else.

        Create my itenirary for {destination} from {start_date} to {end_date}

        `
        Use a json blob to specify a tool by providing an action key (tool name) and an action_input key (tool input).

        Valid "action" values: "Final Answer" or {tool_names}

        Provide only ONE action per $JSON_BLOB, as shown:

        ```
        {{
        "action": $TOOL_NAME,
        "action_input": $INPUT
        }}
        ```

        **Follow this format:**

        Question: input question to answer
        Thought: consider previous and subsequent steps
        Action:
        ```
        $JSON_BLOB # Use google_search to find specific details
        ```
        Observation: action result
        ... (repeat Thought/Action/Observation N times)
        Thought: I know what to respond
        Action:
        ```
        {{
        "action": "Final Answer",
        "action_input": "Final response to human"
        }}

        Begin! Reminder to ALWAYS respond with a valid json blob of a single action. Use tools if necessary. Respond directly if appropriate. Format is Action:```$JSON_BLOB```then Observation'''
        """

prompt_template = PromptTemplate(
    input_variables=["destination", "start_date", "end_date", "tools", "agent_scratchpad"],
    template=system_template
)
print(f"this is template {prompt_template}")

# Create the agent and executor outside the route function for reusability
agent = create_structured_chat_agent(llm=llm, tools=[google_tool], prompt=prompt_template)
agent_executor = AgentExecutor(agent=agent, tools=[google_tool], verbose=True, handle_parsing_errors=True, max_iterations=20)

@app.route('/itinerary', methods=['POST'])
def itinerary():
    data = request.json
    
    destination = data.get('destination')
    start_date = data.get('start_date')
    end_date = data.get('end_date')

    # Use the pre-created agent and executor
    itinerary = agent_executor.invoke({
        "destination": destination,
        "start_date": start_date,
        "end_date": end_date
    })
    itinerary_output = itinerary['output'] if 'output' in itinerary else "No itinerary generated."
    return jsonify({'itinerary': itinerary_output})

if __name__ == '__main__':
    app.run(debug=True)