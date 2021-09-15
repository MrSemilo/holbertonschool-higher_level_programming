#!/usr/bin/node
//  script that reads and prints the content of a file.

const argv = process.argv[2];
const request = require('request');

request(argv, function (err, result, body) {
  if (err) {
    console.log('error: ', err);
  } else {
    const fs = require('fs');
    const argv1 = process.argv[3];
    fs.writeFile(agrv1, body, function (err) {
      if (err) {
        console.log('error: ', err);
      }
    });
  }
});
