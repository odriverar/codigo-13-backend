const { application } = require('express');
const express = require('express');
const {config} = require('./config');
const cors = require('cors');

const alumnoApi = require('./routes/alumno.routes');
const cursoApi = require('./routes/curso.routes');

//! Middlewares
const {errorHandler, boomErrorHandler} = require('./middlewares/error.handler')

const app = express();
const port = config.port;

app.use(cors());
app.use(express.json());

app.get('/', (req, res) => {
      res.json({
            'status': true,
            'content': 'Servidor activo'
      })
})

alumnoApi(app);
cursoApi(app);

//! Manejo de errores
app.use(boomErrorHandler);
app.use(errorHandler);

app.listen(port, () => {
      console.log('Servidor en http://localhost:' + port);
})
