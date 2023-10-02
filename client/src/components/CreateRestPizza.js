import React, { useState } from 'react';

function CreateRestaurantPizza() {
  const [formData, setFormData] = useState({
    price: '',
    pizza_id: '',
    restaurant_id: '',
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    
    fetch('/restaurant_pizzas', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((data) => {
        
        console.log('Created relationship:', data);
      })
      .catch((error) => console.error('Error creating relationship:', error));
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  return (
    <div>
      <h2>Create Restaurant-Pizza Relationship</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Price:
          <input
            type="number"
            name="price"
            value={formData.price}
            onChange={handleChange}
          />
        </label>
        <label>
          Pizza ID:
          <input
            type="number"
            name="pizza_id"
            value={formData.pizza_id}
            onChange={handleChange}
          />
        </label>
        <label>
          Restaurant ID:
          <input
            type="number"
            name="restaurant_id"
            value={formData.restaurant_id}
            onChange={handleChange}
          />
        </label>
        <button type="submit">Create Relationship</button>
      </form>
    </div>
  );
}

export default CreateRestaurantPizza;