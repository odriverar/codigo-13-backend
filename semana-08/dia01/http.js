const http = require('http');

http.createServer(function(req, res){
      console.log('servidor WEB iniciado');
      res.write('<h1> Bienvenido a mi sitio web con NodeJS </h1>');
}).listen(3000);