#!/usr/bin/node
const request = require('request');
const url = process.argv.slice(2)[0];
request(url, function (error, response, body) {
  if (error) { console.log(error); } 
  else 
  {
    data = JSON.parse(body);
    result = {}
    for (let job of data)
    {
      if (result[job.userId] == undefined)
      {
        result[job.userId] = 0;
      }
      if (job["completed"] === true)
      {
        result[job.userId]++;
      }
    }
    console.log(result);
  }
});
