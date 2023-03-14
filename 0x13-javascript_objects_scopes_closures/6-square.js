#!/usr/bin/node

const PrevSquare = require('./5-square');

class Square extends PrevSquare {
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
