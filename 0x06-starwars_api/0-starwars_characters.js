#!/usr/bin/node

const request = require('request');
const baseUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

function getCharacters (path) {
  return new Promise((resolve, reject) => {
    request(path, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
}

async function main () {
  const result = await getCharacters(baseUrl);
  const characters = JSON.parse(result).characters;
  let i = 0;
  const length = characters.length;
  while (i < length) {
    const person = await getCharacters(characters[i]);
    console.log(JSON.parse(person).name);
    i += 1;
  }
}
main();
