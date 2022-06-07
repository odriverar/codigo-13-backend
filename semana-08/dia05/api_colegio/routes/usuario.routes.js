const express = require('express');
const UsuarioService = require('../services/usuario.service');
const boom = require('@hapi/boom');

function usuarioApi(app){
      const router = express.Router();
      app.use("/usuario", router);

      const objUsuarioService = new UsuarioService();

      router.get("/", async (req, res) => {
            try {
                  const usuarios = await objUsuarioService.getAll();
                  res.status(200).json({
                        status:true,
                        content:usuarios
                  })
            } catch (error) {
                  console.log(error);
            }
      })

      router.post("/", async (req, res) => {
            const {body: usuario} = req;
            try {
                  const crearUsuario = await objUsuarioService.create({usuario});
                  res.status(201).json({
                        status:true,
                        content:crearUsuario
                  })
            } catch (error) {
                  console.log(error);
            }
      })
}

module.exports = usuarioApi;