#!/usr/bin/node
//script that reads and prints the content of a file.

const argv = process.argv[2];
const  fs = require('fs');

fs.readFile(argv, 'UTF-8', function (error, descri) {
  if (error) {
    console.log('error: ', error);
  } else {
    console.log(descri);
  }
});
