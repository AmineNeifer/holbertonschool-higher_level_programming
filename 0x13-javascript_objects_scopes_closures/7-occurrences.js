#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let num = 0;
  list.forEach(element => { if (searchElement === element) { num++; } });
  return num;
};
