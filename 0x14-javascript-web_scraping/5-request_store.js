#!/usr/bin/node

const argc = process.argv.slice(2);
const url = argc[0];
const file = argc[1];
const fs = require('fs');
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    return console.error(err);
  }
  fs.writeFile(file, body, function (err) {
    if (err) {
      return console.error(err);
    }
  });
});
