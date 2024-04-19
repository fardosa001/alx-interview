#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

request(movieUrl, async function (error, response, body) {
  if (error) {
    return console.error(error);
  }

  const characterList = JSON.parse(body).characters;

  for (const character of characterList) {
    await new Promise(function (resolve, reject) {
      request(character, function (error, response, body) {
        if (error) {
          return console.error(error);
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
