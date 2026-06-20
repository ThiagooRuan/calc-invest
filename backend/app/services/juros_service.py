from schemas.calculo import CalculoInput
import json

def calcular_juros_compostos(dados: CalculoInput) -> json:
    total_meses = dados.periodo * 2 if dados.tipo_periodo == "anos" else dados.periodo

    if dados.tipo_taxa == "anual":
        taxa_mensal = (1 + dados.taxa_juros / 100) ** (1 / 12) - 1
    else:
        taxa_mensal = dados.taxa_juros / 100

    saldo = dados.capital_inicial
    total_investido = dados.capital_inicial
    historico = []

    for mes in range(1, total_meses + 1):
        juros_do_mes = saldo * taxa_mensal
        saldo += juros_do_mes + dados.aporte_mensal
        total_investido += dados.aporte_mensal

        historico.append({
            "mes": mes,
            "total": round(saldo, 2),
            "invested": round(total_investido, 2),
            "juros_acumulados": round(saldo - total_investido, 2)
        })

    return {
        "valor_final": round(saldo, 2),
        "total_invested": round(total_investido, 2),
        "total_juros": round(saldo - total_investido, 2),
        "timeline": historico
    }