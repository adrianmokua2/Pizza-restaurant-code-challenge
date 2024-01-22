import React, {useEffect, useState}from 'react';
import {Link} from 'react-router-dom';
import Swal from 'sweetalert2';


export default function Restaurants() {

    const [restaurants, setRestaurants] = useState([]);

    useEffect(()=>{
        fetch("/restaurants")
        .then(res => res.json())
        .then(data => setRestaurants(data))

    }, [])

    function handleDelete(id){
        fetch(`/restaurants/${id}`, {method:'DELETE'})
        .then((r) => {
            if (r.ok) {
              setRestaurants((restaurants) =>
                restaurants.filter((restaurant) => restaurant.id !== id))
       
            Swal.fire({
                position: "center",
                icon: "success",
                title: "Restaurant deleted successfully!",
                showConfirmButton: false,
                timer: 1500
              });
        }
       })

    }


  return (
    <div className='container'>
        <h1>Here are the available restaurants...</h1>

        { restaurants.map(restaurant => 
            <div key={restaurant.id} className='card'>
                <h2>
                  <Link to={`/restaurants/${restaurant.id}`}>{restaurant.name}</Link>
                </h2>
                <p>Address: {restaurant.address}</p>
                <button onClick={()=>{handleDelete(restaurant.id)}}>Delete</button>

            </div>
        )}
    </div>
  )
}
