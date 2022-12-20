#!/usr/bin/node
// function that returns the reversed version of a list

exports.esrever = function (list) {
  const reversedList = [];
  for (let sanna = list.length - 1; sanna >= 0; sanna--) {
    reversedList.push(list[sanna]);
  }
  return reversedList;
};
