#!/usr/bin/node
/* script that writes a string to a file. */

const fs = require('fs');
const fn = process.argv[2];
const txt = process.argv[3];
fs.writeFile(fn, txt, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
