import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import RestaurantList from './RestaurantList';
import RestaurantDetails from './RestaurantDetails';
import CreateRestaurantPizza from './CreateRestPizza';

function App() {
  return (
    <Router>
      <div>
        <h1>Welcome to the Pizza Restaurant App!</h1>

        <Routes>
          <Route path="/" element={<RestaurantList/>} />
          <Route path="/restaurants/:restaurantId" element={<RestaurantDetails/>} />
          <Route path="/create-restaurant-pizza" element={<CreateRestaurantPizza/>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;