#!/usr/bin/node

exports.esrever = function (list) {
  let x;
  const array = [];
  for (x = list.length - 1; x >= 0; x--) {
    array.push(list[x]);
  }

  return (array);
};
