from schemas.calculo import CalculoInput
import json

def calcular_juros_compostos(dados: CalculoInput):
    total_periodo = dados.periodo

    # Ajuste das taxas baseado no tipo informado pelo usuário
    if dados.tipo_taxa == 'anual':
        taxa_ano = dados.taxa_juros / 100
        taxa_mensal = (1 + taxa_ano) ** (1 / 12) - 1
    else:
        taxa_mensal = dados.taxa_juros / 100
        taxa_ano = (1 + taxa_mensal) ** 12 - 1

    saldo = dados.capital_inicial
    total_investido = dados.capital_inicial
    historico = []

    # Corrigido para bater rigorosamente com o select do Angular
    if dados.tipo_periodo == 'ano' or dados.tipo_periodo == 'anos':
        for ano in range(1, total_periodo + 1):
            
            # --- AJUSTE EXCLUSIVO DE CÁLCULO ---
            # Simula exatamente os 12 meses daquele ano internamente para zerar a diferença
            for _ in range(12):
                juros_do_mes = saldo * taxa_mensal
                saldo += juros_do_mes + dados.aporte_mensal
                total_investido += dados.aporte_mensal
            # ------------------------------------

            historico.append({
                "ano": ano,
                "total": round(saldo, 2),
                "invested": round(total_investido, 2),
                "juros_acumulados": round(saldo - total_investido, 2)
            })
    else:
        for mes in range(1, total_periodo + 1):
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