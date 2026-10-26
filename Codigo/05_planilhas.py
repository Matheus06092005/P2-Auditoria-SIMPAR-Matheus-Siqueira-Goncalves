#!/usr/bin/env python3
"""Nome alternativo previsto no roteiro; delega ao gerador de planilha 05_planilha.py."""
from pathlib import Path
p=Path(__file__).with_name('05_planilha.py')
exec(compile(p.read_text(encoding='utf-8'),str(p),'exec'))
