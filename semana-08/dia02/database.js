const mysql = require('mysql2');

const mysqlConnection = mysql.createConnection({
      host: 'localhost',
      user: 'root',
      password: '123456789',
      database: 'db_colegio'
});

mysqlConnection.connect((err) => {
  if (err){
    console.error(err);
    return;
  }
  else{
    console.log('Conectado a la Base de Datos');
  }
});
 
module.exports = mysqlConnection;

// sqlConnection.query('SELECT * FROM TBL_ALUMNO', function (error, results, fields) {
//   if (error) throw error;
//   console.log(results);
// });
 
// sqlConnection.end();