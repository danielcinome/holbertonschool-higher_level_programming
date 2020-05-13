#!/usr/bin/node

const argc = process.argv.slice(2);
const url = argc[0];
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    return console.error(err);
  }
  const res = JSON.parse(body).results;
  let count = 0;

  res.forEach(element => {
    const val = element.characters;
    val.forEach(elem => {
      if (elem.includes('18')) {
        count++;
      }
    });
  });
  console.log(count);
});
