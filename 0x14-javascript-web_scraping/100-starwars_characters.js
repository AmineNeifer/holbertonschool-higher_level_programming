#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/';
request(url, function (error, response, body) {
  if (error) { console.log(error); } else {
    const listChar = JSON.parse(body).characters;
    for (const actor of listChar) {
      request(actor, function (error, response, body) {
        if (error) { console.log(error); } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
