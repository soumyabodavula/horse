import React, { useState } from 'react'
import breeds from '../../data/horse_breed_imgs.json';
import './horseGrid.css';

export default function HorseGrid() {

    const fallbackImage = require("../../stick_horse_drawing.jpg")

    const [filter, setFilter] = useState('');
    const filteredBreeds = breeds.filter((breed) =>
      breed.Name.toLowerCase().normalize('NFD').replace(/\p{Diacritic}/gu, "").startsWith(filter.toLowerCase())
    );

    const [copiedCard, setCopiedCard] = useState(null); 
    const handleCopy = (breedName) => {
      navigator.clipboard.writeText(breedName);
      setCopiedCard(breedName);

      setTimeout(() => {
        setCopiedCard(null);
      }, 250);
    };

    const [selectedImage, setSelectedImage] = useState(null);
    const handleImageClick = (imageName) => {
      if (selectedImage === imageName) {
        setSelectedImage(null);
      } else {
        setSelectedImage(imageName);
      }
    };

    return (
      <div>
        <h1><i className="horseIcon fa-solid fa-horse"></i></h1>
        <input
          type="text"
          placeholder="Search or filter by letter"
          value={filter}
          onChange={(e) => setFilter(e.target.value)}
          className="filter-input"
        />
        <div className="grid-container">
          {filteredBreeds.map((breed) => (
              <div key={breed.Name} className={`grid-item ${selectedImage === breed.Name ? 'enlarged' : ''}`}>
                <img 
                src={breed.Image || fallbackImage}
                onError={(e) => {
                  e.target.onerror = null;
                  e.target.src = fallbackImage
                }}
                alt={breed.Name} 
                className={`horse-image ${selectedImage === breed.Name ? 'enlarged' : ''}`}
                onClick={() => handleImageClick(breed.Name)}
                />
                <p className="horse-text">{breed.Name}
                  <i 
                    className= {`copyIcon fa-regular fa-copy ${copiedCard === breed.Name ? 'copied' : ''}`} 
                    onClick={() => handleCopy(breed.Name)}>
                  </i>
                  <i className="linkIcon fa-solid fa-up-right-from-square"
                  onClick={() => window.open(breed.Link, '_blank')}>
                  </i>
                </p>
              </div>
          ))}
        </div>
      </div>
    );
  }