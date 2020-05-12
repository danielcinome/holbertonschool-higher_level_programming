#!/usr/bin/node

const argc = process.argv.slice(2);
const file = argc[0];
const content = argc[1];
const fs = require('fs');

fs.writeFile(file, content, function (err) {
  if (err) {
    return console.error(err);
  }
});
