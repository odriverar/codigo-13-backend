const express = require('express');
const morgan = require('morgan');

const app = express();

app.use(morgan('combined'));

app.use((req, res, next) => {
      console.log('Time:', Date.now());
      next();
});

app.get("/", (req, res) => {
      res.json({
            content:"Ejemplo de middleware"
      })
})

//! Middleware para una ruta
app.use('/usuario', (req, res, next) => {
      console.log(a + 3);
      console.log('Tipo de request:', req.method);
      next();
})

//? Middleware de Errores
app.use("/usuario", (err, req, res, next) => {
      console.error(err.stack);
      res.status(500).json({
            status:false,
            content:"Error en el server",
            detail:err.stack
      })
})

app.get("/usuario", (req, res) => {
      res.json({
            nombre: "David Rivera"
      })
})


app.listen(3000, ()=>console.log("http://localhost:3000"));