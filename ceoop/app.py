from http import HTTPStatus

from fastapi import FastAPI

from ceoop.schemas import Message

app = FastAPI(title='API do CEOOP', version='1.0.0')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Bem vindo a API do CEOP!'}
