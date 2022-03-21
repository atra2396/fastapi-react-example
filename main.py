import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse

UI_BUILD = "ui/build/"
UI_STATIC = "ui/build/static"
UI_PUBLIC = "ui/public/"

app = FastAPI()
templates = Jinja2Templates(directory=UI_BUILD)

app.mount("/static", StaticFiles(directory=UI_STATIC), name="ui-build-assets")


@app.get("/")
async def get_site(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/{full_path:path}")
async def handle_spa_routing(request: Request, full_path: str):
    file_path = os.path.join(UI_PUBLIC, full_path)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return templates.TemplateResponse("index.html", {"request": request})
