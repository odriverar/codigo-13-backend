const MysqlLib = require('../lib/mysql');

class CursoService{
      constructor(){
            this.sql = new MysqlLib();
      }

      async getAll(){
            const sqlAll = "select * from tbl_curso";
            const result = await this.sql.querySql(sqlAll);
            return result;
      }

      async create({curso}){
            const sqlCreate = `insert into tbl_curso(curso_nombre) values ('${curso.nombre}')`;

            await this.sql.querySql(sqlCreate);
            const sqlCursoCreado = "select * from tbl_curso order by curso_id desc limit 1";
            const result = await this.sql.querySql(sqlCursoCreado);

            return result;
      }
}

module.exports = CursoService;