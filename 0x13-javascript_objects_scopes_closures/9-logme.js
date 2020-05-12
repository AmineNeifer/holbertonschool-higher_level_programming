#!/usr/bin/node
exports.logMe = function (item) {
  if (global.num == null) {
    global.num = 0;
  } else {
    global.num++;
  }
  console.log(global.num + ': ' + item);
};
