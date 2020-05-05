#!/usr/bin/node
const myArgs = process.argv.slice(2)[0];
function factorial(a) {
  if (a === 1 || a === 0) {
    return 1;
  }
  return a * factorial(a - 1);
}
if (isNaN(myArgs) || !myArgs) {
  console.log(1);
} else {
  console.log(factorial(Number(myArgs)));
}
