require('dotenv').config();

const config = {
      port: process.env.PORT || 3000,
      mysql_user : process.env.MYSQL_USER || 'root',
      mysql_pwd : process.env.MYSQL_PWD || '123456789',
      mysql_host : process.env.MYSQL_HOST || 'localhost',
      mysql_db : process.env.MYSQL_DB || 'db_colegio'
}

module.exports = {config};