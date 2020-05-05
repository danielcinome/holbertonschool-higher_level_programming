#!/usr/bin/node

const argc = process.argv.slice(2).length;

if (argc === 0) {
  console.log('No argument');
} else if (argc === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
