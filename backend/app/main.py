from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas.calculo import CalculoInput
from services.juros_service import calcular_juros_compostos

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/calcular")
def calcular(dados: CalculoInput):
    return calcular_juros_compostos(dados)