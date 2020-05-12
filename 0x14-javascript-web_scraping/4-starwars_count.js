#!/usr/bin/node
const request = require('request');
const url = process.argv.slice(2)[0];
request(url, function (error, response, body) {
  if (error) { console.log(error); } else {
    const listFilms = JSON.parse(body).results;
    let num = 0;
    for (const movie of listFilms) {
      if (movie.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        num++;
      }
    }
    console.log(num);
  }
});
