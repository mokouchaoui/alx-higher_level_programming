#!/usr/bin/node
/* script that gets the contents of a webpage and stores it in a file. */

const req = require('request');
const fs = require('fs');
const url = process.argv[2];
const fn = process.argv[3];

req(url, (err, response, body) => {
  if (err) console.log(err);
  else {
    fs.writeFile(fn, body, 'utf8', (err) => {
      if (err) console.log(err);
    });
  }
});
