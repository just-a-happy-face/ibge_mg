import pandas as pd
import numpy as np
import os

#criando a pasta para dados tratados
os.makedirs('dados_tratados', exist_ok=True)

#importando os dicionarios de pesquisa e indicadores
dicionario_indicadores_df = pd.read_csv('dicionario_indicadores.csv', encoding='utf-8')
dicionario_pesquisas_df = pd.read_csv('dicionario_pesquisas.csv')

#mapeando indicadores e pesquisas
mapa_indicadores = dicionario_indicadores_df.set_index('indicador_id')['nome_indicador']
mapa_pesquisas = dicionario_pesquisas_df.set_index('pesquisa_id')['pesquisa']

#importando os datasets - melhorar (DRY) depois
censo_2022_df = pd.read_csv('censo_2022_10102.csv', encoding='utf-8')
dados_sobre_genero_df = pd.read_csv('dados_sobre_genero_10112.csv', encoding='utf-8')
extracao_vegetal_silvicultura_df = pd.read_csv('extracao_vegetal_e_silvicultura_16.csv', encoding='utf-8')
frota_de_veiculos_df = pd.read_csv('frota_de_veiculos_22.csv', encoding='utf-8')
mortalidade_df = pd.read_csv('mortalidade_17.csv', encoding='utf-8')
pecuaria_df = pd.read_csv('pecuaria_18.csv', encoding='utf-8')
pesquisa_nacional_saneamento_basico_df = pd.read_csv('pesquisa_nacional_de_saneamento_basico_30.csv', encoding="utf-8")
pesquisa_nacional_saude_df = pd.read_csv('pesquisa_nacional_de_saude_47.csv', encoding='utf-8')
pesquisa_nacional_saude_escolar_df = pd.read_csv('pesquisa_nacional_de_saude_do_escolar_10056.csv', encoding='utf-8')
pnad_pesquisa_nacional_amostra_domicilios_df = pd.read_csv('pnad___pesquisa_nacional_por_amostra_de_domicilios_44.csv', encoding='utf-8')
producao_agricola_cereais_leguminosas_oleaginosas_df = pd.read_csv('producao_agricola___cereais__leguminosas_e_oleaginosas_31.csv', encoding='utf-8')
producao_agricola_lavoura_permanente_15_df = pd.read_csv('producao_agricola___lavoura_permanente_15.csv', encoding='utf-8')
producao_agricola_lavoura_temporaria_df = pd.read_csv('producao_agricola___lavoura_temporaria_14.csv', encoding='utf-8')
servicos_saude_df = pd.read_csv('servicos_de_saude_32.csv', encoding='utf-8')

#substituindo indicador_id por nome_indicador
conjunto = [
    censo_2022_df,
    dados_sobre_genero_df,
    extracao_vegetal_silvicultura_df,
    frota_de_veiculos_df,
    mortalidade_df,
    pecuaria_df,
    pesquisa_nacional_saneamento_basico_df,
    pesquisa_nacional_saude_df,
    pesquisa_nacional_saude_escolar_df,
    pnad_pesquisa_nacional_amostra_domicilios_df,
    producao_agricola_cereais_leguminosas_oleaginosas_df,
    producao_agricola_lavoura_permanente_15_df,
    producao_agricola_lavoura_temporaria_df,
    servicos_saude_df
    ]

for i in conjunto :
    i['indicador_id'] = i['indicador_id'].map(mapa_indicadores)
    i['pesquisa_id']  = i['pesquisa_id'].map(mapa_pesquisas)
    

