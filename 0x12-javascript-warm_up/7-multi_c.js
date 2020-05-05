#!/usr/bin/node
const myArg = process.argv.slice(2)[0];
let i;
if (isNaN(myArg) || !myArg) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < Number(myArg) ; i++) {
      console.log('C is fun');
  }
}
