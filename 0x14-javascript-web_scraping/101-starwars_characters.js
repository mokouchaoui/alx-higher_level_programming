#!/usr/bin/node
/* script that prints all characters of a Star Wars movie */
const req = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`;

req(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const index = 0;
  const characters = JSON.parse(body).characters;
  printCharcter(characters, index);
});

const printCharcter = function (url, i) {
  req(url[i], (err, res, body) => {
    if (err) console.log(err);
    console.log(JSON.parse(body).name);
    if (++i < url.length) {
      printCharcter(url, i++);
    }
  });
};
