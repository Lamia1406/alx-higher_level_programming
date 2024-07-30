#!/usr/bin/node
const request = require('request');

if (process.argv.length > 1) {
  request(process.argv[2], (err, res, body) => {
    if (!err || res.statusCode === 200) {
      const films = JSON.parse(body).results;
      let wedgeAntillesCount = 0;
      for (const film of films) {
        if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
          wedgeAntillesCount++;
        }
      }
      console.log(wedgeAntillesCount);
    } else {
      console.error(err);
    }
  });
}
