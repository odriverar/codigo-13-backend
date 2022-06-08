const jwt = require('jsonwebtoken');

function verifyToken(req, res, next){
      const bearerToken = req.headers['authorization'];
      console.log('Bearer token = ', bearerToken);

      if (typeof bearerToken !== 'undefined'){
            //! obtenemos el token enviado
            const bearer = bearerToken.split(' ');
            const token = bearer[1];

            try {
                  const decoded = jwt.verify(token, 'codigo2022');
                  console.log(decoded);
            } catch (error) {
                  console.log(error);
                  return res.status(401).json({
                        status:false,
                        content:"Token invalido"
                  })
            }
            return next();
      } else {
            res.status(403).json({
                  status:false,
                  content:"No se encontro el token"
            })
      }
}

module.exports = { verifyToken }