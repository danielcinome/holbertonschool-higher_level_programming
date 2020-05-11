#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0 & h > 0)) {
      this.c = 'X';
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;

    while (i < this.height) {
      console.log(this.c.repeat(parseInt(this.width, 10)));
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

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
