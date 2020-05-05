#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (!myArgs[0]) {
  console.log('No argument');
} else {
  myArgs.forEach(element => console.log(element));
}
