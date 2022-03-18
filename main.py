from tempfile import template
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="ndb-ui/public")

app.mount("/static", StaticFiles(directory="ndb-ui/public/"), name="static")


@app.get("/")
def get_site(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
