#!/usr/bin/node

const request = require('request');
const uri = process.argv[2];
let count = 0;

request(uri, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const films = JSON.parse(body).results;

  for (const film of films) {
    const len = film.characters.length;
    let x = 0;
    while (x < len) {
      if (film.characters[x] === 'https://swapi-api.alx-tools.com/api/people/18/') {
        count += 1;
      }
      x += 1;
    }
  }
  console.log(count);
});
