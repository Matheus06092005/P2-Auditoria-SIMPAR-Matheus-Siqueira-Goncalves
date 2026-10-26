from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SEED=241003357
DATA_CUTOFF='2025-12-31'
ACCESS_DATE='2026-10-25'
# Valores em R$ mil, demonstrações financeiras consolidadas de 2025 e 2024.
FINANCIALS={
 'Ativo total':(88642122,84025791),
 'Imobilizado líquido':(47944350,46262499),
 'Receita líquida':(43528375,40738086),
 'Lucro líquido do exercício':(212641,93833),
 'Lucro de operações continuadas':(215250,89071),
 'Lucro antes de IR/CS':(254114,404692),
 'Caixa e equivalentes':(3029953,1903850),
 'Empréstimos, financiamentos e debêntures — curto prazo':(9148886,6965532),
 'Empréstimos, financiamentos e debêntures — longo prazo':(47519787,48086335),
 'Arrendamentos por direito de uso — curto prazo':(383176,446771),
 'Arrendamentos por direito de uso — longo prazo':(1930507,1675401),
 'Fluxo operacional líquido':(-781548,-3560134),
 'Fluxo de investimento líquido':(-393261,-1528622),
 'Fluxo de financiamento líquido':(2300912,5647131),
 'Variação de caixa líquida':(1126103,558375),
 'Patrimônio líquido consolidado':(7411001,5724991),
 'Estoques':(2831914,3200318),
 'Contas a receber':(7700608,6176225),
 'Provisão para demandas judiciais e administrativas':(535411,670149),
}
# Materialidade preliminar em R$ mil; julgamentos acadêmicos, não percentuais obrigatórios.
MATERIALITY_BENCHMARK='Receita líquida'
MATERIALITY_RATE=0.005
EXECUTION_RATE=0.75
TRIVIAL_RATE=0.05
