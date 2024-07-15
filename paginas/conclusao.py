import streamlit as st
from util.layout import layout_saida

st.set_page_config(
    page_title="Conclusão | Tech Challenge 4",
    layout="wide",
)
layout_saida()

with st.container():
    st.header(":red[Conclusão]", divider="red")
    st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>
                    
            Para concluir o projeto de consultoria envolvendo análise e previsão dos preços do petróleo Brent, 
            utilizamos o modelo Prophet para realizar as previsões de série temporal. Ao analisar as métricas de 
            desempenho do modelo, observamos que para um horizonte de previsão de 9 dias, o modelo apresentou um 
            MSE de 44.82, RMSE de 6.69, MAE de 4.69 e MAPE de 5.36%. Para um horizonte mais longo de 90 dias, 
            as métricas foram MSE: 269.90, RMSE: 16.43, MAE: 12.02 e MAPE: 13.47%. Essas métricas indicam uma 
            performance aceitável do modelo, com uma cobertura de 48.16% para o primeiro intervalo e 85.05% para 
            o segundo, sugerindo que o modelo captura bem as tendências de curto e médio prazo.

            O Prophet foi configurado com seus hiperparâmetros que se adaptam ao contexto do nosso projeto, 
            que incluem sazonalidade aditiva, capacidade de ajuste de mudanças sazonais 
            e ajuste automático de incertezas. Para melhorar a precisão da previsão, considerar variáveis 
            exógenas como dados macroeconômicos e noticia, poderia ser explorado. Além do Prophet, outras 
            tecnologias como modelos de rede neural recorrente (RNNs) ou Long Short-Term Memory (LSTM) 
            poderiam ser implementadas para capturar relações não-lineares e dependências de longo prazo 
            nos dados de série temporal, potencialmente aumentando a acurácia das previsões.

            Em resumo, o projeto não apenas desenvolveu um dashboard interativo para análise de insights relevantes 
            sobre os preços do petróleo, mas também implementou um modelo preditivo robusto. O uso do Streamlit 
            para deploy em produção garante que o modelo seja acessível e útil para decisões futuras do cliente.
            
            </h1>
            """,unsafe_allow_html=True,
            )