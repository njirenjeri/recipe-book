import { useEffect, useState } from 'react'
// import React { useState, useEffect} from 'react'
import { Form, Button } from 'react-bootstrap'
import {Link} from 'react-router-dom'

const Login = () => {

  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  const handleSubmit = () =>{
    console.log("Form Submited")
    console.log(username)
    console.log(password)
   

    setUsername('')
    setPassword('')
 
  }

  return (
    <div className='container'>
          <div className='form'>
            <h1>Login</h1>
            <form>
              <Form.Group>
                <Form.Label>Username</Form.Label>
                  <Form.Control type='text' 
                    placeholder='enter your username'
                    value={username}
                    name='username'
                    onChange={(e) => {setUsername(e.target.value)}}
                  />
              </Form.Group>
              
              <br/>
              <Form.Group>
                <Form.Label>Password</Form.Label>
                  <Form.Control type='password' 
                    placeholder='enter your password'
                    value={password}  
                    name='password'
                    onChange={(e) => {setPassword(e.target.value)}}
                  />
              </Form.Group>
              
              <br/>
              <Form.Group>
                <Button as='sub' variant='primary' onClick={handleSubmit}>Login</Button>
              </Form.Group>

              <br/>
              <Form.Group>
                <small>Don't have an account? <Link to='/signup'>Create</Link></small>
              </Form.Group>
            </form>
          </div>
        </div>
  )
}

export default Login