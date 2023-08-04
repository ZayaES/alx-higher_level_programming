#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
var c_tasks = {};
var count = 0;

request(url, function (err, response, body) {
  if (err) {
  console.error(err)
  }
  body = JSON.parse(body);
  len = body.length;

  for (var task of body) {
    if (task.completed === true) {
      if (c_tasks[task.userId]) {
        c_tasks[task.userId] += 1;
      } else {
        c_tasks[task.userId] = 1;
      }
    }
  }
  console.log(c_tasks);
});
