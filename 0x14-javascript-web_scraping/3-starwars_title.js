#!/usr/bin/node
const request = require('request');
const arg = process.argv.slice(2)[0];
const url = 'https://swapi-api.hbtn.io/api/films/' + arg;
request(url, function (error, response, body) {
  if (error) { throw (error); } else {
    process.stdout.write(JSON.parse(body).title);
  }
});
