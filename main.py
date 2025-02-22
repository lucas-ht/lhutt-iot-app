import os

import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    app_name = "App 1"
    app_version = "1.0.0"

    pod_id = os.environ.get("POD_ID", "Not available")
    node_id = os.environ.get("NODE_ID", "Not available")

    return templates.TemplateResponse(
        request=request,
        name="index.html.j2",
        context={
            "app_name": app_name,
            "app_version": app_version,
            "pod_id": pod_id,
            "node_id": node_id,
        },
    )


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=3000,
    )
