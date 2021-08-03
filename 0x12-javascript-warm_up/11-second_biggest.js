#!/usr/bin/node
// second_biggest
const myVar = process.argv;
const array = [];
let count;
for (count = 2; count < myVar.length; count++) {
  array.push(parseInt(myVar[count]));
}
array.splice(array.indexOf(Math.max(...array)), 1);
if (array.length === 0) {
  console.log(0);
} else {
  console.log(Math.max(...array));
}
