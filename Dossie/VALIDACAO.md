# Registro de validação do pacote

Validação realizada no ambiente Linux em 25/10/2026. Os resultados refletem a última execução concluída de `codigo/run_all.py`; atualizações normativas posteriores serão incorporadas e testadas em nova execução antes do ZIP final.

| Verificação | Resultado |
|---|---|
| Fluxo integrado `python3 codigo/run_all.py` | Executou até o fim sem erro; scripts de geração, testes, análises, matrizes, gráficos, planilha, papéis e DOCX/PDF concluídos. |
| Base sintética CSV | 500.000 registros de dados, header mais 500.000 linhas. |
| Integridade dos testes artificiais | 12 verificações OK; 12 anomalias deliberadas em 8 classes detectadas na contagem esperada. |
| Identificadores | 499.999 IDs distintos em 500.000 registros (duplicação deliberada). |
| Dossiê PDF | PDF válido, 19 páginas; texto extraído para inspeção; imagens e gráficos incorporados. |
| Dossiê Word | DOCX aberto via `python-docx`; 5 imagens inline e tabelas presentes. |
| Workpapers | 32 DOCX válidos: PT-EC e 26 NBC TA (27 critérios normativos) + PT-01 a PT-05. |
| Planilha | XLSX aberto com `openpyxl`; sete abas, incluindo cobertura normativa; ZIP interno sem erro. |
| Fontes e matrizes | 8 fontes no registro, 19 riscos, 27 critérios normativos e 9 limitações registradas. |
| Somas/cálculos | Fluxos de caixa e composição de lucro líquido conciliados aritmeticamente; análise vertical/horizontal e materialidade calculadas em R$ mil. |

## Limitações de validação

Os testes da base validam somente regras artificiais, não registros SIMPAR. A validação de abertura de DOCX foi por parser e exportação; não se realizou revisão humana em Microsoft Word. A conferência de cifras foi feita na cópia pública reproduzida e comparada aos metadados CVM, não ao PDF RAD integral. Consulte `README.md` e `matrizes/registro_limitacoes.csv` para pendências de auditoria, fonte e norma.


## Complemento: pesquisa normativa concluída (25/10/2026)
A pesquisa item a item foi concluída para a Estrutura Conceitual e as 26 NBC TA listadas no roteiro (27 critérios no total). Os resultados foram confrontados com a matriz e os papéis individuais. Confirmações de transição relevantes: NBC TA 240 (R1) e NBC TA 570 na redação aplicável ao período iniciado em 2025; as revisões publicadas em setembro de 2026 (NBC TA 240 (R2) e NBC TA 570 (R1)) têm aplicação às auditorias de períodos iniciados em ou após 01/01/2027, portanto não foram tratadas como vigentes para o exercício de 2025. A pesquisa normativa não substitui a leitura do relatório de auditoria integral nem a obtenção de evidência interna da SIMPAR.
