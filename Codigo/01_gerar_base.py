#!/usr/bin/env python3
"""Gera uma população artificial para fins didáticos. Não usa cadastro da SIMPAR."""
from __future__ import annotations
import csv, random
from datetime import date, timedelta
from pathlib import Path

SEED = 241003357
N = 500_000
AS_OF = date(2025, 12, 31)
OUT = Path(__file__).resolve().parents[1] / "dados" / "base_imobilizado_sintetica.csv"
EXC_CSV = Path(__file__).resolve().parents[1] / "dados" / "registro_excecoes_inseridas.csv"
rng = random.Random(SEED)
classes = ["Veículos", "Máquinas e equipamentos", "Edificações", "Terrenos", "Equipamentos de TI", "Móveis e utensílios", "Imobilizado em andamento", "Direito de uso"]
locations = ["Sudeste", "Sul", "Centro-Oeste", "Nordeste", "Norte"]
centers = ["CC-LOG", "CC-FROTA", "CC-LOCACAO", "CC-INFRA", "CC-CORPORATIVO"]
entities = ["Entidade sintética A", "Entidade sintética B", "Entidade sintética C", "Entidade sintética D"]
exc = {
 101: "depreciacao_acumulada_maior_que_custo", 202: "depreciacao_acumulada_maior_que_custo", 303: "depreciacao_acumulada_maior_que_custo",
 404: "vida_util_zero", 505: "vida_util_zero", 606: "ativo_baixado_com_valor_liquido_positivo", 707: "ativo_baixado_com_valor_liquido_positivo",
 808: "data_disponivel_futura", 909: "localizacao_ausente", 1010: "depreciacao_negativa", 1111: "identificador_duplicado", 1212: "valor_residual_maior_que_custo"
}
headers = ["id_ativo_sintetico", "entidade_sintetica", "classe", "descricao_sintetica", "data_aquisicao", "data_disponivel_para_uso", "custo_bruto_R$", "vida_util_anos", "valor_residual_R$", "depreciacao_acumulada_R$", "valor_contabil_liquido_R$", "taxa_depreciacao_anual", "localizacao_sintetica", "situacao_sintetica", "data_baixa", "centro_custo_sintetico", "flag_anomalia_inserida", "tipo_anomalia_sintetica"]
OUT.parent.mkdir(parents=True, exist_ok=True)
with OUT.open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(headers)
    for i in range(1, N + 1):
        # Magnitudes geradas sem calibração ao saldo publicado. Todos os atributos são artificiais.
        gross = max(100, int(rng.lognormvariate(10.4, 0.9)))
        cls = rng.choice(classes)
        acq = date(2008, 1, 1) + timedelta(days=rng.randrange((AS_OF - date(2008,1,1)).days + 1))
        available = min(acq + timedelta(days=rng.randrange(0, 91)), AS_OF)
        life = rng.choice([3,4,5,8,10,12,15,20,25,30])
        residual = int(gross * rng.choice([0, .02, .05, .10])) if cls != "Terrenos" else int(gross * .95)
        elapsed = max(0, (AS_OF - available).days / 365.25)
        dep = min(max(0, int(max(0, gross-residual) * min(.95, elapsed/max(life,1)))), max(0,gross-residual))
        status = "Em operação"; disposal = ""; loc = rng.choice(locations)
        asset_id = f"SIM-{i:06d}"
        typ = exc.get(i, "")
        if typ == "depreciacao_acumulada_maior_que_custo": dep = gross + 1000
        elif typ == "vida_util_zero": life = 0
        elif typ == "ativo_baixado_com_valor_liquido_positivo": status, disposal = "Baixado - simulado", "2025-10-01"; dep = max(0, gross - int(gross*.2))
        elif typ == "data_disponivel_futura": available = date(2026, 2, 1)
        elif typ == "localizacao_ausente": loc = ""
        elif typ == "depreciacao_negativa": dep = -1000
        elif typ == "identificador_duplicado": asset_id = "SIM-000001"
        elif typ == "valor_residual_maior_que_custo": residual = gross + 500
        net = gross - dep
        w.writerow([asset_id, rng.choice(entities), cls, f"Ativo demonstrativo {i:06d}", acq.isoformat(), available.isoformat(), gross, life, residual, dep, net, (1/life if life else 0), loc, status, disposal, rng.choice(centers), "SIM" if typ else "NAO", typ])
# Registro das inserções deliberadas — não é evidência sobre a companhia.
with EXC_CSV.open("w", newline="", encoding="utf-8") as f:
    w=csv.writer(f); w.writerow(["linha_dados", "tipo_anomalia_sintetica", "nota"])
    for row,typ in exc.items(): w.writerow([row,typ,"Inserida deliberadamente pelo gerador; dados artificiais."])
print(f"Gerada {N:,} linhas sintéticas em {OUT}; seed={SEED}; anomalias inseridas={len(exc)}")
