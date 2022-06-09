import python_weather

async def get_weather(location: str):
    client = python_weather.Client(format=python_weather.IMPERIAL)
    weather = await client.find(location)

    forecast = weather.forecasts[1]
    forecast.location = location

    await client.close()
    return forecast
