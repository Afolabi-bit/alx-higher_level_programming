#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || !w || !h || h <= 0)
    {
      this.width = undefined;
      this.height = undefined;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
