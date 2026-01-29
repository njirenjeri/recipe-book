import React from 'react'
import {Link} from 'react-router-dom'

const Home = () => {
  return (
    <div className='home container'>
        <h1>Welcome to Recipe Book</h1>
        <h3>Your Everyday Kitchen Companion!</h3>
        <Link to='/signup' className='btn btn-primary btn-lg' >Get Started</Link>
    </div>
  )
}

export default Home