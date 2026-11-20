# Dicionário de dados: IBGE, Minas Gerais

Gerado automaticamente a partir dos CSVs baixados da API do IBGE (servicodados.ibge.gov.br). Os detalhes de cada indicador estão em `dicionario_indicadores.csv`.

## Colunas dos CSVs

| Coluna | Significado |
|---|---|
| `pesquisa_id` | ID da pesquisa na API do IBGE (servicodados). |
| `pesquisa` | Nome da pesquisa. |
| `nivel` | Nível geográfico da linha: 'municipio' ou 'uf'. |
| `cod_ibge` | Código IBGE de 7 dígitos do município (2 dígitos = UF). Chave para ligar ao shapefile de municípios (campo CD_MUN). |
| `localidade` | Nome do município ou do estado. |
| `caminho_indicador` | Hierarquia do indicador, separada por ' > ' (do tema geral ao específico). |
| `indicador_id` | ID do indicador na API. |
| `posicao` | Posição do indicador na hierarquia da pesquisa (ex.: 1.2.3). |
| `unidade` | Unidade de medida informada pelo IBGE. |
| `ano` | Período de referência (pode vir com sufixo, como 'preliminar'). |
| `valor` | Valor como texto. Pode ser um número ou um símbolo (ver tabela abaixo). |

## Símbolos no campo `valor`

Convenção do IBGE; confirme nas notas de cada pesquisa.

| Símbolo | Significado |
|---|---|
| `-` | Zero verdadeiro (dado numérico igual a zero, não resultante de arredondamento). É dado real. |
| `..` | Não se aplica. |
| `...` | Dado numérico não disponível. |
| `x / X` | Omitido para evitar a identificação de informantes (sigilo estatístico). |
| `0, 0,0` | Zero resultante do arredondamento de um valor positivo. |

## Pesquisas baixadas

| ID | Pesquisa | Níveis | Municípios com dado | Indicadores | Anos |
|---|---|---|---|---|---|
| 14 | Produção Agrícola - Lavoura Temporária | municipio, uf | 852 | 155 | 2021, 2022, 2023, 2024, 2025 |
| 15 | Produção Agrícola - Lavoura Permanente | municipio, uf | 818 | 180 | 2021, 2022, 2023, 2024, 2025 |
| 16 | Extração vegetal e Silvicultura | municipio, uf | 826 | 134 | 2021, 2022, 2023, 2024, 2025 |
| 17 | Mortalidade | municipio, uf | 853 | 125 | 2018, 2019, 2020, 2021, 2022 |
| 18 | Pecuária | municipio, uf | 853 | 72 | 2021, 2022, 2023, 2024, 2025 |
| 22 | Frota de veículos | municipio, uf | 853 | 22 | 2021, 2022, 2023, 2024, 2025 |
| 30 | Pesquisa Nacional de Saneamento Básico | municipio, uf | 853 | 194 | 2008, 2017 |
| 31 | Produção agrícola - Cereais, leguminosas e oleaginosas | municipio, uf | 852 | 75 | 2007 |
| 32 | Serviços de saúde | municipio, uf | 853 | 100 | 2005, 2009 |
| 44 | PNAD - Pesquisa Nacional por Amostra de Domicílios | uf | 0 | 128 | 2011, 2012, 2013, 2014, 2015 |
| 47 | Pesquisa Nacional de Saúde | uf | 0 | 72 | 2019 |
| 10056 | Pesquisa Nacional de Saúde do Escolar | uf | 0 | 77 | 2015, 2019, 2024 |
| 10102 | Censo 2022 | municipio, uf | 853 | 168 | 2022 |
| 10110 | ESTADIC - Suplemento de Segurança Alimentar | uf | 0 | 349 | 2024 |
| 10112 | Dados sobre gênero | municipio, uf | 853 | 28 | 2022 |

## Observações

- Os valores vêm como texto; converta para número só depois de tratar os símbolos.
- `-` é um zero real; `..`, `...` e `x` não devem ser tratados como zero.
- Cobertura municipal baixa costuma indicar pesquisa por amostra ou que cobre só capitais e grandes cidades.
