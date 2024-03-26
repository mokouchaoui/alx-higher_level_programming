#!/usr/bin/node
/* script that prints all characters of a Star Wars movie */

const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/';

req(url, (err, response, body) => {
  if (err) console.log(err);
  else {
    const characters = JSON.parse(body).characters;
    for (let i = 0; i < characters.length; i++) {
      req(characters[i], (err, response, body) => {
        if (err) console.log(err);
        else console.log(JSON.parse(body).name);
      });
    }
  }
});
