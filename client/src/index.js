import 'bootstrap/dist/css/bootstrap.min.css';
// import React, { useEffect, useState } from 'react'
import { createRoot } from 'react-dom/client'
import Navbar from './components/Navbar';
import './styles/main.css'
import {
    BrowserRouter as Router,
    Routes,
    Route
} from 'react-router-dom'
import Home from './components/Home';
import Login from './components/Login';
import SignUp from './components/SignUp';
import CreateRecipe from './components/CreateRecipe';


const App=()=>{

    
    return (
        <Router>
        <div className=''>
            <Navbar/>
            <Routes>
                <Route path='/create-recipe' element={<CreateRecipe/>}/>
                <Route path='/signup' element={<SignUp/>}/>
                <Route path='/login' element={<Login/>}/>
                <Route path='/' element={<Home/>}/>
            </Routes>
        </div>
        </Router>
    )
}

const root = createRoot(document.getElementById('root'));
root.render(<App/>)

// ReactDOM.render(<App/>, document.getElementById('root'));