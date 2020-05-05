#!/usr/bin/node
const myArg = process.argv.slice(2)[0];
let letter;
let i;
let j;
if (isNaN(myArg) || !myArg) {
  console.log('Missing size');
} else {
  for (i = 0; i < Number(myArg); i++) {
    letter = 'X';
    for (j = 1; j < Number(myArg); j++) {
      letter = letter + letter;
    }
    console.log(letter);
  }
}
