import React, { useState } from 'react';
import { Container, TextField, Button, Typography, Paper, Box } from '@mui/material';
import './App.css';

function App() {
    const [destination, setDestination] = useState('');
    const [startDate, setStartDate] = useState('');
    const [endDate, setEndDate] = useState('');
    const [itinerary, setItinerary] = useState('');

    const handleGenerateItinerary = async () => {
        const response = await fetch('http://127.0.0.1:5000/itinerary', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ destination, start_date: startDate, end_date: endDate }),
        });
        const data = await response.json();
        console.log(data);
        setItinerary(data.itinerary);
    };

    return (
        <Container maxWidth="sm">
            <Paper elevation={3} style={{ padding: '2rem', marginTop: '2rem' }}>
                <Typography variant="h4" gutterBottom>
                    Travel Itinerary Generator
                </Typography>
                <TextField
                    label="Destination"
                    variant="outlined"
                    fullWidth
                    margin="normal"
                    value={destination}
                    onChange={(e) => setDestination(e.target.value)}
                />
                <TextField
                    label="Start Date"
                    type="date"
                    variant="outlined"
                    fullWidth
                    margin="normal"
                    InputLabelProps={{ shrink: true }}
                    value={startDate}
                    onChange={(e) => setStartDate(e.target.value)}
                />
                <TextField
                    label="End Date"
                    type="date"
                    variant="outlined"
                    fullWidth
                    margin="normal"
                    InputLabelProps={{ shrink: true }}
                    value={endDate}
                    onChange={(e) => setEndDate(e.target.value)}
                />
                <Button
                    variant="contained"
                    color="primary"
                    fullWidth
                    style={{ marginTop: '1rem' }}
                    onClick={handleGenerateItinerary}
                >
                    Generate Itinerary
                </Button>
                <Typography variant="h6" gutterBottom style={{ marginTop: '2rem' }}>
                    Itinerary:
                </Typography>
                <Paper variant="outlined" style={{ padding: '1rem', whiteSpace: 'pre-wrap' }}>
                    {itinerary}
                </Paper>
            </Paper>
        </Container>
    );
}

export default App;
