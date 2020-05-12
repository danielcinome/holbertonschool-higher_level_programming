#!/usr/bin/node

const argc = process.argv.slice(2);
const file = argc[0];
const fs = require('fs');

fs.readFile(file, 'utf-8', function (err, content) {
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(content);
  }
});
