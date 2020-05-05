#!/usr/bin/node
const myArg = process.argv.slice(2)[0];
const letter = 'X';
let i;
if (isNaN(myArg) || !myArg) {
  console.log('Missing size');
} else {
  for (i = 0; i < Number(myArg); i++) {
    console.log(letter.repeat(Number(myArg)));
  }
}
