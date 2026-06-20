from pydantic import BaseModel

class CalculoInput(BaseModel):
    capital_inicial: float
    aporte_mensal: float
    taxa_juros: float
    tipo_taxa: str # "mensal" ou "anual"
    periodo: int
    tipo_periodo: str # "meses" ou "anos"