#!/usr/bin/node
const request = require('request');
request('https://swapi-api.alx-tools.com/api/films', function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const wedgeAntilles = JSON.parse(body).results.flatMap(result => result.characters).filter(character => character === 'https://swapi-api.alx-tools.com/api/people/18/');
    console.log(wedgeAntilles.length);
  }
});
