from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title='Minha API BALA wq')


@app.get('/', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def read_root():
    message = 'Hello World'
    return f"<h1>{message}</h1>"
