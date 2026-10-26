#!/usr/bin/env python3
from pathlib import Path
import json,csv
import xlsxwriter
from parametros import ROOT,FINANCIALS
ROOT.joinpath('dados').mkdir(exist_ok=True)
out=ROOT/'dados'/'Dossie_SIMPAR_Analises.xlsx'
wb=xlsxwriter.Workbook(out)
navy='#18324B';teal='#147D78';light='#EAF1F5';gray='#687785';amber='#D89C46'
title=wb.add_format({'bold':True,'font_size':18,'font_color':'white','bg_color':navy,'valign':'vcenter'})
sub=wb.add_format({'bold':True,'font_color':'white','bg_color':teal,'text_wrap':True,'valign':'vcenter'})
num=wb.add_format({'num_format':'#,##0.0;[Red](#,##0.0);–'})
pct=wb.add_format({'num_format':'0.00%;[Red](0.00%);–'})
wrap=wb.add_format({'text_wrap':True,'valign':'top'})
warning=wb.add_format({'bold':True,'font_color':'#7A4A00','bg_color':'#FFF2CC','text_wrap':True,'valign':'top'})
# Sumário
s=wb.add_worksheet('Leia-me');s.set_column('A:A',27);s.set_column('B:B',100);s.merge_range('A1:B1','Dossiê Acadêmico de Auditoria — SIMPAR 2025',title);s.set_row(0,34)
readme=[('Período','Exercício findo em 31/12/2025; comparativo 2024.'),('Unidade pública','R$ mil, salvo indicação contrária.'),('Proveniência','Cifras conferidas em demonstrações publicadas 2025/2024; cópia recuperada por reprodução jornalística; protocolo e metadados da DFP da CVM conferidos.'),('Limitação','Não é auditoria, não emite opinião e não teve acesso a razão, cadastro de ativo ou papéis de auditores.'),('Base sintética','CSV 500.000 linhas; integralmente artificial; seed 241003357; 12 anomalias deliberadas; não corresponde a SIMPAR.'),('Materialidade','0,5% da receita consolidada; execução 75% e trivial 5%. Julgamento preliminar, não exigência normativa.'),('Guia','Use Comparativo, Materialidade, Riscos e Testes. Bases volumosas ficam nos CSV externos, não embutidas nesta pasta de trabalho.')]
for i,(a,b) in enumerate(readme,2):s.write(i,0,a,sub);s.write(i,1,b,warning if a in ['Limitação','Base sintética'] else wrap);s.set_row(i,38)
# Comparativo
ws=wb.add_worksheet('Comparativo');ws.freeze_panes(3,1);ws.set_column('A:A',56);ws.set_column('B:E',22);ws.merge_range('A1:E1','Demonstrações consolidadas e análise horizontal',title);ws.write_row('A3',['Indicador','2025 (R$ mil)','2024 (R$ mil)','Variação (R$ mil)','Variação %'],sub)
for r,(name,(v25,v24)) in enumerate(FINANCIALS.items(),3):
 ws.write(r,0,name,wrap);ws.write_number(r,1,v25,num);ws.write_number(r,2,v24,num);ws.write_formula(r,3,f'=B{r+1}-C{r+1}',num);ws.write_formula(r,4,f'=IF(C{r+1}>0,B{r+1}/C{r+1}-1,"")',pct)
ws.autofilter(2,0,2+len(FINANCIALS),4);ws.conditional_format(3,4,2+len(FINANCIALS),4,{'type':'3_color_scale'})
chart=wb.add_chart({'type':'bar'});chart.add_series({'name':'2025 (R$ mil)','categories':['Comparativo',3,0,8,0],'values':['Comparativo',3,1,8,1],'fill':{'color':teal}});chart.add_series({'name':'2024 (R$ mil)','categories':['Comparativo',3,0,8,0],'values':['Comparativo',3,2,8,2],'fill':{'color':'#8094AD'}});chart.set_title({'name':'Saldos/fluxos principais — R$ mil'});chart.set_x_axis({'name':'R$ mil'});chart.set_legend({'position':'bottom'});chart.set_size({'width':770,'height':420});ws.insert_chart('G3',chart)
# Materialidade
m=json.loads((ROOT/'dados'/'materialidade.json').read_text());w=wb.add_worksheet('Materialidade');w.set_column('A:A',50);w.set_column('B:B',25);w.set_column('C:C',80);w.merge_range('A1:C1','Materialidade preliminar — julgamento acadêmico',title);w.write_row('A3',['Parâmetro','R$ mil','Base/justificativa'],sub)
rows=[('Benchmark: receita líquida',FINANCIALS['Receita líquida'][0],'Consolidada 2025; unidade da DFP.'),('Percentual global',m['rate'],'Percentual escolhido para discussão, não prescrito pela norma.'),('Materialidade global',m['global_R$_mil'],'Receita × 0,5%.'),('Materialidade de execução',m['execution_R$_mil'],'75% da materialidade global.'),('Limite claramente trivial',m['clearly_trivial_R$_mil'],'5% da materialidade global.'),('Alternativa: 0,5% ativo total',m['alternative_benchmarks_R$_mil']['0.5% do ativo total'],'Sensibilidade ao benchmark.'),('Alternativa: 5% lucro antes de IR/CS',m['alternative_benchmarks_R$_mil']['5% do lucro antes de IR/CS'],'Mais volátil, sensibilidade.'),('Alternativa: 1% patrimônio líquido',m['alternative_benchmarks_R$_mil']['1% do patrimônio líquido'],'Sensibilidade.'),]
for i,row in enumerate(rows,3):w.write(i,0,row[0],wrap);w.write_number(i,1,row[1],num);w.write(i,2,row[2],wrap);w.set_row(i,34)
# Riscos
risk=wb.add_worksheet('Riscos');risk.set_column('A:A',25);risk.set_column('B:B',38);risk.set_column('C:C',27);risk.set_column('D:E',19);risk.set_column('F:G',70);risk.set_column('H:H',26);risk.set_column('I:I',16);risk.merge_range('A1:I1','Matriz preliminar de riscos e respostas propostas',title);risk.write_row('A3',['Ciclo','Risco','Afirmações','Probabilidade','Impacto','Resposta planejada','Evidência requerida','NBC TA','Status'],sub)
with (ROOT/'matrizes'/'matriz_riscos.csv').open(encoding='utf-8-sig') as f:
 for r,row in enumerate(csv.DictReader(f),3):
  for c,key in enumerate(['Ciclo','Risco','Afirmações','Probabilidade preliminar','Impacto preliminar','Resposta de auditoria proposta','Evidência necessária','Normas','Status']):risk.write(r,c,row[key],wrap)
  risk.set_row(r,55)
risk.freeze_panes(3,0);risk.autofilter(2,0,r,8)
# Testes
wt=wb.add_worksheet('Testes');wt.set_column('A:A',52);wt.set_column('B:C',17);wt.set_column('D:D',75);wt.merge_range('A1:D1','Validação da base sintética — não são achados da SIMPAR',title);wt.write_row('A3',['Regra','Inseridas','Detectadas','Interpretação'],sub)
inserted={}
with (ROOT/'dados'/'registro_excecoes_inseridas.csv').open(encoding='utf-8') as f:
 for row in csv.DictReader(f):inserted[row['tipo_anomalia_sintetica']]=inserted.get(row['tipo_anomalia_sintetica'],0)+1
report={}
for line in (ROOT/'dados'/'resultados_testes.txt').read_text().splitlines():
 if ': inserida=' in line:
  key=line.split(': inserida=')[0]; a=line.split('inserida=')[1].split(';')[0];b=line.split('detectada=')[1].split(';')[0];report[key]=(int(a),int(b))
for i,(k,(a,b)) in enumerate(report.items(),3):wt.write(i,0,k,wrap);wt.write_number(i,1,a,num);wt.write_number(i,2,b,num);wt.write(i,3,'Dados artificiais; regras deliberadamente inseridas para teste de código.',warning);wt.set_row(i,32)
# Fontes
src=wb.add_worksheet('Fontes');src.set_column('A:A',10);src.set_column('B:B',52);src.set_column('C:C',26);src.set_column('D:D',75);src.set_column('E:E',20);src.merge_range('A1:E1','Fontes e ressalvas',title);src.write_row('A3',['ID','Título','Instituição','URL','Status/limitação'],sub)
with (ROOT/'matrizes'/'registro_fontes.csv').open(encoding='utf-8-sig') as f:
 for r,row in enumerate(csv.DictReader(f),3):src.write(r,0,row['ID']);src.write(r,1,row['Título'],wrap);src.write(r,2,row['Instituição'],wrap);src.write_url(r,3,row['URL exata'],string=row['URL exata']);src.write(r,4,row['Status/limitação'],wrap);src.set_row(r,55)
norm=wb.add_worksheet('Cobertura NBC TA');norm.set_column('A:A',10);norm.set_column('B:B',35);norm.set_column('C:C',42);norm.set_column('D:E',75);norm.set_column('F:F',25);norm.set_column('G:G',70);norm.merge_range('A1:G1','Cobertura normativa — status e fontes oficiais',title);norm.write_row('A3',['Código','Norma/revisão','Versão aplicável','Requisitos/objetivo','Aplicação SIMPAR','Status','Fonte CFC'],sub)
with (ROOT/'matrizes'/'matriz_cobertura_normas.csv').open(encoding='utf-8-sig') as f:
 for r,row in enumerate(csv.DictReader(f),3):
  norm.write(r,0,row['Código']);norm.write(r,1,row['Norma/revisão'],wrap);norm.write(r,2,row['Versão aplicável ao período'],wrap);norm.write(r,3,row['Objetivo/requisitos relevantes'],wrap);norm.write(r,4,row['Aplicação SIMPAR 2025'],wrap);norm.write(r,5,row['Status da evidência'],wrap);norm.write_url(r,6,row['Fonte oficial'],string=row['Fonte oficial']);norm.set_row(r,75)
norm.freeze_panes(3,0);norm.autofilter(2,0,r,6)
for sheet in wb.worksheets():sheet.hide_gridlines(2);sheet.set_default_row(22)
wb.close();print(out)
