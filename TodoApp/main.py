from fastapi import FastAPI, Request, status
from . import models
from .database import engine
from .routers import auth, todos, admin, users
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="TodoApp/templates")

app.mount("/static", StaticFiles(directory="TodoApp/static"), name="static")

@app.get("/healthy")
def health_check():
    return {"status": "Healthy"}

@app.get("/")
def test(request: Request):
    return RedirectResponse(url="/todos/todo-page", status_code=status.HTTP_302_FOUND)


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)


