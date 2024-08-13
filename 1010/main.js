var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var calc1 = lines.shift().split(' ');
var calc2 = lines.shift().split(' ');

var peca_cod1 = calc1.shift();
var peca_num1 = calc1.shift();
var peca_valor1 = calc1.shift();
var peca_cod2 = calc2.shift();
var peca_num2 = calc2.shift();
var peca_valor2 = calc2.shift();

var valor_total = (parseInt(peca_num1) * parseFloat(peca_valor1)) + (parseInt(peca_num2) * parseFloat(peca_valor2))

console.log(`VALOR A PAGAR: R$ ${valor_total.toFixed(2)}`)
