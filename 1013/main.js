var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var nums = lines.shift().split(' ');

var a = parseInt(nums.shift());
var b = parseInt(nums.shift());
var c = parseInt(nums.shift());

var maiorAB = (a + b + Math.abs(a - b)) / 2
var maior = (maiorAB + c + Math.abs(maiorAB - c)) / 2

console.log(`${maior} eh o maior`)