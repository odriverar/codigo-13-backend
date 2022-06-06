const { application } = require('express');
const express = require('express');
const {config} = require('./config');

const alumnoApi = require('./routes/alumno.routes');
const cursoApi = require('./routes/curso.routes');

const app = express();
const port = config.port;

app.use(express.json());

app.get('/', (req, res) => {
      res.json({
            'status': true,
            'content': 'Servidor activo'
      })
})

alumnoApi(app);
cursoApi(app);

app.listen(port, () => {
      console.log('Servidor en http://localhost:' + port);
})
