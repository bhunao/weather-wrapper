import { useEffect, useState } from 'react';

import './App.css';
import SearchIcon from './search.svg'

const API_URL = 'http://localhost:5000/location/'

const App = () => {
  const [forecast, setForecast] = useState([])

  const getForecast = async (location) => {
    const URL = API_URL + location;
    console.log(URL)
    const response = await fetch(URL);
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
