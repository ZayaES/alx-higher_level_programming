#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const cTasks = {};

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  }
  body = JSON.parse(body);

  for (const task of body) {
    if (task.completed === true) {
      if (cTasks[task.userId]) {
        cTasks[task.userId] += 1;
      } else {
        cTasks[task.userId] = 1;
      }
    }
  }
  console.log(cTasks);
});
