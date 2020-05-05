#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (myArgs === 0) {
  console.log('undefined  is  undefined');
} else if (myArgs === 1) {
  console.log(myArgs[0] + ' is undefined');
} else {
  console.log(myArgs[0] + ' is ' + myArgs[1]);
}
