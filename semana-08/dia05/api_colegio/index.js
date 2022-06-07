const express = require('express');
const {config} = require('./config');
const cors = require('cors');

//! Middlewares
const {errorHandler, boomErrorHandler} = require('./middlewares/error.handler')
const { verifyToken } = require('./middlewares/auth.handler');


//? Routes
const alumnoApi = require('./routes/alumno.routes');
const cursoApi = require('./routes/curso.routes');
const authApi = require('./routes/auth.routes');
const usuarioApi = require('./routes/usuario.routes');

const app = express();
const port = config.port;

app.use(cors());
app.use(express.json());

app.get('/', verifyToken, (req, res) => {
      res.json({
            'status': true,
            'content': 'Servidor activo'
      })
})

alumnoApi(app);
cursoApi(app);
authApi(app);
usuarioApi(app);

//! Manejo de errores
app.use(boomErrorHandler);
app.use(errorHandler);

app.listen(port, () => {
      console.log('Servidor en http://localhost:' + port);
})
