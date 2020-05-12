#!/usr/bin/node

const argc = process.argv.slice(2);
const url = argc[0];
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    return console.error(err);
  }
  console.log('code: ' + response.statusCode);
});
