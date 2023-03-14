#!/usr/bin/node

exports.esrever = function (list) {
  const myArr = [];
  for (let i = list.length - 1; i >= 0; i--) {
    myArr.push(list[i]);
  }
  return myArr;
};
