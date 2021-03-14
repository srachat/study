import aiofiles
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from ..worker.tasks import *
from ..worker.celery import app as celery_app, logger


app = FastAPI()

templates = Jinja2Templates(directory="src/app/templates")

TASKS = {
    name: {
        "name": name,
        "last_id": None
    } for name in TASKS
}


async def get_index_template(request: Request, **kwargs) -> templates.TemplateResponse:
    async with aiofiles.open("celery.log", "r") as celery_log:
        log = await celery_log.read()
    log = log.split("\n")
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "tasks": list(TASKS.values()), "log": log, **kwargs}
    )


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return await get_index_template(request)


@app.post("/process_task", response_class=HTMLResponse)
async def process_task(request: Request, task_name: str = Form(...), data: str = Form(...)):
    logger.info(f"Task {task_name} was called with arguments {data}")
    task_id = globals()[task_name].apply_async(args=[int(arg) for arg in data.split(" ")])
    TASKS[task_name]["last_id"] = task_id
    return await get_index_template(request)


@app.post("/check_state_by_id", response_class=HTMLResponse)
async def check_state_by_id(request: Request, task_id: str = Form(...)):
    state = celery_app.AsyncResult(task_id).state
    logger.info(f"Task with id {task_id} has a result {state}")
    return await get_index_template(request, task_state=state)


@app.post("/check_result_by_id", response_class=HTMLResponse)
async def check_state_by_id(request: Request, task_id: str = Form(...)):
    result = celery_app.AsyncResult(task_id).get()
    logger.info(f"Task with id {task_id} has a state {result}")
    return await get_index_template(request, task_result=result)

