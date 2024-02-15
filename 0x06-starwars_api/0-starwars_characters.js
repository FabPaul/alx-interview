#!/usr/bin/node

const request = require('request');

const fetchFilm = (filmId) => {
  return new Promise((resolve, reject) => {
    const url = `https://swapi.dev/api/films/${filmId}/`;
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const film = JSON.parse(body);
        resolve(film);
      }
    });
  });
};

const fetchCharacter = (characterUrl) => {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const character = JSON.parse(body);
        resolve(character);
      }
    });
  });
};

const filmID = process.argv[2];

if (!filmID) {
  console.log("Please provide a movie ID.");
} else {
  fetchFilm(filmID)
    .then((film) => {
      console.log(`Characters in ${film.title}:`);
      return Promise.all(film.characters.map(fetchCharacter));
    })
    .then((characters) => {
      characters.forEach((character) => {
        console.log(`- ${character.name}`);
      });
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
