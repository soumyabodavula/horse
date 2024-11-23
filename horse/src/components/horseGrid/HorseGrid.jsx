import React, { useState } from 'react'
import breeds from '../../data/horse_breed_imgs.json';
import './horseGrid.css';

export default function HorseGrid() {

    const fallbackImage = require("../../data/horse_images/American_Paint_Horse.jpg")

    const [filter, setFilter] = useState('');
    const filteredBreeds = breeds.filter((breed) =>
      breed.Name.toLowerCase().startsWith(filter.toLowerCase())
    );

    const [copiedCard, setCopiedCard] = useState(null); 
    const handleCopy = (breedName) => {
      navigator.clipboard.writeText(breedName);
      setCopiedCard(breedName);

      setTimeout(() => {
        setCopiedCard(null);
      }, 200);
    };

    return (
      <div>
        <h1>Horse Breed Gallery</h1>
        <i class="fa-solid fa-horse"></i>
        <input
          type="text"
          placeholder="Search or filter by letter"
          value={filter}
          onChange={(e) => setFilter(e.target.value)}
          className="filter-input"
        />
        <div className="grid-container">
          {filteredBreeds.map((breed) => (
              <div key={breed.Name} className="grid-item">
                <img 
                src={breed.Image || fallbackImage}
                onError={(e) => {
                  e.target.onerror = null;
                  e.target.src = fallbackImage
                }}
                alt={breed.Name} 
                className="horse-image" 
                />
                <p className="horse-text">{breed.Name}
                  <i 
                    className= {`copyIcon fa-regular fa-copy ${copiedCard === breed.Name ? 'copied' : ''}`} 
                    onClick={() => handleCopy(breed.Name)}>
                  </i>
                </p>
              </div>
          ))}
        </div>
      </div>
    );
  }