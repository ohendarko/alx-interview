#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${args[0]}/`;

// If id is not provided in args
if (args.length === 0) {
  console.log('Usage: ./0x06-starwars_api [number]');
  process.exit(1);
}

// Function to fetch data from a URL and return a promise
function fetchData (url) {
  return new Promise((resolve, reject) => {
    request.get(url, (err, response, body) => {
      if (err) {
        return reject(err);
      }
      if (response.statusCode !== 200) {
        return reject(new Error(`Failed to fetch data. Status code: ${response.statusCode}`));
      }
      resolve(JSON.parse(body));
    });
  });
}

// Fetch film data
fetchData(apiUrl)
  .then(film => {
    const apiCharacters = film.characters;
    const characterPromises = apiCharacters.map(url => fetchData(url));

    return Promise.all(characterPromises);
  })
  .then(characters => {
    characters.forEach(character => {
      console.log(character.name);
    });
  })
  .catch(err => {
    console.error('Error:', err.message);
  });
