#!/usr/bin/node
// Rotate and Double the width and height the Rectangle

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }

  print () {
    for (let sanna = 0; sanna < this.height; sanna++) console.log('X'.repeat(this.width));
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
};
