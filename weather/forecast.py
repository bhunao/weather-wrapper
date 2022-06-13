import python_weather

async def get_weather(location: str):
    client = python_weather.Client(format=python_weather.METRIC)
    weather = await client.find(location)

    forecast = weather.forecasts[1]

    await client.close()
    return {
        'location': str(location),
        'date': str(forecast.date),
        'sky_text': str(forecast.sky_text),
        'temperature': str(forecast.temperature)
    }
