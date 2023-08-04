#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

function readWrite (url, filePath) {
  request(url).pipe(fs.createWriteStream(filePath));
}

readWrite(url, filePath);
