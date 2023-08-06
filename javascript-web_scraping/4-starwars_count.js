#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let counter = 0;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }

  if (response.statusCode === 200) {
    const data = JSON.parse(body).results;
    for (const film of data) {
      for (const character of film.characters) {
        if (character.includes('/18/')) {
          counter += 1;
        }
      }
    }
    console.log(counter);
  } else {
    console.error('Request failed with status:', response.statusCode);
  }
});