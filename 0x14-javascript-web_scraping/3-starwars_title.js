#!/usr/bin/node

const argc = process.argv.slice(2);
const url = 'https://swapi-api.hbtn.io/api/films/' + argc[0];
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    return console.error(err);
  }
  const res = JSON.parse(response.body);
  console.log(res.title);
});
