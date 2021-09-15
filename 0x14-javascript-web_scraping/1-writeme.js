#!/usr/bin/node
//  script that reads and prints the content of a file.

const argv = process.argv[2];
const fs = require('fs');
const argv1 = process.argv[3];

fs.appendFile(argv, argv1, function (error) {
  if (error) {
    console.log('error: ', error);
  }
});
