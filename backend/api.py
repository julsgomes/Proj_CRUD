from typing import Union
import consultas
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    teste = consultas.inserir_dados()
    return teste

