#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0 & h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;

    while (i < this.height) {
      console.log('X'.repeat(parseInt(this.width, 10)));
      i++;
    }
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }

  rotate () {
    const temp = this.height;

    this.height = this.width;
    this.width = temp;
  }
}
module.exports = Rectangle;
