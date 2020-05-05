#!/usr/bin/node

const argc = process.argv.slice(2);
let value = 0;

if (argc.length === 0) {
  console.log('Not a number');
} else {
  value = parseInt(argc[0], 10);
  if (value) {
    console.log('My number: ' + value);
  } else {
    console.log('Not a number');
  }
}
