#!/usr/bin/node
//  script that reads and prints the content of a file.

const argv = process.argv[2];
const request = require('request');

request(argv, function (err, result, body) {
  if (err) {
    console.log('error: ', err);
  }
  const films = JSON.parse(body).results;
  let count = 0;
  for (let i = 0; i < films.length; i++) {
    const tempCount = films[i].characters.toString().match(/18/g);
    if (tempCount !== null) {
      count = count + tempCount.length;
    }
  }
  console.log(count);
});
