#!/usr/bin/node

const argv = process.argv.slice(2);

add(argv[0], argv[1]);
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
