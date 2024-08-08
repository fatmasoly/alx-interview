#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, async (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode === 200) {
    const movies = JSON.parse(body);
    const characters = movies.characters;

    for (const character of characters) {
      const characterBody = await fetchCharacterName(character);

      console.log(JSON.parse(characterBody).name);
    }
  }
});

async function fetchCharacterName(characterEndpoint) {
  return new Promise((resolve, reject) => {
    request.get(characterEndpoint, (error, response, body) => {
      if (error) reject(error);

      if (response.statusCode === 200) {
        resolve(body);
      } else {
        reject(new Error(`Failed to fetch character: ${response.statusCode}`));
      }
    });
  });
}
