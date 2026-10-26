#!/usr/bin/env python3
from pathlib import Path
import pandas as pd, matplotlib.pyplot as plt
from parametros import ROOT, FINANCIALS
ROOT.joinpath('graficos').mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','axes.titleweight':'bold','figure.dpi':130})
# Comparativo das métricas financeiras selecionadas; R$ bilhões para legibilidade.
names=['Ativo total','Imobilizado líquido','Receita líquida','Lucro líquido do exercício','Caixa e equivalentes','Fluxo operacional líquido']
fig,ax=plt.subplots(figsize=(10,5.8)); ys=range(len(names))
for j,yr in enumerate([2024,2025]):
 vals=[FINANCIALS[n][1-j]/1_000_000 for n in names]
 ax.barh([i+(j-.5)*.34 for i in ys],vals,height=.32,label=str(yr),color=['#8094ad','#147d78'][j])
ax.set_yticks(list(ys),names);ax.set_xlabel('R$ bilhões');ax.set_title('SIMPAR consolidado — saldos e fluxos selecionados');ax.grid(axis='x',alpha=.2);ax.legend(title='Exercício');fig.text(.01,.01,'Fonte: demonstrações financeiras 2025/2024, R$ mil convertido para R$ bi. Valores reportados; fluxo operacional negativo.',fontsize=8);fig.tight_layout(rect=[0,.04,1,1]);fig.savefig(ROOT/'graficos'/'comparativo_2024_2025.png');plt.close(fig)
# Materialidade e saldos relevantes.
mat=FINANCIALS['Receita líquida'][0]*.005/1000
labels=['Materialidade\nglobal','Execução','Trivial','Imobilizado\nlíquido','Lucro líquido']
values=[mat,mat*.75,mat*.05,FINANCIALS['Imobilizado líquido'][0]/1000,FINANCIALS['Lucro líquido do exercício'][0]/1000]
fig,ax=plt.subplots(figsize=(9,5));bars=ax.bar(labels,values,color=['#147d78','#57a39c','#b7d9d5','#8094ad','#d89c46']);ax.set_ylabel('R$ milhões');ax.set_title('Materialidade preliminar versus saldos relevantes');ax.grid(axis='y',alpha=.2)
for b,v in zip(bars,values):ax.text(b.get_x()+b.get_width()/2,b.get_height(),f'{v:,.1f}',ha='center',va='bottom',fontsize=8)
fig.text(.01,.01,'Materialidade: 0,5% da receita líquida consolidada 2025; execução 75%; trivial 5%. Julgamentos didáticos, não regra normativa.',fontsize=8);fig.tight_layout(rect=[0,.05,1,1]);fig.savefig(ROOT/'graficos'/'materialidade.png');plt.close(fig)
# EDA sintética por classes + tipos de exceção; base inteira sintética.
df=pd.read_csv(ROOT/'dados'/'base_imobilizado_sintetica.csv',usecols=['classe','custo_bruto_R$','flag_anomalia_inserida','tipo_anomalia_sintetica'],low_memory=False)
agg=df.groupby('classe')['custo_bruto_R$'].sum().sort_values()/1e6
fig,ax=plt.subplots(figsize=(9,5));agg.sort_values().plot.barh(ax=ax,color='#147d78');ax.set_xlabel('Custo bruto sintético (R$ milhões)');ax.set_title('Distribuição do custo bruto — base inteiramente sintética');ax.grid(axis='x',alpha=.2);fig.text(.01,.01,'Dados artificiais, seed 241003357. Não representam cadastro patrimonial nem saldos reais da SIMPAR.',fontsize=8);fig.tight_layout(rect=[0,.04,1,1]);fig.savefig(ROOT/'graficos'/'distribuicao_sintetica.png');plt.close(fig)
counts=df[df.flag_anomalia_inserida.eq('SIM')].groupby('tipo_anomalia_sintetica').size().sort_values()
fig,ax=plt.subplots(figsize=(10,5));counts.plot.barh(ax=ax,color='#c45d4d');ax.set_xlabel('Registros artificiais marcados');ax.set_title('Anomalias deliberadamente inseridas na base sintética');ax.grid(axis='x',alpha=.2);fig.text(.01,.01,'Inserções didáticas detectadas pelo script; não são exceções observadas na SIMPAR.',fontsize=8);fig.tight_layout(rect=[0,.04,1,1]);fig.savefig(ROOT/'graficos'/'anomalias_sinteticas.png');plt.close(fig)
print('4 gráficos gerados em graficos/.')
