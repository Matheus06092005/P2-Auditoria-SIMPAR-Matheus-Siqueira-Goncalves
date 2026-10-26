#!/usr/bin/env python3
"""Testes de consistência sobre a base SINTÉTICA. Não testa dados reais da SIMPAR."""
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/'dados'/'base_imobilizado_sintetica.csv', keep_default_na=False)
cutoff='2025-12-31'
detected={
 'depreciacao_acumulada_maior_que_custo':int((df['depreciacao_acumulada_R$']>df['custo_bruto_R$']).sum()),
 'vida_util_zero':int((df['vida_util_anos']<=0).sum()),
 'ativo_baixado_com_valor_liquido_positivo':int(((df['situacao_sintetica'].str.contains('Baixado'))&(df['valor_contabil_liquido_R$']>0)).sum()),
 'data_disponivel_futura':int((pd.to_datetime(df['data_disponivel_para_uso'])>pd.Timestamp(cutoff)).sum()),
 'localizacao_ausente':int((df['localizacao_sintetica'].str.strip()=='').sum()),
 'depreciacao_negativa':int((df['depreciacao_acumulada_R$']<0).sum()),
 'identificador_duplicado':int(df['id_ativo_sintetico'].duplicated(keep='last').sum()),
 'valor_residual_maior_que_custo':int((df['valor_residual_R$']>df['custo_bruto_R$']).sum()),
}
inserted=df.loc[df.flag_anomalia_inserida.eq('SIM'),'tipo_anomalia_sintetica'].value_counts().to_dict()
expected={'depreciacao_acumulada_maior_que_custo':3,'vida_util_zero':2,'ativo_baixado_com_valor_liquido_positivo':2,'data_disponivel_futura':1,'localizacao_ausente':1,'depreciacao_negativa':1,'identificador_duplicado':1,'valor_residual_maior_que_custo':1}
checks={'linhas':(len(df),500_000),'linhas_marcadas':(int(df.flag_anomalia_inserida.eq('SIM').sum()),12),'ids_distintos':(int(df.id_ativo_sintetico.nunique()),499_999),'custo_bruto_positivo':(int((df['custo_bruto_R$']>0).sum()),500_000)}
lines=['RESULTADOS DOS TESTES — BASE SINTÉTICA','População artificial; nenhum registro real da SIMPAR.','Data de referência para teste de disponibilidade: 31/12/2025.','']
for k,(v,e) in checks.items(): lines.append(f'{k}: detectado={v}; esperado={e}; '+('OK' if v==e else 'FALHA'))
lines+=['','ANOMALIAS — contagem inserida versus detectada:']
for k,e in expected.items():
 ins=int(inserted.get(k,0)); det=int(detected[k]); lines.append(f'{k}: inserida={ins}; detectada={det}; '+('OK' if ins==e and det==e else 'FALHA'))
lines+=['','Interpretação: cada alerta corresponde a regra artificial deliberadamente inserida. Não é achado da SIMPAR, projeção de erro ou evidência de auditoria.']
(ROOT/'dados'/'resultados_testes.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')
df.sample(n=100,random_state=241003357).to_csv(ROOT/'dados'/'amostra_sintetica_100.csv',index=False)
df.nlargest(25,'custo_bruto_R$').to_csv(ROOT/'dados'/'top25_custo_bruto_sintetico.csv',index=False)
print('\n'.join(lines))
if any(v!=e for v,e in checks.values()) or any(inserted.get(k,0)!=e or detected[k]!=e for k,e in expected.items()): raise SystemExit('Falha na reconciliação dos testes sintéticos')
