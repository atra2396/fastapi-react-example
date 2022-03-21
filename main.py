import os
from tempfile import template
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse

app = FastAPI()
templates = Jinja2Templates(directory="ndb-ui/build/")

app.mount(
    "/static", StaticFiles(directory="ndb-ui/build/static"), name="ui-build-assets"
)


@app.get("/")
async def get_site(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/{full_path:path}")
async def handle_spa_routing(request: Request, full_path: str):
    if os.path.exists(os.path.join("ndb-ui/public", full_path)):
        return FileResponse(os.path.join("ndb-ui/public", full_path))
    return templates.TemplateResponse("index.html", {"request": request})
