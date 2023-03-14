#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && typeof (w) === 'number' && typeof (h) === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let j = 0; j < this.height; j++) {
      let ch = '';
      for (let i = 0; i < this.width; i++) {
        ch += 'X';
      }
      console.log(ch);
    }
  }

  rotate () {
    const w = this.width;
    this.width = this.height;
    this.height = w;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let ch = '';
      for (let j = 0; j < this.width; j++) {
        if (c === undefined || !c) {
          ch += 'X';
        } else {
          ch += c;
        }
      }
      console.log(ch);
    }
  }
}
module.exports = Square;
