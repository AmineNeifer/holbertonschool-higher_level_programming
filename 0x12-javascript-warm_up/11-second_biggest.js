#!/usr/bin/node
const myArgs = process.argv.slice(2);
function secondBiggest (array) {
  let max1 = array[0];
  let max2 = array[0];
  let i;
  for (i = 0; i < array.length; i++) {
    if (Number(array[i]) > max1) {
      max1 = Number(array[i]);
    }
  }
  for (i = 0; i < array.length; i++) {
    if (Number(array[i]) !== max1 && Number(array[i]) > max2) {
      max2 = Number(array[i]);
    }
  }
  return max2;
}
if (isNaN(myArgs[0]) || !myArgs[0] || myArgs.length === 1) {
  console.log(0);
} else {
  console.log(secondBiggest(myArgs));
}
