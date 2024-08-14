var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let raio = parseFloat(lines.shift());
let pi = 3.14159;
let volume = pi * (4/3.0) * Math.pow(raio,3);

console.log(`VOLUME = ${volume.toFixed(3)}`);