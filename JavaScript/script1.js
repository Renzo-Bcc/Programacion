function generarNumeroAleatorio(min, max) {
    return Math.random() * (max - min) + min;
}
var numaleatorio = generarNumeroAleatorio(1, 60);
console.log(numaleatorio);