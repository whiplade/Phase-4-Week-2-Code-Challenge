import React, { useEffect, useState } from 'react';

function RestaurantList() {
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    
    fetch('/restaurants')
      .then((response) => response.json())
      .then((data) => setRestaurants(data))
      .catch((error) => console.error('Error fetching data:', error));
  }, []);

  return (
    <div>
      <h2>Restaurant List</h2>
      <ul>
        {restaurants.map((restaurant) => (
          <li key={restaurant.id}>
            <a href={`/restaurants/${restaurant.id}`}>{restaurant.name}</a>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default RestaurantList;