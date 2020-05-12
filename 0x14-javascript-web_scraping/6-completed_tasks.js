#!/usr/bin/node

const argc = process.argv.slice(2);
const url = argc[0];
const request = require('request');
let count = 0;

request(url, function (err, response, body) {
  if (err) {
    return console.error(err);
  }
  const res = JSON.parse(response.body);
  const obj = {};
  let act = 1;

  res.forEach(element => {
    if (element.completed) {
      if (act !== element.userId) {
        obj[act] = count;
        act = element.userId;
        count = 0;
      }
      count++;
    }
  });
  obj[act] = count;
  console.log(obj);
});
