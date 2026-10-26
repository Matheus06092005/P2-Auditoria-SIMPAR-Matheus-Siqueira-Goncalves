# Dicionário de variáveis — base patrimonial sintética

**Status:** SIMULADO. Base criada artificialmente por `codigo/01_gerar_base.py`; não extraída de sistemas SIMPAR, não vinculada a ativo real. Semente 241003357, corte didático 31/12/2025, 500.000 registros. Valores monetários em reais nominais artificiais. Não calibrada ao saldo oficial.

| Campo | Tipo | Definição / regra |
|---|---|---|
| `id_ativo_sintetico` | texto | Identificador artificial; uma duplicação deliberada para testar unicidade. |
| `entidade_sintetica` | texto | Entidade fictícia A–D; nomes genéricos, não correspondem ao grupo real. |
| `classe` | texto | Categoria sorteada entre oito classes artificiais. |
| `descricao_sintetica` | texto | Descrição artificial baseada no número de linha. |
| `data_aquisicao` | ISO AAAA-MM-DD | Data artificial entre 01/01/2008 e 31/12/2025. |
| `data_disponivel_para_uso` | ISO AAAA-MM-DD | Data artificial de aquisição a até 90 dias, limitada ao corte, exceto uma exceção deliberada. |
| `custo_bruto_R$` | inteiro | Custo bruto artificial positivo, gerado por distribuição lognormal. Não é valor publicado da SIMPAR. |
| `vida_util_anos` | inteiro | Vida útil didática selecionada de conjunto finito; dois casos deliberados iguais a zero. |
| `valor_residual_R$` | inteiro | Residual sintético; um caso deliberado superior ao custo. |
| `depreciacao_acumulada_R$` | inteiro | Depreciação acumulada sintética; três acima do custo e um negativo são deliberados. |
| `valor_contabil_liquido_R$` | inteiro | `custo_bruto_R$ − depreciacao_acumulada_R$`; valores negativos são possíveis nos erros artificiais. |
| `taxa_depreciacao_anual` | decimal | Inverso da vida útil, zero quando vida útil é zero; simplificação ilustrativa, não política contábil. |
| `localizacao_sintetica` | texto | Região artificial; um campo em branco deliberado. |
| `situacao_sintetica` | texto | Status fictício; dois ativos baixados com saldo líquido positivo deliberados. |
| `data_baixa` | ISO AAAA-MM-DD/vazio | Data preenchida para os casos deliberados de baixa. |
| `centro_custo_sintetico` | texto | Código de centro fictício. |
| `flag_anomalia_inserida` | SIM/NAO | Marca apenas os 12 registros deliberadamente alterados pelo gerador. |
| `tipo_anomalia_sintetica` | texto/vazio | Nome da regra inserida, vazio em registros sem erro deliberado. |

## Regras de teste

1. Depreciação acumulada acima de custo: três registros.
2. Vida útil menor ou igual a zero: dois registros.
3. Status “Baixado” e valor contábil líquido positivo: dois registros.
4. Disponibilidade após 31/12/2025: um registro.
5. Localização ausente: um registro.
6. Depreciação acumulada negativa: um registro.
7. Identificador duplicado: um registro duplicado adicional (500.000 linhas e 499.999 IDs distintos).
8. Residual acima de custo: um registro.

Os testes verificam contagens conhecidas no conjunto artificial. Não são procedimentos de auditoria sobre a companhia; não se projeta a frequência nem o valor de qualquer exceção para dados reais. O saldo oficial de imobilizado é valor contábil líquido e não é igual ao custo bruto sintético. Não há reconciliação à DFP, ao razão ou ao cadastro patrimonial.
