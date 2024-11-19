import React, { useEffect, useState } from 'react'
import horseData from '../../data/horse_breed_imgs.json';
import './horseGrid.css';

export default function HorseGrid() {
    const [breedsWithImages, setBreedsWithImages] = useState([]);

    useEffect(() => {
      const filteredBreeds = horseData.filter((breed) => breed.Image);
      setBreedsWithImages(filteredBreeds);
    }, []);

    const fallbackImage = require("../../data/horse_images/American_Paint_Horse.jpg")
    
  
    return (
      <div>
        <h1>Horse Breed Gallery</h1>
        <div className="grid-container">
          {breedsWithImages.map((breed) => (
            <div key={breed.Name} className="grid-item">
              <img 
              src={require(`../../data/${breed.Image}`)}
              onError={(e) => {
                e.target.onerror = null;
                e.target.src = fallbackImage
              }}
              alt={breed.Name} 
              className="horse-image" />
              <p>{breed.Name}</p>
            </div>
          ))}
        </div>
      </div>
    );
  }
