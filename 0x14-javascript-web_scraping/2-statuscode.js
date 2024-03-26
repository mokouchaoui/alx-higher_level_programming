#!/usr/bin/node
/* script that display the status code of a GET request. */

const req = require('request');
const url = process.argv[2];
req(url, (err, res) => {
  if (err) {
    console.log(err);
  } else {
    console.log('code:', res.statusCode);
  }
});
