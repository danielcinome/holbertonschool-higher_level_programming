#!/usr/bin/node

const argc = process.argv.slice(2);
const url = argc[0];
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    return console.error(err);
  }
  const res = JSON.parse(response.body);
  const obj = {};
  res.forEach(element => {
    if (element.completed) {
      if (!obj[element.userId]) {
        obj[element.userId] = 1;
      } else {
        obj[element.userId] += 1;
      }
    }
  });
  console.log(obj);
});
