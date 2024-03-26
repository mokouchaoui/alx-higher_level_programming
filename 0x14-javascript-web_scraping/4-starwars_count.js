#!/usr/bin/node
/* script that prints the number of movies where
 * the character “Wedge Antilles” is present. */

const req = require('request');
const api = process.argv[2];

req(api, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    const results = JSON.parse(body).results;
    for (let i = 0; i < results.length; i++) {
      const characters = results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].search('18') > 0) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
