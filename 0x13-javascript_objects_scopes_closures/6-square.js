#!/usr/bin/node

const square = require('./5-square');
class Square extends square {
  charPrint (c) {
    if (!c) {
      this.c = 'X';
      super.print();
    } else {
      this.c = 'C';
      super.print();
    }
  }
}
module.exports = Square;
