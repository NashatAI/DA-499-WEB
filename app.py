from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "مرحبًا بك في FastAPI!"})

@app.post("/")
def handle_post(request: Request):
    return {"message": "تم استلام طلب POST!"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
