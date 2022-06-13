import uvicorn

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from weather.forecast import get_weather


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static")

@app.get("/", response_class=HTMLResponse)
async def weather(request: Request, loc: None | str="são paulo"):
    return templates.TemplateResponse(
        "index.html", {
            "request": request,
            "forecast": await get_weather(loc)
        }
    )

class Weather(BaseModel):
    location: str


@app.get("/location/")
async def location(loc: Weather):
    print(loc)
    result = await get_weather(loc.location)
    print(result)
    return result

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=5000,
        reload=True
    )
