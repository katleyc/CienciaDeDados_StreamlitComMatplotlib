import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./br_rj_rio_de_janeiro_ipp_ips_dimensoes_componentes.csv", sep=",")

st.title("Trabalho Terceiro Bimestre")
st.subheader("Índice de Progresso Social (IPS) do Rio de Janeiro")
st.write("""A base utilizada dispõe de dados de algumas regiões administrativas da cidade do Rio de Janeiro e suas respectivas notas no Índice de Progresso Social (IPS).
         \nAs informações disponíveis contemplam os anos de 2016, 2018 e 2020.""")
st.write(df) # exibe o dataframe


# Primeiro Gráfico
# - Análise da alteração do IPS durante os anos
st.subheader("Média do IPS por Ano")
media_ips = df.groupby("ano")["ips_geral"].mean().reset_index() # agrupa por ano e a variável recebe o valor da média da coluna "ips_geral"
plt.figure(figsize=(10, 6))
plt.plot(media_ips["ano"], media_ips["ips_geral"], marker="o") # gera o gráfico de linha definindo o marcador
plt.title("Média do IPS por Ano") 
plt.xlabel("Ano")
plt.ylabel("Média do IPS")
plt.xticks(media_ips["ano"])  # mantém só os anos que aparecem no df
plt.grid()
st.pyplot(plt) # exibe o gráfico no streamlit

plt.clf() # limpa a figura salva

# Gráfico 2: Cinco maiores notas no ano mais recente da pesquisa (2020)
st.subheader("Maiores Notas de 2020")
plt.figure(figsize=(10, 6))
indices_maiores_notas = df[df["ano"]==2020]["ips_geral"].sort_values(ascending=False).head().index # busca os índices das cidades com maiores notas
plt.bar(df.loc[indices_maiores_notas]["regiao_administrativa"], df.loc[indices_maiores_notas]["ips_geral"]) # cria gráfico de barra com as cidades com as maiores notas
plt.title("Maiores notas na última pesquisa")
plt.xlabel("Cidade")
plt.ylabel("Nota")
plt.grid()
st.pyplot(plt) # exibe o gráfico no streamlit

plt.clf() # limpa a figura salva

# Gráfico 3: Notas nos três anos realizados
st.subheader("Notas nas Três Pesquisas")
anos = df["ano"].unique() # salva os anos presentes no DF
plt.figure(figsize=(16, 6))
for ano in anos: # cada ano é utilizado para imprimir uma linha no gráfico
    plt.scatter(df[df["ano"]==ano]["regiao_administrativa"], df[df["ano"]==ano]["ips_geral"], label=ano) # cria o gráfico de pontos

plt.title("Notas IPS por bairro e Ano")
plt.xlabel("Bairros")
plt.ylabel("Nota IPS")
plt.xticks(rotation=60)  # Rotaciona as legendas para melhorar a legibilidade
plt.grid()
plt.legend(title="Ano")
plt.tight_layout() # busca não sobrepor as legendas
st.pyplot(plt)

plt.clf()

# Gráfico 4: Histograma das notas das necessidades humanas básicas
st.subheader("Notas na Avaliação das Necessidade Humanas Básicas")

plt.figure(figsize=(10, 6))
plt.hist(df["necessidades_humanas_basicas_nota_dimensao"], color="blue") # criação do histograma
plt.title("Histograma das Notas da Avaliação")
plt.xlabel("Valor")
plt.ylabel("Frequência")
plt.grid(axis="y")

st.pyplot(plt)