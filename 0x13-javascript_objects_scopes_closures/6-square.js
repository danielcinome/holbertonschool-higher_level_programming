#!/usr/bin/node

const square = require('./5-square');
class Square extends square {
  charPrint (c) {
    let i = 0;
    let letter;

    if (!c) {
      letter = 'X';
    } else {
      letter = c;
    }
    while (i < this.height) {
      console.log(letter.repeat(parseInt(this.width, 10)));
      i++;
    }
  }
}
module.exports = Square;
