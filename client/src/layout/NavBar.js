import React from 'react'
import {Link} from 'react-router-dom'

export default function NavBar() {
  return (
    <div>
      <header>
        <div className="logo">
          {/*<img src={logo} alt="Pizza logo" />*/}
          <h1>Pizza Restaurants</h1>
       </div>
       <nav>
        <Link to="/">Home</Link>
        <Link to="/pizzas">Pizzas</Link>
       
       </nav>
      </header>

    </div>
  )
}
