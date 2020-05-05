#!/usr/bin/node
const myArgs = process.argv.slice(2);
function add (a, b) {
  return Number(a) + Number(b);
}
if (isNaN(myArgs[0]) || isNaN(myArgs[1]) || !myArgs[0]) {
  console.log('NaN');
} else {
  console.log(add(myArgs[0], myArgs[1]));
}
