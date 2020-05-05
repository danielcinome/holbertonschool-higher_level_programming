#!/usr/bin/node

let i = 0;
const argv = process.argv.slice(2);

if (argv.length === 0) {
  console.log('Missing number of occurrences');
} else {
  while (i < argv[0]) {
    console.log('C is fun');
    i++;
  }
}
