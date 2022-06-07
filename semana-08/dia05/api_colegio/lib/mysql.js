const mysql = require('mysql2');
const {config} = require('../config');

class MysqlLib{
      constructor(){
            this.dbSettings = {
                  host : config.mysql_host,
                  user : config.mysql_user,
                  password : config.mysql_pwd,
                  database : config.mysql_db
            }
      }

      async getConnection(){
            try {
                  const pool = await mysql.createPool(this.dbSettings);
                  return pool;
            } catch (err) {
                  console.error(err);
            }
      }

      async querySql(sql){
            const pool = await this.getConnection();
            return new Promise((resolve, reject) => {
                  pool.query(sql, (err, result, fields) => {
                        if(!err) resolve(JSON.parse(JSON.stringify(result)));
                        else reject(err);
                  })
            })
      }
}

module.exports = MysqlLib;