#!/usr/bin/node
const myArg = process.argv.slice(2)[0];
if (isNaN(myArg) || !myArg) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myArg);
}
