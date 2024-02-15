#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

function starwarscharacters(movieId) {
    const url = `https://swapi.dev/api/films/${movieId}/`;
    request(url, (error, response, body) => {
        if (!error && response.statusCode == 200) {
            const film = JSON.parse(body);
            console.log(`Characters in ${film.title}:`);
            film.characters.forEach(characterUrl => {
                request(characterUrl, (charError, charResponse, charBody) => {
                    if (!charError && charResponse.statusCode == 200) {
                        const character = JSON.parse(charBody);
                        console.log(`- ${character.name}`);
                    } else {
                        console.log('Error fetching starwars character:', charError);
                    }
                });
            });
        } else {
            console.log('Error fetching film:', error)
        }
    });
}

if (!movieId) {
    console.log('Please enter a movie ID');
} else {
    starwarscharacters(movieId);
}
