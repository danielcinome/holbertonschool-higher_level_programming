#!/usr/bin/node

const square = require('./5-square');
class Square extends square {
  charPrint (c) {
    let i = 0;
    if (!c) {
      c = 'X';
    } else {
      c = 'C';
    }
    while (i < this.height) {
      console.log(c.repeat(parseInt(this.width, 10)));
      i++;
    }
  }
}
module.exports = Square;
