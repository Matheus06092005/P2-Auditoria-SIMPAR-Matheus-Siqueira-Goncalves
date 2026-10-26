#!/usr/bin/env python3
"""Gera um DOCX por norma. Procedimentos não executados são rotulados de forma explícita."""
from pathlib import Path
import csv
from docx import Document
from docx.shared import Inches,Pt,RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT,WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from dossie_pts_a import PROGRAMAS
from parametros import ROOT,ACCESS_DATE
OUT=ROOT/'workpapers';OUT.mkdir(exist_ok=True)

def shade(cell,color):
 tcPr=cell._tc.get_or_add_tcPr();shd=OxmlElement('w:shd');shd.set(qn('w:fill'),color);tcPr.append(shd)
def make_header(doc,code,title):
 sec=doc.sections[0];sec.top_margin=Inches(.65);sec.bottom_margin=Inches(.65);sec.left_margin=Inches(.75);sec.right_margin=Inches(.75)
 p=sec.header.paragraphs[0];p.text='SIMPAR S.A.  |  DOSSIÊ ACADÊMICO DE AUDITORIA 2025';p.style='Caption'
 p=sec.footer.paragraphs[0];p.alignment=WD_ALIGN_PARAGRAPH.CENTER;p.add_run('Matrícula 241003357 | Preparado em 25/10/2026 | Sem opinião de auditoria independente  •  ')
 fld=OxmlElement('w:fldSimple');fld.set(qn('w:instr'),'PAGE');p._p.append(fld)
 doc.styles['Normal'].font.name='Aptos';doc.styles['Normal'].font.size=Pt(9);doc.styles['Normal'].font.color.rgb=RGBColor(45,57,67)
 for sty,size,color in [('Title',24,'18324B'),('Heading 1',15,'18324B'),('Heading 2',11,'147D78')]:
  s=doc.styles[sty];s.font.name='Aptos Display';s.font.size=Pt(size);s.font.bold=True;s.font.color.rgb=RGBColor.from_string(color)
 doc.add_heading(f'PT-{code} — {title}',0)
 p=doc.add_paragraph('SIMPAR S.A. | demonstrações consolidadas encerradas em 31/12/2025 | comparativo 2024');p.style='Subtitle'

def add_section(doc,head,body):
 doc.add_heading(head,2);doc.add_paragraph(body)

def write_wp(row):
 code,title,version,req,application,status,url=row
 filename='PT-EC.docx' if code=='EC' else f'PT-{code}.docx'
 doc=Document();make_header(doc,code,title)
 t=doc.add_table(rows=4,cols=2);t.alignment=WD_TABLE_ALIGNMENT.CENTER;t.style='Table Grid'
 meta=[('Código/critério',f'{code} — {title}'),('Versão e fonte',f'{version}\nFonte oficial: {url}'),('Responsável e data','Matrícula 241003357 | 25/10/2026'),('Status geral',status)]
 for i,(a,b) in enumerate(meta):t.cell(i,0).text=a;t.cell(i,1).text=b;shade(t.cell(i,0),'EAF1F5');t.cell(i,0).vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER;t.cell(i,1).vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
 add_section(doc,'1. Objetivo e escopo',req+' Este papel aplica o critério ao planejamento acadêmico do exame das demonstrações consolidadas SIMPAR 2025; não representa compromisso de auditoria nem opinião.')
 add_section(doc,'2. Risco avaliado e afirmações',application+' Afirmações a considerar, conforme ciclo: existência/ocorrência; integridade; direitos e obrigações; avaliação/alocação; corte; classificação/apresentação e divulgação. A aplicabilidade específica depende da conta/transação e evidência ainda não obtida.')
 add_section(doc,'3. Critérios normativos relevantes',f'{title}. A descrição resumida acima é um mapa de aplicação, não citação literal. A redação, itens de aplicação e vigência devem ser conferidos no texto integral do CFC indicado. Para as normas revisadas depois do período, ver a identificação temporal abaixo e não retroagir requisito futuro.')
 add_section(doc,'4. População e amostra','População documental disponível: demonstrativos públicos 2025/2024 e informações públicas do relatório anual; não foram obtidos razão, cadastro, contrato, pacote de componente nem base de auditoria da Companhia. A seleção de amostra real é PENDENTE. A amostra artificial de 100 registros e a seleção top 25 só se aplicam à base SIMULADA (PT-02), não são amostra da população da SIMPAR.')
 # Program-specific procedures if available; otherwise norm-specific response.
 matched=None
 for key,items in PROGRAMAS.items():
  if any(k.lower() in application.lower() or k.lower() in title.lower() for k in [key]):matched=items;break
 if matched:
  for head,body in matched:add_section(doc,head,body)
 else:
  add_section(doc,'5. Procedimentos planejados',f'1) Identificar população, componente/ciclo e afirmação afetada. 2) Avaliar risco e desenhar resposta compatível com relevância e qualidade da evidência. 3) Obter evidência externa/interna pertinente, testar integridade e confiabilidade dos dados e documentar seleção, execução e desvios. 4) Avaliar distorções, comunicações, divulgações e impacto na conclusão. Aplicação SIMPAR: {application}')
 add_section(doc,'6. Evidências necessárias','Documento oficial original, razão e reconciliações, contratos e aprovações, cálculos e suportes do saldo, confirmações externas quando pertinentes, comunicações com governança/componente e registro contemporâneo do procedimento. As evidências internas e confirmações não foram obtidas neste estudo.')
 add_section(doc,'7. Procedimentos efetivamente executados','PÚBLICO VERIFICADO: consulta a metadados da DFP na CVM e leitura da cópia pública reproduzida das demonstrações financeiras 2025/2024; cálculos analíticos e registro de limitações. SIMULADO: somente testes identificados como tal na base artificial de 500.000 linhas. Não houve inspeção, circularização, teste de controle, recálculo com dados reais, comunicação com administração ou exame dos papéis do auditor.')
 add_section(doc,'8. Resultados e exceções','Resultado público: valores agregados utilizados no dossiê são rastreados à demonstração publicada, R$ mil, PDF reproduzido p. 2; políticas localizadas nas notas 2.12, 2.14 e 2.20 e eventos subsequentes na nota 6 quando aplicável. Exceções reais: nenhuma foi determinada, pois não foi obtida população/teste interno. Exceções sintéticas: doze inserções deliberadas em oito classes, testadas separadamente; não são achados da SIMPAR.')
 add_section(doc,'9. Avaliação e conclusão','O critério orienta o planejamento e a documentação dos procedimentos aplicáveis a SIMPAR. Com a evidência atual não se conclui sobre conformidade, distorção, controle ou suficiência dos saldos da Companhia; a execução é PLANEJADA/PENDENTE. Atualizar a conclusão somente após obter evidência apropriada e revisar os requisitos oficiais item a item.')
 add_section(doc,'10. Referências cruzadas','Dossiê principal; matrizes/matriz_cobertura_normas.csv; matrizes/matriz_riscos.csv; matrizes/registro_procedimentos.csv; matrizes/registro_fontes.csv; PT-01 planejamento; PT-02 base sintética; PT-03 resultados analíticos; PT-04 riscos/ciclos; PT-05 conclusão integrada; fontes/EVIDENCIAS_EXTERNAS.md. Localizador de demonstrações: F2, PDF reproduzido p. 2, R$ mil; página/nota de movimentação do imobilizado pendente de confirmar no PDF CVM integral.')
 add_section(doc,'11. Responsável, data e status','Preparador: matrícula 241003357. Data: 25/10/2026. Revisão por segundo profissional: não realizada. Classificações: Público verificado; Planejado; Simulado; Pendente, conforme indicado. Documento acadêmico, não arquivo de auditoria independente.')
 doc.save(OUT/filename)

with (ROOT/'matrizes'/'matriz_cobertura_normas.csv').open(encoding='utf-8-sig') as f: rows=list(csv.DictReader(f))
for row in rows:
 write_wp((row['Código'],row['Norma/revisão'],row['Versão aplicável ao período'],row['Objetivo/requisitos relevantes'],row['Aplicação SIMPAR 2025'],row['Status da evidência'],row['Fonte oficial']))
print(f'Gerados {len(rows)} papéis de trabalho em {OUT}.')

# Papéis gerais além dos papéis individuais por norma.
def aux(name,title,sections):
 d=Document();make_header(d,name,title);d.add_heading(f'{name} — {title}',0)
 d.add_paragraph('SIMPAR S.A. | 2025 consolidado | Preparador: 241003357 | 25/10/2026')
 for h,b in sections:add_section(d,h,b)
 target=OUT/(name.replace(' ','_')+'.docx');d.save(target)
aux('PT-01','Planejamento, materialidade e avaliação preliminar',[
('Objetivo','Planejar academicamente procedimentos sobre demonstrações consolidadas 2025, comparativo 2024, com foco inicial em imobilizado.'),
('Cifras públicas verificadas','Ativo total R$ 88.642.122 mil; imobilizado líquido R$ 47.944.350 mil, comparativo R$ 46.262.499 mil; variação R$ 1.681.851 mil (+3,63%). Fonte: demonstração financeira publicada em R$ mil, cópia reproduzida, PDF p.2; protocol metadata DFP CVM seq.155854.'),
('Materialidade','Benchmark: receita líquida R$ 43.528.375 mil; 0,5% = R$ 217.641,875 mil; execução 75% = R$ 163.231,406 mil; trivial 5% = R$ 10.882,094 mil. Julgamento acadêmico; comparar alternativas no arquivo dados/materialidade.json.'),
('Riscos/afirmações','Existência, integridade, direitos e obrigações, avaliação/alocação, corte, apresentação e divulgação, com foco em bens operacionais, depreciação, vida útil, residual, impairment, baixas, leases e consolidação.'),
('Procedimentos e resultado','Público verificado: metadados CVM e análise horizontal. Planejado: razão/cadastro, recálculo, inspeção física, títulos, impairment e corte. Simulado: base artificial. Evidência insuficiente para conclusão sobre registros individuais.'),
('Conclusão/status','Imobilizado representa 54,1% dos ativos de 2025 e é área relevante de risco. É saldo líquido divulgado, distinto de custo bruto. Não é conclusão de auditoria.')])
aux('PT-02','Base sintética e execução reproduzível',[
('Objetivo/população','Demonstrar análise automatizada sobre 500.000 registros artificiais, sem extrair ou replicar cadastro SIMPAR.'),
('Semente e campos','Semente 241003357. Arquivo dados/base_imobilizado_sintetica.csv; esquema descrito em dados/dicionario_variaveis.md. Campos incluem ID, entidade/classe/descrição fictícias, datas, custo bruto, vida útil, residual, depreciação, valor líquido, localização, situação, data de baixa, centro de custo e taxa.'),
('Anomalias e testes','12 anomalias deliberadas em 8 classes, com correspondência inserida/detectada verificada. CSV de exceções, amostra reproduzível de 100, top 25 por custo bruto e resultados em dados/.'),
('Resultados/limite','500.000 linhas, 499.999 IDs distintos, 12 flags e 12 ocorrências detectadas segundo regras; conferir resultados_testes.txt. Nenhuma exceção real da SIMPAR; nenhuma projeção/extrapolação.'),
('Reprodução','Executar `python3 codigo/01_gerar_base.py` seguido de `python3 codigo/02_testes_base.py`; resultados são reportados por stdout/CSV.')])
aux('PT-03','Programas de auditoria por ciclo',[(k,'\n'.join(f'{h}: {b}' for h,b in v)) for k,v in PROGRAMAS.items()])
aux('PT-04','Matriz de riscos preliminares',[
('Escopo','19 riscos preliminares cobrindo imobilizado/depreciação, receita/recebíveis, caixa, estoques, dívida/arrendamentos, passivos, estimativas/contingências, partes relacionadas, consolidação e continuidade.'),
('Afirmações e resposta','Cada linha da matriz lista afirmações, probabilidade/impacto preliminares, resposta proposta e evidências. “Alta/Média/Baixa” são julgamentos de planejamento e não achados.'),
('Status','Matriz em matrizes/matriz_riscos.csv; procedimentos em matrizes/registro_procedimentos.csv. Nenhum procedimento interno foi executado.')])
aux('PT-05','Conclusão integrada e limitações',[
('Evidência pública','DFP 2025 metadados CVM conferidos. Cifras detalhadas transcritas de cópia reproduzida em publicação financeira, unidade R$ mil, PDF p.2; o PDF RAD integral e nota detalhada de movimentação do imobilizado precisam conferência.'),
('Procedimentos efetivos','Somente pesquisa de fontes públicas, transcrição, cálculos horizontais/verticais e teste da base sintética. Não houve auditoria independente, confirmações, teste de controles, inspeção física, acesso a razão/cadastro/contratos, contato com administração ou exame de papéis de auditores.'),
('Conclusão','O imobilizado líquido é uma área prioritária de planejamento por seu peso relativo e natureza das operações. A evidência pública contextualiza, mas não permite concluir sobre existência, direitos, integridade, avaliação ou suficiência dos saldos. Sem opinião de auditoria.'),
('Pendente','Conferir DFP original/CVM, relatório do auditor e localizadores integrais; revisar itens normativos em fonte oficial; acesso a evidências internas e roteiro visual do professor se disponível.')])
print('Papéis gerais PT-01 a PT-05 também gerados.')
