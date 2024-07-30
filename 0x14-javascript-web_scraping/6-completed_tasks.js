#!/usr/bin/node
const request = require('request');

request(`${process.argv[2]}`, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const result = data.reduce((acc, currentValue) => {
      const key = currentValue.userId;
      if (currentValue.completed === true) {
        if (!acc[key]) {
          acc[key] = 1;
        } else {
          acc[key]++;
        }
      }
      return acc;
    }, {});
    console.log(result);
  }
});
