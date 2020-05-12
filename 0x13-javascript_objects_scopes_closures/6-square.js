#!/usr/bin/node
const S = require('./5-square');
class Square extends S {
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
