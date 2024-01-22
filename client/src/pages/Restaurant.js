import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import RestaurantPizza from '../components/RestaurantPizza';

export default function Restaurant() {
  const { id } = useParams();
  const [restaurant, setRestaurant] = useState([]);

  useEffect(() => {
    fetch(`/restaurants/${id}`)
      .then((r) => r.json())
      .then((data) => {
        setRestaurant(data);
        //console.log('thrgbjjjnnk', data);
      });
  }, [id]);

  //console.log(restaurant);

  
  const pizzas = restaurant.pizzas;

  //console.log(pizzas);

  function handleAddPizza(newRestaurantPizza) {
    setRestaurant({
        ...restaurant,
        pizzas: [
          ...restaurant.pizzas,
          newRestaurantPizza,
        ],
    })}
  

  return (
    <div className="container">
      <div className="card">
        <h1 style={{color: "blue"}}>{restaurant.name}</h1>
        <p>{restaurant.address}</p>
      </div>

      <div className="card">
        <h2 style={{color: "blue"}}>Pizza Menu</h2>
        {pizzas && pizzas.length > 0 ? (
          pizzas.map((restaurant_pizza) => (
            <div key={restaurant_pizza.id}>
              <h3>{restaurant_pizza.name}</h3>
              <p>
                <em>Ingredients: {restaurant_pizza.ingredients}</em>
              </p>
            </div>
          ))
        ) : (
          <div className="alert alert-warning d-flex align-items-center" role="alert">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              fill="currentColor"
              className="bi bi-exclamation-triangle-fill flex-shrink-0 me-2"
              viewBox="0 0 16 16"
              role="img"
              aria-label="Warning:"
            >
              <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z" />
            </svg>
            <div>There are no pizzas for sale at the moment</div>
          </div>
        )}
        <h3 style={{color: "blue"}}>Add Piza</h3>
        <RestaurantPizza restaurantId={restaurant.id} onAddPizza={handleAddPizza}/>
      </div>
    </div>
  );
}
