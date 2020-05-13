#!/usr/bin/node
const request = require('request');
const url = process.argv.slice(2)[0];
request(url, function (error, response, body) {
  if (error) { console.log(error); } else {
    const data = JSON.parse(body);
    let result = {};
    for (const job of data) {
      if (result[job.userId] == null) {
        result[job.userId] = 0;
      }
      if (job.completed === true) {
        result[job.userId]++;
      }
    }
    let test = false;
    for (const el in result) { if (result[el] !== 0) { test = true; } }
    if (test === false) { result = {}; }
    console.log(result);
  }
});
