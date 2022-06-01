function hola(nombre, primercallback){
      setTimeout(function(){
            console.log('Hola ' + nombre);
      }, 1000);
      primercallback(nombre);
}

function hablar(nombre, segundocallback){
      setTimeout(function(){
            console.log('como te va ' + nombre);
      }, 500);
      segundocallback(nombre)
}

function adios(nombre){
      console.log('Adios ' +  nombre);
}

let nom = 'David Rivera Robles'
hola(nom, function(nombre){
      hablar(nombre, function(nombre){
            adios(nombre);
      })
});