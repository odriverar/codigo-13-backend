function hola(nombre){
      return new Promise(function(resolve, reject){
            setTimeout(function() {
                  console.log('Hola ' + nombre);
            }, 500);
            resolve(nombre);
            reject("Error")
      });
}

function hablar(nombre){
      return new Promise((res, rej) => {
            setTimeout(() => {
                  console.log('Como te va ' + nombre);
            }, 500);
            res(nombre);
            rej('no te entiendo')
      })
}

let nom = 'David Rivera'
hola(nom)
      .then(hablar)
      .then(() => {
            setTimeout(() => {
                  console.log('adios');
            }, 1000);
      })