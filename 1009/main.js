var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let nome = lines.shift();
let salFixo = parseFloat(lines.shift());
let totalVendas = parseFloat(lines.shift());
let comissao = 0.15;
let salFinal = salFixo + totalVendas*comissao;

console.log(`TOTAL = R$ ${salFinal.toFixed(2)}`);
