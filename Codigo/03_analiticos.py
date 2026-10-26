#!/usr/bin/env python3
from pathlib import Path
import json, pandas as pd
from parametros import ROOT, FINANCIALS, MATERIALITY_BENCHMARK, MATERIALITY_RATE, EXECUTION_RATE, TRIVIAL_RATE
out=ROOT/'dados';out.mkdir(exist_ok=True)
rows=[]
for name,(v25,v24) in FINANCIALS.items():
 # Percentual padrão apenas para comparativo positivo; fluxos/saldos negativos ficam nulos para evitar interpretação enganosa.
 pct=(v25/v24-1) if v24>0 else None
 rows.append({'Indicador':name,'2025_R$_mil':v25,'2024_R$_mil':v24,'Variação_absoluta_R$_mil':v25-v24,'Variação_percentual':pct})
compar=pd.DataFrame(rows);compar.to_csv(out/'comparativo_financeiro.csv',index=False,encoding='utf-8-sig')
revenue=FINANCIALS[MATERIALITY_BENCHMARK][0]
mat=revenue*MATERIALITY_RATE
materiality={'benchmark':MATERIALITY_BENCHMARK,'rate':MATERIALITY_RATE,'global_R$_mil':mat,'execution_rate':EXECUTION_RATE,'execution_R$_mil':mat*EXECUTION_RATE,'trivial_rate':TRIVIAL_RATE,'clearly_trivial_R$_mil':mat*TRIVIAL_RATE,'alternative_benchmarks_R$_mil':{'0.5% do ativo total':FINANCIALS['Ativo total'][0]*.005,'5% do lucro antes de IR/CS':FINANCIALS['Lucro antes de IR/CS'][0]*.05,'1% do patrimônio líquido':FINANCIALS['Patrimônio líquido consolidado'][0]*.01}}
(ROOT/'dados'/'materialidade.json').write_text(json.dumps(materiality,ensure_ascii=False,indent=2),encoding='utf-8')
metrics={
 'Receita/ativos 2025':FINANCIALS['Receita líquida'][0]/FINANCIALS['Ativo total'][0],
 'Imobilizado/ativos 2025':FINANCIALS['Imobilizado líquido'][0]/FINANCIALS['Ativo total'][0],
 'Liquidez corrente 2025':28_898_090/24_251_860,
 'Liquidez corrente 2024':27_220_964/21_080_863,
 'Dívida financeira bruta (empréstimos/debêntures) 2025 R$ mil':FINANCIALS['Empréstimos, financiamentos e debêntures — curto prazo'][0]+FINANCIALS['Empréstimos, financiamentos e debêntures — longo prazo'][0],
 'Dívida financeira bruta (empréstimos/debêntures) 2024 R$ mil':FINANCIALS['Empréstimos, financiamentos e debêntures — curto prazo'][1]+FINANCIALS['Empréstimos, financiamentos e debêntures — longo prazo'][1],
 'Passivos de arrendamento por direito de uso 2025 R$ mil':FINANCIALS['Arrendamentos por direito de uso — curto prazo'][0]+FINANCIALS['Arrendamentos por direito de uso — longo prazo'][0],
 'Passivos de arrendamento por direito de uso 2024 R$ mil':FINANCIALS['Arrendamentos por direito de uso — curto prazo'][1]+FINANCIALS['Arrendamentos por direito de uso — longo prazo'][1],
 'Imobilizado/Ativo total 2025':FINANCIALS['Imobilizado líquido'][0]/FINANCIALS['Ativo total'][0],
 'Imobilizado/Ativo total 2024':FINANCIALS['Imobilizado líquido'][1]/FINANCIALS['Ativo total'][1],
 'Caixa/Ativo total 2025':FINANCIALS['Caixa e equivalentes'][0]/FINANCIALS['Ativo total'][0],
 'Caixa/Ativo total 2024':FINANCIALS['Caixa e equivalentes'][1]/FINANCIALS['Ativo total'][1],
 'Margem bruta 2025':11_392_337/FINANCIALS['Receita líquida'][0],
 'Margem bruta 2024':10_427_445/FINANCIALS['Receita líquida'][1],
 'Margem lucro antes de IR/CS 2025':FINANCIALS['Lucro antes de IR/CS'][0]/FINANCIALS['Receita líquida'][0],
 'Margem lucro antes de IR/CS 2024':FINANCIALS['Lucro antes de IR/CS'][1]/FINANCIALS['Receita líquida'][1],
}
(ROOT/'dados'/'indicadores.json').write_text(json.dumps(metrics,ensure_ascii=False,indent=2),encoding='utf-8')
print('Análises financeiras e materialidade geradas. Unidade das fontes: R$ mil.')
print(compar.to_string(index=False))
print(json.dumps(materiality,ensure_ascii=False,indent=2))
