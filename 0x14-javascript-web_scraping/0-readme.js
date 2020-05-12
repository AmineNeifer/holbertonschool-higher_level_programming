#!/usr/bin/node
const file = process.argv.slice(2)[0];
const fs = require('fs');
fs.readFile(file, 'utf8', function (err, data) {
  if (err) { console.log(err); } else { process.stdout.write(data); }
});
