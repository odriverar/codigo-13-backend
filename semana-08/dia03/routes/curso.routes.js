const express = require('express');
const CursoService = require('../services/curso.service');

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
}

module.exports = cursoApi;