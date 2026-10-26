#!/usr/bin/env python3
"""Reconstrói todos os entregáveis do dossiê a partir dos códigos e fontes arquivadas."""
from pathlib import Path
import subprocess,sys
ROOT=Path(__file__).resolve().parents[1];CODE=ROOT/'codigo'
steps=['01_gerar_base.py','02_testes_base.py','03_analiticos.py','cobertura.py','04_graficos.py','05_planilhas.py','07_docs.py','06_dossie.py','08_validar.py']
for step in steps:
 print(f'\n===== {step} =====',flush=True)
 subprocess.run([sys.executable,str(CODE/step)],cwd=CODE,check=True)
print('\nReprodução concluída. Verifique README.md e matrizes/registro_limitacoes.csv.')
