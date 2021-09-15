#!/usr/bin/node
//  script that reads and prints the content of a file.

const argv = process.argv[2];
const request = require('request');

request(argv, function (err, result, body) {
  console.log('code: ' + result.statusCode);
  if (err) {
    console.log('error: ', err);
  }
});
