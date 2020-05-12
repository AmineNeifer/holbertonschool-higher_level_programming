#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let i;
    if (c == null) {
      c = 'X';
    }
    for (i = 0; i < this.height; i++) {
      process.stdout.write(c.repeat(this.height) + '\n');
    }
  }
}
module.exports = Square;
