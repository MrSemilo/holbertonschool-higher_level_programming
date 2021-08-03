#!/usr/bin/node
// Factorial
const myVar = parseInt(process.argv[2]);
if (isNaN(myVar)) {
  console.log(1);
} else {
  console.log(factorial(myVar));
}

function factorial (a) {
  if (a === 1) {
    return 1;
  } else {
    return (a * factorial(a - 1));
  }
}
