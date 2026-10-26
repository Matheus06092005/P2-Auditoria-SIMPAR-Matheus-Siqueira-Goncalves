[README.md](https://github.com/user-attachments/files/33941696/README.md)
[README.md](https://github.com/user-attachments/files/33941683/README.md)
# Dossiê Acadêmico de Auditoria — SIMPAR S.A. (2025)

**Matrícula:** 241003357 · **Período:** exercício encerrado em 31/12/2025 · **Comparativo:** 2024 · **Data:** 25/10/2026 · **Idioma:** português brasileiro.

## Uso e na# Dossiê SIMPAR 2025 — pacote organizado

- `Dossie/`: documento principal em Word e PDF, README, validação e subpasta `Papeis_de_Trabalho/` com os papéis individuais.
- `Base Simulado/`: base artificial completa, amostra, anomalias inseridas, dicionário e maiores saldos sintéticos. Os dados são exclusivamente sintéticos.
- `Planilhas/`: planilha de análises e matriz normativa em Excel.
- `Matriz Normas e Fontes/`: matrizes de normas, riscos, fontes, limitações e procedimentos; inclui o registro de evidências externas.
- `Codigo/`: scripts Python. A reprodução integral espera a estrutura de pastas original descrita no README dentro de `Dossie/`.
- `Resultados/`: relatórios de testes, resultados analíticos e gráficos.
- `Dados Publicos/`: PDFs públicos consultados, incluindo reprodução secundária das demonstrações e Relatório Anual Integrado.

A cópia das demonstrações é uma reprodução secundária; a conferência do PDF integral do RAD/CVM permanece pendente. O trabalho é acadêmico e não constitui relatório nem opinião de auditoria independente.
tureza do material

Este pacote contém análise acadêmica de informações públicas e procedimentos planejados. Não constitui auditoria independente, não é recomendação de investimento, não emite opinião e não atesta que as demonstrações estejam livres de distorção relevante. Procedimentos que dependem de livros contábeis, cadastro de ativos, contratos, confirmações, inspeção, atas, respostas legais ou auditores de componentes aparecem como Planejados ou Pendentes e não foram executados.

O CSV de 500.000 linhas é inteiramente sintético, seed 241003357, sem registros ou nomes reais. Doze anomalias foram deliberadamente inseridas; os testes conferem correspondência entre inserções e detecções. Os resultados sintéticos não são achados, não são amostra do cadastro SIMPAR e não podem ser extrapolados.

As demonstrações consolidadas detalhadas foram conferidas em cópia reproduzida na imprensa, publicada em 31/03/2026, não no download direto do RAD. A página da CVM confirmou metadados da DFP 2025, o período, o protocolo e o auditor indicado, mas a interface não entregou suas tabelas/arquivo integral no amb[README_ORGANIZACAO.md](https://github.com/user-attachments/files/33941706/README_ORGANIZACAO.md)iente. A cópia detalhada é PDF p. 2 e os valores estão em R$ mil. Conferir os localizadores de nota e página na DFP original antes de submissão acadêmica definitiva. Ver `fontes/EVIDENCIAS_EXTERNAS.md` e `matrizes/registro_limitacoes.csv`.

Nenhuma fotografia de terceiros foi incorporada. Os elementos visuais são gráficos/fluxograma próprios, criados por código e com fontes/notas metodológicas, evitando uso sem autorização de imagens da companhia.

## Artefatos

- `Dossie_Auditoria_SIMPAR_2025.docx` — documento editável principal.
- `Dossie_Auditoria_SIMPAR_2025.pdf` — versão final para leitura/impressão.
- `workpapers/PT-EC.docx` e `PT-200.docx`…`PT-600.docx` — um papel para cada critério normativo (Estrutura Conceitual + as 26 NBC TA explicitamente enumeradas; 27 documentos ao todo).
- `workpapers/PT-01.docx`…`PT-05.docx` — planejamento, base sintética, programas por ciclo, riscos e conclusão.
- `dados/base_imobilizado_sintetica.csv` — 500.000 linhas artificiais.
- `dados/dicionario_variaveis.md`, `amostra_sintetica_100.csv`, `top25_custo_bruto_sintetico.csv`, `registro_excecoes_inseridas.csv`, `resultados_testes.txt`.
- `dados/Dossie_SIMPAR_Analises.xlsx` — abas de leitura, comparativo, materialidade, riscos, testes, fontes e cobertura normativa.
- `codigo/` — scripts para geração, testes, análise, gráficos, planilha, Word, fontes e reprodução.
- `matrizes/` — cobertura normativa em CSV e `Matriz_Cobertura_Normas.xlsx`, riscos, fontes, procedimentos e limitações em CSV.
- `graficos/` — arquivos PNG e Mermaid do fluxograma; gráficos gerados por Python.
- `fontes/` — cópias locais dos PDFs consultados e registro de evidências externas.

## Dependências e ambiente

Requer Python 3, pacotes `pandas`, `matplotlib`, `xlsxwriter`, `python-docx`, e `libreoffice` com `pdftotext`/Poppler (para extração local de PDFs e conversão DOCX→PDF). Instale os pacotes Python com:

```bash
python3 -m pip install pandas matplotlib xlsxwriter python-docx
```

No Ubuntu, ferramentas de sistema podem ser instaladas com `sudo apt install libreoffice poppler-utils`. A extração local de texto é opcional à reprodução analítica; a pesquisa e download automatizado da CVM NÃO estão implementados.

## Reproduzir a geração

Na raiz do projeto:

```bash
python3 codigo/run_all.py
```

O fluxo é: regenerar CSV sintético; testar população/anomalias; calcular comparativos/materialidade; gerar matrizes; gerar quatro gráficos; criar planilha; gerar papéis de trabalho; gerar DOCX e PDF; executar `codigo/08_validar.py` para checagens mecânicas de integridade/abertura. A validação não substitui revisão humana nem procedimentos de auditoria. A execução completa substitui resultados anteriores e reescreve o CSV de 500 mil linhas.

Comandos parciais:

```bash
python3 codigo/01_gerar_base.py
python3 codigo/02_testes_base.py
python3 codigo/03_analiticos.py
python3 codigo/cobertura.py
python3 codigo/04_graficos.py
python3 codigo/05_planilhas.py
python3 codigo/07_docs.py
python3 codigo/06_dossie.py
```

`codigo/00_extrair_dados_publicos.py caminho/arquivo.pdf` executa apenas `pdftotext` em PDFs locais; não baixa documentos nem simula extração automatizada da CVM.

## Principais valores públicos interpretados corretamente

As demonstrações da cópia consultada estão em R$ mil. Em 2025: ativo total 88.642.122; imobilizado líquido 47.944.350; receita líquida 43.528.375; lucro das operações continuadas 215.250 e resultado de operações descontinuadas (2.609), perfazendo lucro líquido total de 212.641. Assim, R$ 215.250 mil não é o lucro líquido total do exercício. O saldo de imobilizado é valor contábil líquido, não custo bruto.

Materialidade preliminar selecionada: 0,5% da receita consolidada = R$ 217.641,875 mil; execução 75% = R$ 163.231,406 mil; trivial 5% = R$ 10.882,094 mil. São julgamentos didáticos; o dossiê inclui alternativas e não os trata como percentuais normativos obrigatórios.

O resumo do relatório do auditor reproduzido na cópia consultada declara opinião “sem modificação” (PDF p. 4); o relatório completo não foi obtido e não foi avaliado. A DRA consolidada informa resultado abrangente de R$ 1.650.658 mil (2025) e -R$ 265.048 mil (2024). A cópia apresenta diferença aparente de R$ 14 mil entre saldo comparativo do PL no balanço e na DMPL; confirmar na DFP original.

## Pendências relevantes para revisão final

1. Baixar/arquivar o PDF RAD original da DFP 2025 e conferi-lo contra a cópia reproduzida, com paginação e notas integrais.
2. Obter o relatório completo do auditor, conferir o resumo publicado (“sem modificação”) e avaliar principais assuntos/ênfases. Obter e analisar as informações financeiras segmentadas e suas reconciliações na DFP integral.
3. Concluir conferência item a item dos textos NBC TA oficiais, referências a itens e vigência; revisões 240(R2) e 570(R1) foram publicadas em 2026 e não foram aplicadas retroativamente ao período 2025.
4. Obter roteiro visual do professor se o “item 5” referido no anexo for requerido; não foi localizado entre os arquivos disponibilizados.
5. Se o objetivo for uma auditoria real, obter autorização e evidência interna: cadastro e razão, contratos, inventários, confirmações, fluxos, covenant, pareceres jurídicos e comunicação com auditores de componentes.
6. Resolver a diferença aparente de R$ 14 mil no PL comparativo de 2024 entre balanço e DMPL na cópia reproduzida, conferindo o documento RAD original.

## Como editar sem Adobe

Abra o DOCX e o XLSX com LibreOffice Writer/Calc (gratuitos) ou Microsoft Word/Excel. O PDF pode ser visualizado com qualquer leitor; use LibreOffice para exportar revisões do DOCX para PDF. Não remova as ressalvas de natureza acadêmica, a distinção lucro continuado/lucro líquido total, a unidade R$ mil nem as legendas “sintético”.
