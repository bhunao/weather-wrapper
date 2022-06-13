import { useEffect, useState } from 'react';
import axios from 'axios';

import './App.css';
import SearchIcon from './search.svg'


const api = axios.create({
  baseURL: "http://localhost:5000"
})

const App = () => {
  const [forecast, setForecast] = useState([])

  const getForecast = async (location) => {
    const URL = 'location/?loc=' + location;
    console.log(URL)

    api.get(URL).then(({data}) => {
      console.log(data);
      setForecast(data);
      console.log(forecast);
    })
  }

  useEffect(() => {
    getForecast('saopaulo');
  }, [])

  return (
    <>
      <div className='text'>
        <h1>{forecast.location}</h1>
        <h2>{forecast.date}</h2>
        <h2>{forecast.sky_text}</h2>
        <h2>{forecast.temperature}</h2>
      </div>
    </>
  );
}

export default App;
