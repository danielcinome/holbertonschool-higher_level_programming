#!/usr/bin/node

let val = process.argv.slice(2);
let res = 0;

if (!val[0]) {
  val = 1;
}
res = factorial(parseInt(val));
console.log(res);
function factorial (val) {
  if (val === 0) {
    return 1;
  }
  return val * factorial(val - 1);
}
