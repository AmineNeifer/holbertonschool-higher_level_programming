#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv.slice(2)[0];
const path = process.argv.slice(2)[1];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(path, body, 'utf8', (error) => {
      if (error) { console.log(error); }
    });
  }
});
