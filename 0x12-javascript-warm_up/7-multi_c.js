#!/usr/bin/node
const myVar = 'C is fun';
const myArg = parseInt(process.argv[2]);
if (isNaN(myArg)) {
  console.log('Missing number of occurrences');
}
else {
  for (let i = 0; i < myArg; i++) {
    console.log(myVar);
  }
}
