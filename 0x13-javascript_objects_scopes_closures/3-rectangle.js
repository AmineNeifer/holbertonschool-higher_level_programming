#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i;
    const x = 'X';
    for (i = 0; i < this.height; i++) {
      process.stdout.write(x.repeat(this.width) + '\n');
    }
  }
}
module.exports = Rectangle;
