import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

function RestaurantList() {
    const [restaurants, setRestaurants] = useState([]);
    const navigate = useNavigate();
    const handleNavigate = (id) =>{
      navigate(`/restaurants/${id}`)}
      
    const handleFetch =() =>{
    fetch('/restaurants')
    .then((response) => response.json())
    .then((data) => setRestaurants(data))
    .catch((error) => console.error('Error fetching data:', error));
  }
    useEffect(() => {
    handleFetch()
    }, []);
    const handleDelete = (id) =>{
      
      fetch(`/restaurants/${id}`, {method:'DELETE'})
      .then((response) => {
        if (response.status === 404) {
          throw new Error('Restaurant not found');
        }
        
      })
      .then((data) =>{
        console.log(data)
        handleFetch()
      })
      .catch((error) => console.error('Error fetching data:', error));
    }
return (
    <div>
      <h2>Restaurant List</h2>
      <ul>
        {restaurants.map((restaurant) => (
          <li key={restaurant.id}>
            <p className='underline' onClick={() =>handleNavigate(restaurant.id)}>{restaurant.name}</p>
            <button onClick={() => handleDelete(restaurant.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default RestaurantList;