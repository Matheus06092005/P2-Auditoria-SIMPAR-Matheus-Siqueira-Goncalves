#!/usr/bin/env python3
"""Extrai texto de PDFs que o usuário já baixou; NÃO baixa DFPs nem autentica na CVM.

Uso: python 00_extrair_dados_publicos.py caminho/para/arquivo.pdf [arquivo2.pdf ...]
Requer pdftotext (poppler-utils). Sem argumentos, mostra os PDFs arquivados em ../fontes.
"""
from pathlib import Path
import subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
if len(sys.argv)>1: files=[Path(x).expanduser().resolve() for x in sys.argv[1:]]
else: files=sorted((ROOT/'fontes').glob('*.pdf'))
if not files:
 print('Nenhum PDF encontrado. Baixe manualmente as fontes públicas e passe o caminho como argumento.');raise SystemExit(0)
for p in files:
 if not p.exists(): raise SystemExit(f'Arquivo não encontrado: {p}')
 out=ROOT/'fontes'/(p.stem+'_extraido.txt')
 result=subprocess.run(['pdftotext','-layout',str(p),str(out)],capture_output=True,text=True)
 if result.returncode: raise SystemExit(result.stderr)
 print(f'Texto extraído localmente: {out} ({out.stat().st_size:,} bytes).')
print('Acesso automatizado à interface CVM/dados abertos não é implementado; consultar URLs e limitações em ../fontes/EVIDENCIAS_EXTERNAS.md.')
