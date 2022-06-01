const express = require('express');

const app = express();

const port = 3000;

app.get('/', (req, res) => {
      res.send('<h1> BIENVENIDO A MI SITIO WEB CON EXPRESS </h1>');
});

app.get('/hola', (req, res) => {
      res.send('<h1> HOLA </h1>');
});

app.listen(port, function(){
      console.log('Servidor activo en http://localhost:' + port);
})