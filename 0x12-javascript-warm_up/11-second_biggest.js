#!/usr/bin/node

const argv = process.argv.slice(2);
let x = 0;
let may = 0;
let ind = 0;

if (argv.length === 0 | argv.length === 1 & argv[0] === '1') {
  console.log(0);
} else {
  while (x < argv.length) {
    argv[x] = parseInt(argv[x]);
    if (may < argv[x]) {
      may = argv[x];
      ind = x;
    }
    x++;
  }
  argv.splice(ind, 1);
  console.log(Math.max(...argv));
}
