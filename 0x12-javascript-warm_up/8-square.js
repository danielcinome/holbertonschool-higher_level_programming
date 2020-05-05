#!/usr/bin/node

let i = 0;
let value = 0;
const argv = process.argv.slice(2);

value = parseInt(argv[0], 10);
if (argv.length === 0 | !value) {
  console.log('Missing size');
} else {
  while (i < argv[0]) {
    console.log('X'.repeat(parseInt(argv[0], 10)));
    i++;
  }
}
