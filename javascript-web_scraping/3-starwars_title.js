#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const id = process.argv[2];
const newString = url + id;

request.get(newString, (err, response, body) => {
  if (err) {
    console.log(err);
  }

  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  } else {
    console.error('Request failed with status:', response.statusCode);
  }
});