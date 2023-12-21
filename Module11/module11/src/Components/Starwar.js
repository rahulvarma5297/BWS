import React from "react";
import { useState } from "react";

const Starwar = () => {
  const [starwar, setStarwar] = useState({
    loadedCharacter: false,
    name: null,
    height: null,
    homeworld: null,
    imageUrl: null,
    films: [],
  });

  const fetchData = () => {
    const randomNumber = Math.floor(Math.random() * 88);
    const url = `https://raw.githubusercontent.com/akabab/starwars-api/master/api/id/${randomNumber}.json`;
    fetch(url)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch.");
        }
        return response.json();
      })
      .then((charData) => {
        setStarwar({
          loadedCharacter: true,
          name: charData.name,
          height: charData.height,
          homeworld: charData.homeworld,
          imageUrl: charData.image,
          films: charData.films,
        });
      })
      .catch((err) => {
        console.log(err);
      });
  };

  return (
    <div className="container">
      {starwar.loadedCharacter && (
        <div>
          <h1>{starwar.name}</h1>
          <p>
            <img
              src={starwar.imageUrl}
              alt={starwar.name}
              className="picture"
            />
          </p>
          <p>
            Height: {starwar.height} <br />
            Homeworld: {starwar.homeworld}
          </p>
        </div>
      )}
      <button onClick={fetchData} className="button">
        Generate Character
      </button>
    </div>
  );
};

export default Starwar;
