#!/usr/bin/node
const request = require('request');
const url = process.argv.slice(2)[0];
request
  .get(url)
  .on('response', function (response) {
    console.log('code: ' + response.statusCode);
  });
