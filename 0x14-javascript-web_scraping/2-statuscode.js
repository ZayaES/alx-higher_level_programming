#!/usr/bin/node

const request = require('request');
const uri = process.argv[2];

request(uri, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log('code:', response.statusCode);
});
