var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let numFunc = parseInt(lines.shift());
let horas = parseInt(lines.shift());
let valHora = parseFloat(lines.shift());
let salary = valHora*horas;

console.log(`NUMBER = ${numFunc}`);
console.log(`SALARY = U$ ${salary.toFixed(2)}`);
