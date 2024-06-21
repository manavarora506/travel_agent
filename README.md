# Travel Itinerary Generator

This project is a web application that generates travel itineraries based on user input. It leverages a Flask backend and a React frontend. The backend uses OpenAI's GPT-3.5 to generate itineraries and Google's Custom Search API to provide up-to-date information.

<div>
    <a href="https://www.loom.com/share/7b49e5072e414a97acf7f5092db95bb8">
      <p>Demo</p>
    </a>
    <a href="https://www.loom.com/share/7b49e5072e414a97acf7f5092db95bb8">
      <img style="max-width:300px;" src="https://cdn.loom.com/sessions/thumbnails/7b49e5072e414a97acf7f5092db95bb8-with-play.gif">
    </a>
  </div>


## Features

- User inputs their travel destination, start date, and end date.
- The application generates a detailed travel itinerary.
- Uses OpenAI's GPT-3.5-turbo for generating itineraries.
- Uses Google's Custom Search API to fetch recent events and places.

## Prerequisites

- Python 3.6+
- Node.js and npm

## Setup

### Backend (Flask)

1. Clone the repository:

    ```sh
    git clone https://github.com/your-username/travel-itinerary-generator.git
    cd travel-itinerary-generator
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Create a `.env` file in the root directory and add your API keys:

    ```env
    OPENAI_KEY=your_openai_api_key
    GOOGLE_CSE_ID=your_google_cse_id
    GOOGLE_API_KEY=your_google_api_key
    ```

4. Run the Flask server:

    ```sh
    python app.py
    ```

### Frontend (React)

1. Navigate to the `frontend` directory:

    ```sh
    cd frontend
    ```

2. Install the required npm packages:

    ```sh
    npm install
    ```

3. Create a `.env` file in the `frontend` directory and add the API URL:

    ```env
    REACT_APP_API_URL=http://127.0.0.1:5000
    ```

4. Start the React development server:

    ```sh
    npm start
    ```

## Usage

1. Open your web browser and go to `http://localhost:3000`.
2. Enter your travel destination, start date, and end date.
3. Click on "Generate Itinerary" to receive a detailed travel plan.

## Code Explanation

### Backend (Flask)

- `app.py`: The main Flask application file. It sets up the endpoints and integrates with OpenAI's API and Google's Custom Search API.
- The environment variables are loaded using `dotenv` to keep API keys secure.
- It defines a route `/itinerary` that accepts POST requests with destination, start date, and end date, and returns a generated itinerary.

### Frontend (React)

- `App.js`: The main React component. It contains the form for user input and displays the generated itinerary.
- Uses Material-UI for a clean and minimalistic UI.
- Fetches data from the Flask backend and displays it to the user.

## Dependencies

### Backend

- Flask
- Flask-CORS
- OpenAI
- LangChain
- python-dotenv

### Frontend

- React
- Material-UI

## Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.
