import React, {useState, useEffect} from 'react'

export default function Pizzas() {
    const [pizzas, setPizzas] = useState([])

    useEffect(()=>{
        fetch("/pizzas")
        .then(r => r.json())
        .then(data => {
            setPizzas(data)
        })
    }, [])

  return (
    <div className='container'>
        <h1>Check out this amazing pizzas and pick on your favorite restaurant on our home page to purchase...</h1>
        {pizzas.map((pizza)=>
        <div key={pizza.id} className='card'>
            <h3 style={{color: "blue"}}>Name: {pizza.name}</h3>
              <p>
                <em>Ingredients: {pizza.ingredients}</em>
              </p>

        </div>
        )}


    </div>
  )
}
