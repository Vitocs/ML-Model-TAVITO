const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

const app = express();
const port = 3000;

app.use(bodyParser.json());

app.post('/predict', async (req, res) => {
    try {
        const userInput = req.body;
        const response = await axios.post('http://127.0.0.1:5000/predict', userInput);
        res.json(response.data);
    } catch (error) {
        res.status(500).send(error.message);
    }
});

app.listen(port, () => {
    console.log(`Node.js server is running on port ${port}`);
});
