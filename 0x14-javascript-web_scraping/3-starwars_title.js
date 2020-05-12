#!/usr/bin/node
const request = require('request');
const arg = process.argv.slice(2)[0];
const url = 'https://swapi-api.hbtn.io/api/films/' + arg;
request(url, function (error, response, body) {
  if (error) { console.log(error); } else {
    console.log(JSON.parse(body).title);
  }
});
