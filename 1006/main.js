let input = require("fs").readFileSync("/dev/stdin", "utf8");
let lines = input.split("\n");

let a = parseFloat(lines.shift());
let b = parseFloat(lines.shift());
let c = parseFloat(lines.shift());

let media = (a*2+b*3+c*5) / 10;

console.log(`MEDIA = ${media.toFixed(1)}`);
