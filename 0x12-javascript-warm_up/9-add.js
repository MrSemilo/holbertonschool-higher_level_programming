#!/usr/bin/node
// add
const myVar = parseInt(process.argv[2]);
const myNum = parseInt(process.argv[3]);
add(myVar, myNum);
function add (a, b) {
  console.log(a + b);
}
