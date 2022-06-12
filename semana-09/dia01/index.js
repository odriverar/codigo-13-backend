const express = require("express");
const app = express();

app.get("/", (req, res) => {
      res.json({
            content:"Servidor activo"
      })
})

const port = 4000;
app.listen(port, () => console.log('Servidor en http://localhost:'+port));

//? ************************ TRABJANDO CON SEQUELIZE ************************ */
const Sequelize = require("sequelize");

const sequelize = new Sequelize({
      dialect: 'sqlite',
      storage: './database.sqllite'
})

sequelize.authenticate()
.then(() => {
      console.log('Conexión establecida');
})
.catch(error => {
      console.log('Error: ', error);
})

//! Creamos modelos

const Alumnos = sequelize.define(
      'alumnos',
      {
            nombre: Sequelize.STRING,
            email: Sequelize.STRING
      }
)

//? MIGRACIONES
sequelize.sync({force:true})
.then(() => {
      console.log("Tablas migradas...");
      Alumnos.bulkCreate(
            [
                  {nombre: 'David Rivera Robles', email: 'odriverar@gmail.com'},
                  {nombre: 'Juan Perez Torres', email: 'eperez@gmail.com'}
            ]
      ).then(() => {
            return Alumnos.findAll();
      }).then((alumnos) => {
            console.log(alumnos);
      })
})

//? CREACION DE ENDPOITS
app.get("/alumno", (req, res) => {
      Alumnos.findAll()
      .then(
            alumnos => res.json(alumnos)
      )
})

app.use(express.json())

app.post("/alumno", (req, res) => {
      Alumnos.create(
            {
                  nombre: req.body.nombre,
                  email: req.body.email
            }
      ).then((alumnos) => {
            res.json(alumnos);
      })
})

app.put("/alumno/:id", (req, res) => {
      Alumnos.findByPk(req.params.id)
      .then((alumnos) => {
            alumnos.update({
                  nombre: req.body.nombre,
                  email: req.body.email
            }).then((alumnos) => {
                  res.json(alumnos)
            })
      })
})

app.delete("/alumno/:id", (req, res) => {
      Alumnos.findByPk(req.params.id)
      .then((alumnos) => {
            alumnos.destroy()
      }).then(() => {
            res.sendStatus(201)
      })
})