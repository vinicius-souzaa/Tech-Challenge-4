import streamlit as st
import warnings
import locale
from util.layout import layout_saida


warnings.filterwarnings("ignore")
#locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

st.set_page_config(page_title='Tech Challenge 4', layout="wide",page_icon="🛠️")

layout_saida()

col1,col2 = st.columns([1,1])

with col1:
    st.header("Tech Challenge 4")

with col2:
    st.image("imagens/fiap-logo.jpg", width=280)

    
st.subheader(":red[O Problema]",divider="red")

st.markdown("""
            <h1 style='text-align:justify; 
                        font-size:15px;
                        font-family: Arial, sans-serif; 
                        font-weight: normal;
                        line-height:1.5'>
            Este projeto de consultoria tem como objetivo explorar e analisar dados     
            históricos de preços do petróleo Brent, disponíveis no site do IPEA,     
            com foco em criar um dashboard interativo e desenvolver um modelo de     
            Machine Learning para previsão do preço do petróleo. O petróleo é uma commodity     
            fundamental na economia global, cujos preços são influenciados por uma     
            variedade de fatores como eventos geopolíticos, crises econômicas,     
            demanda global por energia, entre outros. Este projeto visa extrair insights     
            relevantes desses dados para auxiliar na tomada de decisão estratégica.</h1>
            """, unsafe_allow_html=True)

st.subheader(":red[Objetivo]", divider="red")

st.markdown("""
            <h1 style='text-align:justify; 
                        font-size:15px;
                        font-family: Arial, sans-serif; 
                        font-weight: normal;
                        line-height:1.5'>
            O objetivo deste projeto é criar um dashboard interativo que não só visualiza 
            os dados históricos de preços do petróleo, mas também apresenta insights sobre 
            as variações desses preços relacionadas a eventos geopolíticos, crises econômicas 
            e outros aspectos relevantes. Além disso, será desenvolvido um modelo de 
            Machine Learning para realizar previsões diárias do preço do petróleo Brent, 
            utilizando técnicas de séries temporais. O modelo será integrado ao dashboard 
            para fornecer uma ferramenta completa de análise e previsão</h1>
            """, unsafe_allow_html=True)



st.subheader(":red[Metodologia]", divider="red")

st.markdown("""
            <h1 style='text-align:justify; 
                        font-size:15px;
                        font-family: Arial, sans-serif; 
                        font-weight: normal;
                        line-height:1.5'>
            
            Para abordar o desafio fizemos separamos a metodologia em 7 partes conforme abaixo:
            
            1 - Coleta de Dados: Os dados históricos de preço do petróleo Brent serão obtidos 
            a partir do site do IPEA, em formato de CSV contendo as colunas de data e preço em dólares.\n
            
            2 - Análise Exploratória de Dados: Será realizada uma análise exploratória para entender 
            a distribuição dos preços, identificar tendências, sazonalidades e possíveis outliers. 
            Isso incluirá a visualização dos dados através de gráficos e estatísticas descritivas.

            3 - Desenvolvimento do Dashboard Interativo: Utilizando a biblioteca Streamlit em Python, 
            será desenvolvido um dashboard interativo que permita ao usuário explorar os dados históricos 
            de preço do petróleo. O dashboard incluirá gráficos interativos, tabelas dinâmicas e 
            ferramentas para filtragem por períodos específicos.

            4 - Geração de Insights: A partir da análise dos dados, serão extraídos insights 
            relevantes sobre as variações de preço do petróleo, correlacionando-os com eventos geopolíticos, 
            crises econômicas e outros fatores externos. Pelo menos quatro insights serão destacados e 
            apresentados de forma clara no dashboard.

            5 - Desenvolvimento do Modelo de Machine Learning: Será desenvolvido um modelo de previsão 
            de séries temporais utilizando o algoritmo Prophet da Meta. O modelo será treinado com os 
            dados históricos e avaliado quanto à sua precisão na previsão de preços futuros.

            6 - Plano de Deploy em Produção: Será elaborado um plano para o deploy em produção do dashboard 
            e do modelo de Machine Learning utilizando Streamlit. 
            
            Este plano metodológico visa fornecer uma solução completa e eficiente para análise e previsão 
            de preços do petróleo, utilizando técnicas avançadas de visualização e machine learning.</h1>
            """, unsafe_allow_html=True)


