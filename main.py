from tempfile import template
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="ndb-ui/build/")

app.mount(
    "/static", StaticFiles(directory="ndb-ui/build/static"), name="ui-build-assets"
)


@app.get("/")
def get_site(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


app.mount("/", StaticFiles(directory="ndb-ui/public"), name="public-assets")
