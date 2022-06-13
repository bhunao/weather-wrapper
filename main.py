import uvicorn

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from weather.forecast import get_weather


app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.get("/location/")
async def location(loc: str):
    print(loc)
    result = await get_weather(loc)
    print(result)
    return result

@app.get("/test/")
async def test(tst: str):
    print(tst)
    return tst

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=5000,
        reload=True
    )
