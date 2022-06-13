import React, { useEffect, useState } from 'react';

import './App.css';
import SearchIcon from './search.svg'

const API_URL = 'https://localhost:5000/location/'

const App = () => {
  const [forecast, setForecast] = useState([])

  const getForecast = async (location) => {
    //const URL = API_URL + '?loc=saopaulo';
    const URL = '?loc=saopaulo';
    console.log(URL)
    const response = await fetch(URL, {
      method: 'GET',
      headers: {
        "Access-Control-Allow-Origin": "*",
        "Content-type": "application/json; charset=UTF-8"
      }
    }
      );
    const data = await response.json();

    console.log(data)
    setForecast(data)
  }

  useEffect(() => {
    getForecast('saopaulo')
  }, [])

  return (
    <>
      <div className='text'>
        <h1 >Vai bagui louco</h1>
      </div>
    </>
  );
}

export default App;
