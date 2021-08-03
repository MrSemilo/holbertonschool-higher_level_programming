#!/usr/bin/node
// point 10
let index = 0;
exports.logMe = function (item) {
  console.log(`${index}: ${item}`);
  index = index + 1;
};
