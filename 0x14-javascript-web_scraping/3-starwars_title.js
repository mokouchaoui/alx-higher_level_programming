#!/usr/bin/node
/* script that prints the title of a Star Wars movie
 * where the episode number matches a given integer. */
const req = require('request');
const id = process.argv[2];
const api = 'https://swapi-api.alx-tools.com/api/films/';
req(api + id + '/', (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
