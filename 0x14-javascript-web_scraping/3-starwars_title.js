#!/usr/bin/node
//  script that reads and prints the content of a file.

const argv = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + argv;

request(url, function (err, result, body) {
  console.log(JSON.parse(body).title);
  if (err) {
    console.log('error: ', err);
  }
});
