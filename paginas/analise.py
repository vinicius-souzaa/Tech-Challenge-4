import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
from statsmodels.tsa.seasonal import seasonal_decompose
from util.layout import layout_saida, format_number


st.set_page_config(
    page_title="Analise Exploratória de Dados (EDA)} | {Tech Challenge 4",
    layout="wide",
)

layout_saida()


with st.container():
    st.header(":red[Analise Exploratória de Dados (EDA)]")

    st.markdown("""
        <h1 style='text-align:justify; 
        font-size:15px;
        font-family: Arial, sans-serif; 
        font-weight: normal;
        line-height:1.5'>
                
        A análise exploratória de dados (EDA) é uma etapa fundamental no processo de compreensão 
        e interpretação de conjuntos de dados, especialmente no contexto de séries temporais, como os 
        preços históricos do petróleo Brent. Este processo envolve a utilização de técnicas estatísticas 
        e ferramentas de visualização para descobrir padrões, identificar anomalias, testar hipóteses e 
        verificar suposições através de resumos estatísticos e gráficos.</h1>
        """,unsafe_allow_html=True,
        )
    
    tab0, tab1, tab2, tab3, tab4, tab5 = st.tabs(
        tabs=[
            "Analise Descritiva",
            "Recorrencia dos precos",
            "Tendencias",
            "Desvio Padrao e Volatilidade",
            "Outliers",
            "Decomposicao"
            
        ]
    )
    
    with tab0:
        st.subheader(":red[Análise descritiva]", divider="red")

        st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>
            
            A análise descritiva é uma etapa essencial na compreensão de séries temporais, como os preços 
            históricos do petróleo Brent. Através de medidas estatísticas resumidas, podemos obter uma visão 
            clara das principais características dos dados, identificando padrões e comportamentos que podem 
            influenciar decisões estratégicas.

            Ao analisar a série temporal do petróleo Brent, observamos que a base de dados contém <strong style='font-size: 18px'>11.203</strong> 
            registros de preços diários do barril de petróleo. A média dos preços ao longo do período analisado 
            é de aproximadamente <strong style='font-size: 18px'>53,11\$</strong> por barril, refletindo um valor médio significativo que incorpora 
            diversas flutuações de mercado ao longo dos anos.

            O valor mínimo registrado é de <strong style='font-size: 18px'>9,10\$</strong>, indicando períodos de preços extremamente baixos, 
            possivelmente durante crises econômicas ou excessos de oferta. Em contrapartida, o valor máximo 
            alcançou <strong style='font-size: 18px'>143,95\$</strong>, sugerindo picos de preços em momentos de alta demanda ou eventos geopolíticos 
            significativos que afetaram a oferta.

            Dividindo os dados em quartis, vemos que <strong style='font-size: 18px'>25%</strong> dos preços foram inferiores a 20,53 dólares, 
            enquanto <strong style='font-size: 18px'>50%</strong> dos preços (mediana) ficaram abaixo de <strong style='font-size: 18px'>48,40\$</strong>, 
            e <strong style='font-size: 18px'>75%</strong> dos preços foram inferiores 
            a <strong style='font-size: 18px'>76,61%</strong>. Esses valores demonstram a ampla variação nos preços do petróleo Brent, 
            evidenciada ainda mais pelo desvio padrão de <strong style='font-size: 18px'>33,22%</strong>, 
            que indica uma volatilidade considerável.

            Essas medidas descritivas destacam a natureza volátil e imprevisível do mercado de petróleo, 
            onde os preços podem ser altamente sensíveis a fatores econômicos, políticos e ambientais. 
            A compreensão desses aspectos é crucial para a modelagem precisa e a previsão dos preços futuros 
            do petróleo Brent, auxiliando na tomada de decisões estratégicas no setor energético.</h1>
            """,unsafe_allow_html=True,
            )
                  


        file_path = './dataframe/preco_petroleo.csv'
        df = pd.read_csv(file_path, delimiter=';', skiprows=1, header=None)
        df.columns = ['ds', 'y']

        # Converter a coluna 'ds' para datetime
        df['ds'] = pd.to_datetime(df['ds'], format='%d/%m/%Y')

        # Converter a coluna 'y' para float
        df['y'] = df['y'].str.replace(',', '.').astype(float)
        df_describe = df.describe()
        # Renomear as medidas
        df_describe = df_describe.rename(index={
            "count": "Quantidade de Linhas",
            "mean": "Media",
            "std": "Desvio Padrão",
            "min": "Minima no período",
            "25%": "1º Quartil",
            "50%": "Mediana",
            "75%": "3º quartil",
            "max": "Maxima no período"
            })
        medida_count = df_describe.loc["Quantidade de Linhas"]["y"]
        medida_mean = df_describe.loc["Media"]["y"]
        medida_std = df_describe.loc["Desvio Padrão"]["y"]
        medida_min = df_describe.loc["Minima no período"]["y"]
        medida_25 = df_describe.loc["1º Quartil"]["y"]
        medida_50 = df_describe.loc["Mediana"]["y"]
        medida_75 = df_describe.loc["3º quartil"]["y"]
        medida_max = df_describe.loc["Maxima no período"]["y"]
        df_describe.reset_index(inplace=True)
        df_describe.columns = ["Medidas", "abc","Preço do barril de petróleo"]
        df_describe = df_describe.drop('abc',axis=1)

        with st.container():
            _, col, _ = st.columns([1, 4, 1])

            with col:
                st.dataframe(df_describe, use_container_width=True, hide_index=True)

    with tab1:
        st.subheader(":red[Recorrência dos preços]", divider="red")

        st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>
            
            A análise da recorrência de valores dos preços do petróleo Brent revela uma distribuição variada 
            ao longo do tempo. Ao dividir os dados em intervalos específicos de preço, podemos observar padrões 
            interessantes:</h1>
            """,unsafe_allow_html=True,
            )
        
        # Criando o histograma com Plotly Express
        fig = px.histogram(df, x='y', nbins=14, 
                        title='Histograma dos Preços do Petróleo Brent',
                        color_discrete_sequence=['#8c8787'])

        # Atualizando o layout do gráfico
        fig.update_layout(
            xaxis_title='Preço',
            yaxis_title='Recorrência das Faixas de Preço',
            
        )

        # Atualizando a cor das barras
        fig.update_traces(marker_color='#FF4B4B')

        # Renderizando o gráfico no Streamlit
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>
            <strong>Intervalo (0, 10):</strong> Este intervalo apresenta o menor número de ocorrências com apenas
            <strong style='font-size: 18px'>25</strong>, 
            indicando períodos raros em que os preços do petróleo Brent foram muito baixos.

            <strong>Intervalo (10, 20):</strong> É o intervalo mais frequente, com 
            <strong style='font-size: 18px'>2631</strong> ocorrências. Isso sugere que os 
            preços frequentemente se mantiveram nessa faixa ao longo dos anos.

            <strong>Intervalos (20, 30):</strong> Segundo intervalo de valor com mais frequência
            contabilizando <strong style='font-size: 18px'>1531</strong>. 

            <strong>Intervalos (30, 40) ate (110 a 120):</strong> Esses intervalos mostram uma redução gradual 
            no número de ocorrências à medida que os preços aumentam, refletindo variações menos frequentes 
            em faixas de preço mais altas e mantendo uma media de 750 recorrências por faixa.
            
            <strong>Intervalos superiores a 120:</strong> Valores acima de 120 são menos frequentes, indicando momentos de 
            alta significativa nos preços do petróleo Brent.
                    
            Essa distribuição ilustra a volatilidade e a variabilidade dos preços do petróleo ao longo do 
            tempo, influenciada por uma série de fatores econômicos, geopolíticos e ambientais. O entendimento 
            desses padrões é crucial para previsões futuras e para a gestão de riscos no mercado de energia global.
            </h1>
            """,unsafe_allow_html=True,
            )
        
    with tab2:
        st.subheader(":red[Tendencias]", divider="red")
        st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>
                    
            Na análise de séries temporais financeiras, como o preço do petróleo Brent, a identificação 
            de tendências é essencial para entender a direção geral dos movimentos de mercado ao longo do tempo. 
            Uma ferramenta poderosa utilizada para este fim é a média móvel. A média móvel é um indicador que 
            suaviza as flutuações diárias dos preços, calculando o valor médio de um determinado número de 
            períodos consecutivos. Isso ajuda a revelar padrões subjacentes e tendências de longo prazo, 
            filtrando o ruído presente nos dados diários.

            Ao aplicar a média móvel aos preços do petróleo Brent, podemos visualizar de maneira mais clara 
            e precisa se há uma tendência ascendente, descendente ou lateral nos preços ao longo do tempo. 
            A escolha do período da média móvel, como 30 dias, 90 dias ou 180 dias, determina o quão sensível 
            o indicador será às variações de curto prazo versus a captura de movimentos de médio a longo prazo.

            Este método não apenas facilita a interpretação visual das tendências, mas também serve como base 
            para estratégias de negociação e decisões de investimento, ao destacar períodos de crescimento 
            consistente ou reversões significativas nos preços. A análise da média móvel no contexto do 
            preço do petróleo Brent é crucial para gestores de portfólio, analistas de mercado e outros 
            profissionais que dependem de insights precisos para orientar suas estratégias financeiras.
            
            
            </h1>
            """,unsafe_allow_html=True,
            )
        
        # Filtrar os dados de 2020 até hoje
        df_filtrado = df.loc[df['ds'] >= '2020-01-01']

        # Calcular as médias móveis
        df_filtrado['Média Móvel (30 dias)'] = df_filtrado['y'].rolling(window=30).mean()
        df_filtrado['Média Móvel (90 dias)'] = df_filtrado['y'].rolling(window=90).mean()
        df_filtrado['Média Móvel (180 dias)'] = df_filtrado['y'].rolling(window=180).mean()

        # Plotar o gráfico com Plotly
        fig = go.Figure()

        # Adicionar as séries temporais originais
        fig.add_trace(go.Scatter(x=df_filtrado['ds'], y=df_filtrado['y'], mode='lines', name='Preço Diário', line=dict(color='blue')))

        # Adicionar as médias móveis
        fig.add_trace(go.Scatter(x=df_filtrado['ds'], y=df_filtrado['Média Móvel (30 dias)'], mode='lines', name='Média Móvel (30 dias)', line=dict(color='red')))
        fig.add_trace(go.Scatter(x=df_filtrado['ds'], y=df_filtrado['Média Móvel (90 dias)'], mode='lines', name='Média Móvel (90 dias)', line=dict(color='green')))
        fig.add_trace(go.Scatter(x=df_filtrado['ds'], y=df_filtrado['Média Móvel (180 dias)'], mode='lines', name='Média Móvel (180 dias)', line=dict(color='purple')))

        # Configurar o layout do gráfico
        fig.update_layout(title='Análise de Médias Móveis do Preço do Petróleo Brent (2020 - Hoje)',
                            xaxis_title='Data',
                            yaxis_title='Preço (USD)',
                            
                            xaxis=dict(tickformat='%Y'),
                            legend=dict(orientation="h", yanchor="top", y=1.1, xanchor="center", x=0.5),
                            )

        # Exibir o gráfico
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>
                    
            Na análise de séries temporais financeiras, como o preço do petróleo Brent, a identificação 
            de tendências é essencial para entender a direção geral dos movimentos de mercado ao longo do tempo. 
            Uma ferramenta poderosa utilizada para este fim é a média móvel. A média móvel é um indicador que 
            suaviza as flutuações diárias dos preços, calculando o valor médio de um determinado número de 
            períodos consecutivos. Isso ajuda a revelar padrões subjacentes e tendências de longo prazo, 
            filtrando o ruído presente nos dados diários.

            Ao aplicar a média móvel aos preços do petróleo Brent, podemos visualizar de maneira mais clara 
            e precisa se há uma tendência ascendente, descendente ou lateral nos preços ao longo do tempo. 
            A escolha do período da média móvel, como 30 dias, 90 dias ou 180 dias, determina o quão sensível 
            o indicador será às variações de curto prazo versus a captura de movimentos de médio a longo prazo.

            Este método não apenas facilita a interpretação visual das tendências, mas também serve como base 
            para estratégias de negociação e decisões de investimento, ao destacar períodos de crescimento 
            consistente ou reversões significativas nos preços. 
                    
            </h1>
            """,unsafe_allow_html=True,
            )
    
    with tab3:
        st.subheader(":red[Desvio Padrao e Volatilidade]", divider="red")
        st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>
                    
            A análise de desvio padrão e volatilidade é fundamental para entender as flutuações e o 
            risco associado aos preços do petróleo Brent. O desvio padrão mede a dispersão dos preços 
            em torno da média, enquanto a volatilidade avalia a intensidade das variações de preço ao 
            longo do tempo. Altos níveis de volatilidade podem indicar mercados instáveis ou períodos de 
            incerteza econômica, tornando-se um indicador crucial para tomada de decisão. 
            Nesta seção, exploramos a volatilidade dos preços do petróleo Brent, visualizando o desvio padrão 
            ao longo de diferentes períodos para fornecer insights sobre a estabilidade do mercado e possíveis 
            riscos futuros.
            
            Através do gráfico apresentado a seguir, é possível analisar a instabilidade do petróleo brent 
            e realizar uma comparação da volatilidade através dos períodos de 1987 a 2024.
            
            </h1>
            """,unsafe_allow_html=True,
            )
        

        # Definir a coluna 'ds' como índice
        df.set_index('ds', inplace=True)

        # Calculando desvio padrão e volatilidade
        df['Desvio Padrão (30 dias)'] = df['y'].rolling(window=30).std()

        # Criar a figura do Plotly
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df.index, y=df['y'], mode='lines', name='Preço Diário', line=dict(color='#FF4B4B')))
        fig.add_trace(go.Scatter(x=df.index, y=df['Desvio Padrão (30 dias)'], mode='lines', name='Desvio Padrão (30 dias)', line=dict(color='blue')))

        # Atualizar o layout da figura
        fig.update_layout(
            title='Análise de Volatilidade do Preço do Petróleo Brent',
            xaxis_title='Data',
            yaxis_title='Preço (USD) / Desvio Padrão',
            template='plotly_white',
            
            xaxis=dict(tickformat='%Y'),
            legend=dict(orientation="h", yanchor="top", y=1.1, xanchor="center", x=0.5),
        )

        # Mostrar o gráfico no Streamlit
        st.plotly_chart(fig, use_container_width=True)


        
    
    with tab4:
        st.subheader(":red[Outliers]", divider="red")
        st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>
                    
            Outliers podem indicar eventos anômalos ou erros de medição que podem distorcer a análise 
            e previsões subsequentes. Identificar e tratar esses valores atípicos permite uma melhor 
            compreensão dos padrões subjacentes e das tendências gerais do mercado. Nesta seção, 
            utilizamos métodos visuais como boxplots e violin plot para detectar outliers no conjunto de dados, 
            destacando pontos de dados que se desviam significativamente da distribuição esperada.
            Combinar o boxplot dentro de um violin plot proporciona uma visão mais completa, pois o 
            violin plot além de mostrar a distribuição dos dados, também destaca a densidade e a forma 
            da distribuição, ampliando a compreensão dos comportamentos extremos da série temporal.
            Essa análise fornece insights importantes para decisões estratégicas e para a modelagem 
            precisa de séries temporais.
            
            
            </h1>
            """,unsafe_allow_html=True,
            )
                
        # Dados de exemplo (substitua df['y'] pelo seu DataFrame e coluna)
        data = df['y']

        # Criando o histograma com linha de densidade (kde)
        fig = go.Figure(data=go.Violin(y=df['y'], box_visible=True, line_color='black',
                               meanline_visible=True, fillcolor='#FF4B4B', opacity=0.5,
                               x0='Preço Petróleo Brent'))

        fig.update_layout(title='Distribuição dos Preços do Petróleo Brent',
                  yaxis_title='Preço',
                  yaxis_zeroline=False)

        st.plotly_chart(fig, use_container_width=True)

           
    with tab5:
        st.subheader(":red[Decomposição]", divider="red")
        st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>
                    
            A decomposição da série temporal é uma abordagem que divide uma série em seus componentes principais:
            tendência, sazonalidade e resíduo. Entender esses componentes é crucial para fazer previsões acuradas, pois
            nos ajuda a reconhecer padrões básicos e ciclos regulares. A tendência indica a direção geral da série ao longo
            do tempo, enquanto a sazonalidade expõe padrões recorrentes em períodos fixos, e o resíduo reflete as
            flutuações aleatórias remanescentes. Analisando a série em termos destes elementos, podemos selecionar o
            modelo preditivo mais adequado e determinar se a série é aditiva ou multiplicativa. Se a sazonalidade ou
            tendência muda conforme o nível da série, podemos concluir que ela é multiplicativa e, devido ao excesso de
            ruído e oscilação, não é estacionária.
            
            </h1>
            """,unsafe_allow_html=True,
            )
                
        # Decomposição da série temporal para identificar sazonalidade, tendência e resíduos
        decomposition = seasonal_decompose(df['y'], model='additive', period=365)
        trend = decomposition.trend
        seasonal = decomposition.seasonal
        residual = decomposition.resid

        # Plotando os componentes da decomposição
        fig = make_subplots(rows=4, cols=1, shared_xaxes=True, subplot_titles=['Serie Temporal','Tendencia','Sazonalidade', 'Resíduos'])

        fig.add_trace(go.Scatter(x=df.index, y=df['y'], mode='lines', name='Original',line=dict(color='#FF4B4B')), row=1, col=1)
        fig.add_trace(go.Scatter(x=df.index, y=trend, mode='lines', name='Tendência', line=dict(color='blue')), row=2, col=1)
        fig.add_trace(go.Scatter(x=df.index, y=seasonal, mode='lines', name='Sazonalidade', line=dict(color='green')), row=3, col=1)
        fig.add_trace(go.Scatter(x=df.index, y=residual, mode='lines', name='Resíduos', line=dict(color='black')), row=4, col=1)

        fig.update_layout(xaxis=dict(tickformat='%Y'),
                          title_text='Decomposição da Série Temporal do Preço do Petróleo Brent')
        
        st.plotly_chart(fig, use_container_width=True)
    
    
