# Conteúdo usado por codigo/06_dossie.py e 07_docs.py.
PROGRAMAS = {
'Imobilizado e depreciação': [
('Objetivo','Obter evidência apropriada sobre existência, direitos, integridade, avaliação, corte e apresentação do imobilizado consolidado.'),
('Procedimentos planejados','Obter razão e cadastro por entidade/classe e conciliar com saldo inicial, adições, baixas, depreciação, impairment e saldo final. Testar amostra documental de aquisições/baixas, inspecionar ativos selecionados, testar propriedade/gravames, recalcular depreciação e vidas úteis e avaliar ativos ociosos/impairment. Examinar a classificação de ativos de frota disponíveis para venda e ativos de direito de uso.'),
('Evidências necessárias','Cadastro patrimonial, razão, notas fiscais, aprovações, contratos, títulos, CRLV/registro, evidência de recebimento/uso, inventário, cálculo de depreciação, laudos de impairment e conciliações.'),
('Situação','Planejado/Pendente: não foram obtidos dados internos nem realizada inspeção física. Base sintética é Simulada e não é amostra da população real.')],
'Receita e contas a receber':[
('Objetivo','Testar ocorrência, integridade, precisão, corte, apresentação da receita e avaliação/recuperabilidade das contas a receber.'),
('Procedimentos planejados','Selecionar contratos e transações de receita, conferir serviço/entrega/aceite, faturamento e liquidação; analisar transações antes/depois do fechamento; testar cancelamentos, notas de crédito e lançamentos manuais; reconciliar aging e recebimentos posteriores; avaliar modelo de perdas esperadas.'),
('Evidências necessárias','Contratos, ordens, comprovantes de execução/aceite, faturas, notas fiscais, razão, notas de crédito, aging, recibos, cobrança e memória do modelo de perdas.'),
('Situação','Planejado/Pendente: somente cifras públicas e análise horizontal foram obtidas.')],
'Caixa e aplicações financeiras':[
('Objetivo','Testar existência, titularidade, completude, avaliação, classificação e restrições de caixa e aplicações.'),
('Procedimentos planejados','Confirmações externas sob controle do auditor; extratos obtidos independentemente; conciliações bancárias e itens em trânsito; inspeção de acordos de bloqueio/garantia; testar cotação, juros e classificação de títulos.'),
('Evidências necessárias','Confirmações, extratos bancários, conciliações, contratos de aplicação, avisos de restrição/garantia, cálculo de rendimento e evidência de liquidação posterior.'),
('Situação','Planejado/Pendente: nenhum banco foi contatado e não se inferiu disponibilidade integral do saldo.')],
'Estoque e materiais':[
('Objetivo','Obter evidência sobre existência, integridade, condição, avaliação e corte de estoques.'),
('Procedimentos planejados','Acompanhar inventário físico, selecionar itens para contagem bidirecional, testar estoque em terceiros, reconciliação com razão, custo e valor realizável líquido, obsolescência, movimentações perto do fechamento e vendas subsequentes.'),
('Evidências necessárias','Instruções e folhas de contagem, registros de inventário, notas de compra, custos, aging, confirmação de terceiros e vendas posteriores.'),
('Situação','Planejado/Pendente: números agregados públicos não permitem validar existência ou mensuração.')],
'Dívida, arrendamentos e passivos':[
('Objetivo','Testar integridade, obrigação, classificação, juros, vencimentos, covenant, garantias e divulgação de financiamento, arrendamentos e outros passivos.'),
('Procedimentos planejados','Confirmar credores, inspecionar contratos e aditivos, recalcular juros/fees, testar pagamentos posteriores e busca de passivos não registrados, reconciliar cronograma, testar covenants e avaliar curto/longo prazo e notas de arrendamentos.'),
('Evidências necessárias','Confirmações, contratos, extratos, cronograma de dívida, cálculo, certificates de covenants, garantias, invoices e desembolsos posteriores.'),
('Situação','Planejado/Pendente: análise pública de saldos não testa termos, covenants ou completude.')],
'Estimativas e contingências':[
('Objetivo','Avaliar reconhecimento, mensuração, incerteza e divulgação de estimativas e provisões judiciais/administrativas.'),
('Procedimentos planejados','Obter lista integral de processos, circularizar advogados, examinar processos e eventos posteriores, analisar metodologia, premissas, probabilidade, mensuração, mudanças e possível viés; revisar divulgações.'),
('Evidências necessárias','Cartas de assessores jurídicos, processos, atas, pareceres, cálculos, pagamentos, histórico de estimativa e divulgações.'),
('Situação','Planejado/Pendente: valor agregado público não permite concluir suficiência da provisão.')],
'Partes relacionadas':[
('Objetivo','Identificar e testar completude de partes relacionadas, transações, saldos, termos, aprovações e divulgações.'),
('Procedimentos planejados','Inspecionar declarações de administradores, estrutura societária, atas, cadastro de contrapartes, razão, contratos e transações incomuns; verificar aprovações e eliminações intragrupo.'),
('Evidências necessárias','Organograma e controle, cadastro, declarações, atas, contratos, faturas, confirmações, razão e documentos de consolidação.'),
('Situação','Planejado/Pendente: política pública foi lida; a completude do universo não foi verificada.')],
'Consolidação do grupo':[
('Objetivo','Avaliar universo de componentes, instruções de reporte, políticas uniformes, consolidação, eliminações, PNC e suficiência do trabalho de grupo.'),
('Procedimentos planejados','Obter estrutura jurídica, mapear componentes e auditores, definir materialidade por componente, emitir instruções, avaliar independência/competência e comunicação dos auditores de componentes, rever riscos e papéis relevantes, testar ajustes/eliminações e consolidar conclusões.'),
('Evidências necessárias','Organograma, balancetes/pacotes, instruções, confirmações, relatórios e comunicações de componentes, planilhas de consolidação e cálculo de PNC.'),
('Situação','Planejado/Pendente: não houve acesso aos componentes ou papéis de seus auditores.')],
'Continuidade operacional':[
('Objetivo','Avaliar a base de continuidade, incertezas relevantes, premissas e suficiência das divulgações.'),
('Procedimentos planejados','Examinar projeções de fluxo, caixa e vencimentos, covenants, refinanciamentos, stress tests, planos aprovados e viabilidade; confrontar com eventos subsequentes, contratos e evidência externa; avaliar divulgação e comunicação à governança.'),
('Evidências necessárias','Forecast aprovado, sensibilidade, contratos/renegociações, confirmação de crédito, covenant certificates, atas, comunicações jurídicas e divulgações.'),
('Situação','Planejado/Pendente: o FCO consolidado 2025 é negativo e há dados públicos de dívida/caixa, mas esses fatos não bastam para conclusão. Aplicar versão normativa vigente para período iniciado em 2025.')],
}
