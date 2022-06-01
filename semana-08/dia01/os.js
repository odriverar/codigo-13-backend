const os = require('os');

console.log('Arquitectura de procesador: ', os.arch());
console.log('Sistema Operativo ', os.platform());
console.log('CPU: ', os.cpus().length);
console.log('Memoria RAM: ', os.totalmem());