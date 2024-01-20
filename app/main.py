import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .router import posts

app = FastAPI()

app.mount("/static", StaticFiles(directory="/static"), name="static")
templating = Jinja2Templates(directory="template")


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_method=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)


@app.get("/")
def home(request: Request):
    context = {"request": request}
    return templating.TemplateResponse("index.html", context)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
