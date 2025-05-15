import streamlit as st
from prophet import Prophet
from prophet.plot import plot_plotly
import pandas as pd
from util.layout import layout_saida

st.set_page_config(
    page_title="Modelo Preditivo | Tech Challenge 4",
    layout="wide",page_icon="💻"
)
layout_saida()

with st.container():
    st.header(":red[Modelo Preditivo]", divider="red")
    st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>
                    
            Modelos preditivos para séries temporais desempenham um papel crucial na previsão de 
            tendências e padrões em dados ao longo do tempo. A capacidade de capturar sazonalidades e 
            variações periódicas é fundamental para entender e antecipar comportamentos futuros. 
            O Prophet se destaca nesse cenário ao oferecer uma abordagem flexível e intuitiva, 
            especialmente eficaz para séries que exibem padrões sazonais distintos. Com sua capacidade 
            de modelagem de tendências não lineares e inclusão fácil de feriados e eventos especiais, 
            o Prophet facilita a criação de previsões precisas e ajustáveis, adaptadas às complexidades 
            temporais dos dados, promovendo uma análise robusta e insights acionáveis.
            
            </h1>
            """,unsafe_allow_html=True,
            )
    st.subheader(f":red[Treinamento do Modelo]", divider="red")
    st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>
                    
            Para o treinamento do modelo utilizando a biblioteca Prophet, escolhi os seguintes hiperparâmetros 
            para melhor capturar a sazonalidade dos dados históricos do preço do petróleo Brent:
            
            <strong>seasonality_mode='additive'</strong>
                 
            <strong>daily_seasonality=False</strong>
                 
            <strong>weekly_seasonality=True</strong> 
                
            <strong>yearly_seasonality=True</strong>
                 
            <strong>changepoint_prior_scale=0.5</strong> 
            
            <strong>seasonality_prior_scale=0.01</strong> 
                
            Tais parâmetros e valores foram selecionados apos consulta na documentação da biblioteca meta, na seção de
            tunning de parâmetros.
            
            O <strong>seasonality_mode='additive'</strong> é adequado para adicionar sazonalidades com efeitos constantes 
            ao longo do tempo. Desabilitar a sazonalidade diária <strong>(daily_seasonality=False)</strong>
            reflete a natureza do mercado de commodities. Ativar as sazonalidades semanal e 
            anual <strong>(weekly_seasonality=True e yearly_seasonality=True)</strong> captura padrões semanais e 
            anuais nos preços. Ajustar <strong>changepoint_prior_scale</strong> e <strong>seasonality_prior_scale</strong> controla a 
            flexibilidade do modelo e a influência das mudanças estruturais e sazonalidades, respectivamente.
            
            </h1>
            """,unsafe_allow_html=True,
            )
    st.subheader(f":red[Validacao Cruzada]", divider="red")
    st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>
                    
            A validação cruzada é uma técnica essencial na modelagem de séries temporais, como ao usar o Prophet, 
            para avaliar a performance do modelo de previsão. Ela envolve dividir os dados históricos em múltiplos 
            subconjuntos (folds) e treinar o modelo em diferentes combinações de treinamento e teste. Isso ajuda 
            a garantir que o modelo generalize bem para dados não vistos, evitando overfitting. No contexto do Prophet, 
            a validação cruzada permite avaliar como o modelo se comporta em diferentes períodos temporais, 
            fornecendo uma estimativa robusta da precisão das previsões e ajudando a ajustar os hiperparâmetros
            para melhor performance. 
            
            </h1>
            """,unsafe_allow_html=True,
            )
    st.subheader(f":red[Métricas de Avaliação do Modelo]", divider="red")
    st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>
                    
            Para avaliar a eficácia de um modelo preditivo como o Prophet, diversas métricas são empregadas:

            <strong>MSE (Mean Squared Error):</strong> mede o erro médio ao quadrado entre os valores previstos e os valores reais. 
            Valores menores indicam melhor precisão.
                
            <strong>RMSE (Root Mean Squared Error):</strong> é a raiz quadrada do MSE e fornece a magnitude do erro de previsão.
                
            <strong>MAE (Mean Absolute Error):</strong> calcula o erro absoluto médio entre as previsões e os valores reais, 
            sendo menos sensível a outliers que o MSE.
                
            <strong>MAPE (Mean Absolute Percentage Error):</strong> expressa o erro absoluto médio como uma porcentagem 
            dos valores reais.
                
            <strong>MDAPE (Median Absolute Percentage Error):</strong> similar ao MAPE, mas usa a mediana dos erros percentuais, 
            reduzindo a influência de outliers.
                
            <strong>sMAPE (Symmetric Mean Absolute Percentage Error):</strong> uma variação do MAPE que trata os erros de forma 
            simétrica, independentemente do sinal.
                
            <strong>Coverage:</strong> indica a proporção de valores reais que caem dentro de um intervalo de confiança especificado.
                
            Essas métricas fornecem uma visão abrangente da precisão e da robustez do modelo, 
            auxiliando na escolha do melhor modelo para previsões futuras.
            </h1>
            
            """,unsafe_allow_html=True,
            )
    # Carregar o arquivo CSV
    file_path = './dataframe/resultados-metricas-profit.csv'
    df_prophet_metricas = pd.read_csv(file_path, delimiter=',', skiprows=0)
    
        
    st.dataframe(df_prophet_metricas, use_container_width=True, hide_index=True)

    st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>
                    
            Após a modelagem com o Prophet, obtemos um MAPE de 5,36%, indicando uma alta
            precisão nas previsões do modelo. A cada dia a previsão fica menos acurada, o mape em media 
            cresce 1,16% por dia no período de 90 dias. 
                
            Esse resultado reforça o valor do Prophet como uma
            ferramenta robusta e eficaz para a análise de séries temporais, especialmente em
            contextos complexos como o mercado de ações. O
            </h1>
            
            """,unsafe_allow_html=True,
            )
    
    
    
    st.subheader(f":red[Gráfico da Previsão do Modelo]", divider="red")
    st.markdown("""
                <h1 style='text-align:justify; 
                font-size:15px;
                font-family: Arial, sans-serif; 
                font-weight: normal;
                line-height:1.5'>
                    
                No gráfico abaixo, podemos observar a série temporal do período selecionado para 
                o treinamento do modelo, junto com as faixas de previsão e a projeção dos preços 
                do barril de petróleo feita pelo modelo para os próximos 90 dias.
                </h1>
            
                """,unsafe_allow_html=True,
                )
    
    # Carregar o DataFrame
    file_path = './dataframe/preco_petroleo.csv'
    df_modelo = pd.read_csv(file_path, delimiter=';', skiprows=1, header=None)
    df_modelo.columns = ['ds', 'y']

    # Converter a coluna 'ds' para datetime
    df_modelo['ds'] = pd.to_datetime(df_modelo['ds'], format='%d/%m/%Y')

    # Converter a coluna 'y' para float
    df_modelo['y'] = df_modelo['y'].str.replace(',', '.').astype(float)

    # Filtrar os dados para o período desejado (se necessário)
    df_ml = df_modelo[df_modelo['ds'] >= "2020-01-01"]

    # cria o modelo do prophet com os melhores hiperparâmetros
    modelo = Prophet(seasonality_mode='additive', daily_seasonality=False, 
                    weekly_seasonality=True, yearly_seasonality=True, 
                    changepoint_prior_scale=0.5, seasonality_prior_scale=0.01)
    modelo.add_country_holidays(country_name='BR')
    modelo.fit(df_ml)

    # faz a previsão dos próximos 30 dias para o preço do barril de petróleo do tipo Brent
    df_futuro = modelo.make_future_dataframe(periods=90, freq='D')
    previsao = modelo.predict(df_futuro)


    # plot dos preços históricos (desde 2020) + janela de previsão
    fig = plot_plotly(modelo, previsao,trend=True,  figsize=(1200, 900),xlabel='Data',ylabel='Preco $')


    fig.update_layout(title='Distribuição do valor do barril de petróleo Brent entre 2020 e os dias atuais e previsão dos próximos 90 dias',
                     showlegend=True,
                     legend=dict(orientation="h", yanchor="bottom", y=1, xanchor="center", x=0.5)
                     )

    fig.data[0].name = 'Realidade'
    fig.data[1].name = 'Banda inferior da previsão'
    fig.data[1].fill = 'tonexty'
    fig.data[1].fillcolor = 'rgba(0, 114, 178, 0.2)'
    fig.data[2].name = 'Previsão'
    fig.data[3].name = 'Banda superior da previsão'
    fig.data[4].name = 'Tendência'


    st.plotly_chart(fig, use_container_width=True)

    
    


    
