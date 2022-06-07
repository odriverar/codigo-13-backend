const express = require('express');
const CursoService = require('../services/curso.service');
const boom = require('@hapi/boom');

const validatorHandler = require('../middlewares/validator.handler');
const {createCursoSchema} = require('../schemas/curso.schema');

function cursoApi(app){
      const router = express.Router();
      app.use("/curso", router);

      const objCursoService = new CursoService();

      router.get("/", async (req, res) => {
            try {
                  const cursos = await objCursoService.getAll();
                  res.status(200).json({
                        status:true,
                        content:cursos
                  })
            } catch (error) {
                  console.log(error);
            }
      })

      router.post("/", validatorHandler(createCursoSchema, 'body'), async (req, res) => {
            const {body: curso} = req;
            try {
                  const crearCurso = await objCursoService.create({curso});
                  res.status(201).json({
                        status:true,
                        content:crearCurso
                  })
            } catch (error) {
                  console.log(error);
            }
      })
}

module.exports = cursoApi;