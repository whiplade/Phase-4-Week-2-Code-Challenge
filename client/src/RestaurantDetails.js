import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

function RestaurantDetails() {
  const { restaurantId } = useParams();
  const [restaurant, setRestaurant] = useState(null);

  useEffect(() => {
    fetch(`/restaurants/${restaurantId}`)
      .then((response) => {
        if (response.status === 404) {
          throw new Error('Restaurant not found');
        }
        return response.json();
      })
      .then((data) => setRestaurant(data))
      .catch((error) => console.error('Error fetching data:', error));
  }, [restaurantId]);

  if (!restaurant) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>Restaurant Details</h2>
      <p>Name: {restaurant.name}</p>
      <p>Address: {restaurant.address}</p>
      <h3>Pizzas:</h3>
      <ul>
        {restaurant.pizzas.map((pizza) => (
          <li key={pizza.id}>{pizza.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default RestaurantDetails;