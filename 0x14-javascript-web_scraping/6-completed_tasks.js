#!/usr/bin/node

const argc = process.argv.slice(2);
const url = argc[0];
const request = require('request');
let i = 0;
let count = 0;

request(url, function (err, response, body) {
  if (err) {
    return console.error(err);
  }
  const res = JSON.parse(response.body);
  const obj = {};
  let act = 1;

  while (i < res.length) {
    if (res[i].completed) {
      if (act !== res[i].userId) {
        obj[act] = count;
        act = res[i].userId;
        count = 0;
      }
      count++;
    }
    i++;
  }
  obj[act] = count;
  console.log(obj);
});
