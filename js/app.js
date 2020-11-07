const express = require('express')

const PORT = 3000;
const TIMEOUT = 5000;
const ID = Math.floor(Math.random()*1000);
const app = express();
app.get('/',(req,res)=> {
    res.status(200).send('ping - '+ ID);
});

app.get('/timeout', (req,res) => {
    setTimeout(() => {
        res.status(200).send('timeout - ' + ID);
    },TIMEOUT);
});

app.listen(PORT, () => {
    console.log('Escuchando en el puerto', PORT)
});