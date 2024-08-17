var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let lin1 = lines.shift().split(' ');
let lin2 = lines.shift().split(' ');

let x1 = lin1.shift();
let y1 = lin1.shift();
let x2 = lin2.shift();
let y2 = lin2.shift();

let dist = Math.sqrt(Math.pow(x2-x1, 2) + Math.pow(y2-y1, 2));

console.log(dist.toFixed(4));