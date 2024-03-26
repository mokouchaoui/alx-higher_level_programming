#!/usr/bin/node
/* script that reads and prints the content of a file. */

const fs = require('fs');
const fn = process.argv[2];
fs.readFile(fn, 'utf8', (err, dt) => {
  if (err) {
    console.log(err);
  } else {
    console.log(dt.toString());
  }
});
