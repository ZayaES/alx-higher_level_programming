#!/usr/bin/node

const fs = require('fs');
const wData = process.argv[3];
const filePath = process.argv[2];

fs.writeFile(filePath, wData, 'utf-8', function (error) {
  if (error) {
    console.log(error);
  }
});
