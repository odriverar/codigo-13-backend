const express = require('express');
const { route } = require('express/lib/application');
const AlumnoService = require('../services/alumno.service');
const boom = require('@hapi/boom');

const validatorHandler = require('../middlewares/validator.handler');
const {createAlumnoSchema} = require('../schemas/alumno.schema');

function alumnoApi(app){
      const router = express.Router();
      app.use("/alumno", router);

      const objAlumnoService = new AlumnoService();

      router.get("/", async (req, res) => {
            try {
                  const alumnos = await objAlumnoService.getAll();
                  res.status(200).json({
                        status:true,
                        content:alumnos
                  })
            } catch (err) {
                  console.log(err);
            }
      })

      router.get("/:id", async (req, res) => {
            const {id} = req.params;
            try {
                  const alumno = await objAlumnoService.getById(id);
                  if(alumno.length > 0){
                        res.status(200).json({
                              status:true,
                              content:alumno
                        })
                  } else {
                        /*res.status(204).json({
                              status:false,
                              content:"No hay registros"
                        })*/
                        res.json(boom.notFound('No hay registros'))
                  }
            } catch (error) {
                  console.log(error);
            }
      })

      router.post("/", validatorHandler(createAlumnoSchema, 'body'), async (req, res) => {
            const {body: alumno} = req;
            console.log(alumno);
            try {
                  const crearAlumno = await objAlumnoService.create({alumno});
                  res.status(201).json({
                        status:true,
                        content:crearAlumno
                  })
            } catch (error) {
                  console.log(error);
            }
      })

      router.put("/:id", async (req, res) => {
            const {body: data} = req;
            const {id} = req.params;

            try {
                  const alumno = await objAlumnoService.update({data, id});

                  if(alumno.length > 0){
                        res.status(200).json({
                              status:true,
                              content:alumno
                        })
                  } else {
                        res.status(204).json({
                              status:false,
                              content:'No hay registros'
                        })
                  }
            } catch (error) {
                  console.log(error);
            }
      })

      router.delete("/:id", async (req, res) => {
            const {id} = req.params;
            try {
                  const deleteAlumno = await objAlumnoService.delete(id);

                  if(deleteAlumno){
                        res.status(201).json({
                              status:true,
                              content:'Alumno eliminado'
                        })
                  } else {
                        res.status(204).json({
                              status:false,
                              content: 'No hy registros'
                        })
                  }
            } catch (error) {
                  console.log(error);
            }
      })
}

module.exports = alumnoApi;