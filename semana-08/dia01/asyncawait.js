// async function funcion_asincrona(){
//       return 100;
// }

// const valorSincrono = await funcion_asincrona();

// funcion_asincrona().then(value => {
//       console.log('El resultado es: ', value);
// })

async function hola(nombre){
      return new Promise(function(resolve, reject){
            setTimeout(function() {
                  console.log('Hola ' + nombre);
            }, 500);
            resolve(nombre);
            reject("Error")
      });
}

async function hablar(nombre) {
      return new Promise((res, rej) => {
            setTimeout(() => {
                  console.log('Como te va ' + nombre);
            }, 500);
            res(nombre);
            rej('no te entiendo')
      })
}

async function adios(nombre) {
      setTimeout(() => {
            console.log('Adios ', nombre);
      }, 1000);
}

async function main(){
      let nombre = await hola('David Rivera');
      await hablar(nombre);
      await adios(nombre);
}

main();