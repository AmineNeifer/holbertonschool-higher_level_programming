#!/usr/bin/node
const file = process.argv.slice(2)[0];
const str = process.argv.slice(2)[1];
const fs = require('fs');
fs.writeFile(file, str, 'utf8', (err) => {
  if (err) { console.log(err); }
});
