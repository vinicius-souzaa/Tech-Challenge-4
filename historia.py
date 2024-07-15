import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import plotly.io as pio
from util.layout import layout_saida

st.set_page_config(
    page_title="História | Tech Challenge 4",
    layout="wide",
)

layout_saida()

with st.container():
    # css específico da página
    #with open("assets/historia.css") as f:
    #    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    st.header(":red[História]", divider='red')
    st.markdown("""
                <h1 style='text-align:justify; 
                font-size:15px;
                font-family: Arial, sans-serif; 
                font-weight: normal;
                line-height:1.5'>

                O preço do petróleo Brent, um dos principais indicadores globais do mercado de petróleo, 
                tem uma história marcada por flutuações significativas influenciadas por uma variedade 
                de eventos geopolíticos, econômicos e ambientais. Desde sua adoção como benchmark em 1983, 
                o Brent, extraído do Mar do Norte, tem sido crucial para determinar os preços globais de petróleo. 
                Ao longo das décadas, eventos como guerras, crises econômicas globais e desastres 
                naturais têm desempenhado papéis decisivos em suas variações de preço.

                Além disso, mudanças na demanda global, avanços tecnológicos em energia 
                renovável e decisões políticas sobre produção de petróleo também moldaram seu valor ao 
                longo dos anos. Essas flutuações frequentemente refletem não apenas as dinâmicas do mercado 
                de energia, mas também têm amplo impacto econômico global, afetando desde custos de transporte 
                até políticas fiscais nacionais.
                
                A seguir, serão detalhados 17 desses eventos cruciais, ordenados de forma cronológica:</h1>

                """,unsafe_allow_html=True,
            )
    
    
    # Carregar o arquivo CSV
    file_path = './dataframe/preco_petroleo.csv'
    data = pd.read_csv(file_path, delimiter=';', skiprows=1, header=None)
    data.columns = ['ds', 'y']

    # Converter a coluna 'ds' para datetime
    data['ds'] = pd.to_datetime(data['ds'], format='%d/%m/%Y')

    # Converter a coluna 'y' para float
    data['y'] = data['y'].str.replace(',', '.').astype(float)

    # Eventos relevantes com impacto nos preços do petróleo
    eventos = {
        1987: '1.Crash da Bolsa de Valores de Wall Street',
        1990: '2.Invasão do Kuwait pelo Iraque',
        1997: '3.Crise financeira asiática',
        2001: '4.Ataques de 11 de setembro nos EUA',
        2003: '5.Guerra no Iraque',
        2005: '6.Furacão Katrina nos EUA',
        2006: '7.Crise do Campo Petrolífero de Prudhoe Bay',
        2008: '8.Crise financeira global e bolha imobiliária nos EUA',
        2009: '9.Revolução Verde no Irã', 
        2011: '10.Guerra Civil na Líbia', 
        2012: '11.Sanções Econômicas contra o Irã',
        2014: '12.Excesso de oferta global devido ao boom do shale oil nos EUA', 
        2015: '13.Acordo Nuclear com o Irã', 
        2018: '14.Guerra Comercial EUA-China',
        2019: '15.Ataques às Instalações de Petróleo Sauditas',
        2020: '16.Pandemia de COVID-19', 
        2022: '17.Invasão da Ucrânia pela Rússia e sanções subsequentes',
        
        
    }

    # Criar o gráfico de série temporal
    fig = px.line(data, x='ds', y='y', title='Preço do Petróleo Brent (1987-2024)')

    # Adicionar marcadores coloridos para eventos relevantes
    for idx, (ano, evento) in enumerate(eventos.items(), 1):
        if isinstance(ano, str):
            # Eventos de longo prazo (intervalos de tempo)
            ano_inicio, ano_fim = map(int, ano.split('-'))
            price_range = data[(data['ds'].dt.year >= ano_inicio) & (data['ds'].dt.year <= ano_fim)]['y'].mean()
            trace = go.Scatter(x=[pd.to_datetime(f'{ano_inicio}-01-01'), pd.to_datetime(f'{ano_fim}-12-31')],
                            y=[price_range, price_range], mode='lines', name=evento)
            fig.add_trace(trace)
        else:
            # Eventos específicos (pontos)
            maior_valor_ano = data[data['ds'].dt.year == ano]['y'].idxmax()
            menor_valor_ano = data[data['ds'].dt.year == ano]['y'].idxmin()
            maior_valor = data.loc[maior_valor_ano, 'y']
            menor_valor = data.loc[menor_valor_ano, 'y']
            fig.add_trace(go.Scatter(x=[data.loc[maior_valor_ano, 'ds']],
                                    y=[maior_valor, menor_valor],
                                    mode='markers+text',
                                    name=evento,
                                    marker=dict(color='#8c8787', size=15),
                                    text=f'{idx}',
                                    textposition='top center'))

    # Configurar títulos e legendas
    fig.update_traces(line=dict(color='#FF4B4B'), hovertemplate='Data: %{x|%d-%m-%Y}<br>Preço: %{y}')
    fig.update_layout(xaxis_title='Ano', 
                    yaxis_title='Preço (USD)', 
                    paper_bgcolor='#d2d0d0',
                    showlegend=False
                    
                    )

    st.plotly_chart(fig,use_container_width=True) 


    st.markdown("""
            <h1 style='text-align:justify; 
            font-size:100px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>

            Clique nas caixas expansivas abaixo para ver mais sobre cada um dos 
            eventos numerados no gráfico:</h1>
            

            """,unsafe_allow_html=True)
                    
    
    with st.expander("1 - Crash da Bolsa de Valores de Wall Street (1987)"):

        st.subheader(':red[Crash da Bolsa de Valores de Wall Street (1987)]'
                         , divider='red')
        st.markdown("""
            <div style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>

            O Crash da Bolsa de Valores de Wall Street, ocorrido em 19 de outubro de 1987, 
            conhecido como "Segunda-feira Negra", foi uma queda abrupta e dramática nos mercados de ações dos EUA. 
            O índice Dow Jones Industrial Average despencou <strong style='font-size: 18px'>22,6%</strong> em um único dia, 
            marcando um dos maiores 
            declínios na história financeira global.

            Este evento teve repercussões nos mercados de commodities, incluindo o petróleo Brent. 
            Embora não tenha causado uma queda direta nos preços do Brent, a crise gerou incerteza generalizada 
            nos mercados financeiros, afetando a confiança dos investidores e, consequentemente, a percepção 
            de risco no setor de commodities.

            Em termos de variação percentual, o Crash de 1987 resultou em uma redução dramática nos preços das ações,
            mas o impacto no petróleo Brent foi mais indireto. Os preços não sofreram uma queda direta, 
            pois a influência principal foi a percepção geral de instabilidade econômica global e possíveis impactos 
            na demanda futura por energia.

            Enquanto o Crash de 1987 teve um efeito imediato e severo nos mercados de ações, seu impacto nos 
            preços do petróleo Brent foi mitigado, refletindo mais uma preocupação econômica global do que uma 
            influência direta nos preços do petróleo.</div>
                    
            

            """,unsafe_allow_html=True,
            )
        
        

        # Evento específico de interesse
        evento = {
            'evento': 'Crash da Bolsa de Valores de Wall Street',
            'ano': 1987
        }

        # Filtrar os dados para o ano específico do evento
        data_evento = data[data['ds'].dt.year == evento['ano']]

        # Encontrar a data do Crash da Bolsa de Valores de Wall Street (19 de outubro de 1987)
        data_crash = data_evento[data_evento['ds'].dt.day == 19].iloc[2]

        # Encontrar o menor valor de preço do ano
        menor_valor_ano = data_evento['y'].min()
        data_menor_valor_ano = data_evento[data_evento['y'] == menor_valor_ano].iloc[0]

        # Criar o gráfico de série temporal para o evento específico
        fig = go.Figure()

        # Adicionar linha do preço ao longo do evento
        fig.add_trace(go.Scatter(x=data_evento['ds'], y=data_evento['y'], mode='lines', name='Preço do Petróleo'))

        # Adicionar marcador para o Crash da Bolsa de Valores de Wall Street
        fig.add_trace(go.Scatter(x=[data_crash['ds']], y=[data_crash['y']],
                                mode='markers', name='Crash da Bolsa de Valores de Wall Street',
                                marker=dict(color='#363636', size=15)))

        # Adicionar marcador para o menor valor do ano
        fig.add_trace(go.Scatter(x=[data_menor_valor_ano['ds']], y=[data_menor_valor_ano['y']],
                                mode='markers', name='Menor valor causado pelo evento',
                                marker=dict(color='#800000', size=15)))

        # Configurar título e eixos
        fig.update_traces(line=dict(color='#FF4B4B'), hovertemplate='Data: %{x|%d-%m-%Y}<br>Preço: %{y}')  
        fig.update_layout(title=f'Preço do Petróleo Brent - {evento["evento"]} ({evento["ano"]})',
                        xaxis_title='Data', 
                        yaxis_title='Preço (USD)', 
                        paper_bgcolor='#d2d0d0',
                        xaxis=dict(tickformat='%B-%Y'),
                        legend=dict(orientation="h", yanchor="top", y=1.1, xanchor="center", x=0.5),
                        
                        )

        st.plotly_chart(fig,use_container_width=True)
    


    with st.expander("2 - Invasão do Kuwait pelo Iraque (1990)"):
        st.subheader(':red[Invasão do Kuwait pelo Iraque (1990)]'
                         , divider='red')
        st.markdown("""
            <div style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>
        
            A invasão do Kuwait pelo Iraque em 2 de agosto de 1990 desencadeou a Guerra do Golfo, 
            causando um impacto imediato nos mercados globais de petróleo. Antes do conflito, o petróleo 
            Brent estava estável, mas a invasão e a subsequente ocupação do Kuwait levantaram preocupações 
            sobre a oferta global de petróleo.

            Os preços do petróleo Brent saltaram drasticamente, mais que dobrando em poucos meses, de cerca 
            de <strong style='font-size: 18px'>20\$</strong> por barril antes da invasão para picos acima de 
            <strong style='font-size: 18px'>40$</strong> por barril. Esse aumento refletiu o temor de interrupções 
            significativas na produção 
            de petróleo, dada a importância do Kuwait como produtor global.

            A incerteza sobre a duração do conflito e suas consequências geopolíticas continuou a sustentar 
            os preços elevados por um período prolongado. Este episódio destacou a vulnerabilidade dos mercados 
            de petróleo a eventos geopolíticos no Oriente Médio.

            A invasão do Kuwait pelo Iraque em 1990 resultou em um aumento expressivo e sustentado nos preços 
            do petróleo Brent, devido às preocupações com a oferta global de petróleo e à instabilidade 
            geopolítica na região.</div>
            """, unsafe_allow_html=True,
            )
        

        # Evento específico de interesse
        evento = {
            'evento': 'Invasão do Kuwait pelo Iraque',
            'ano': 1990
        }

        # Filtrar os dados para o ano específico do evento
        data_evento = data[data['ds'].dt.year == evento['ano']]

        # Encontrar a data do Crash da Bolsa de Valores de Wall Street (19 de outubro de 1987)
        data_crash = data_evento[data_evento['ds'].dt.month == 7].iloc[0]

        # Encontrar o menor valor de preço do ano
        maior_valor_ano = data_evento['y'].max()
        data_maior_valor_ano = data_evento[data_evento['y'] == maior_valor_ano].iloc[0]

        # Criar o gráfico de série temporal para o evento específico
        fig = go.Figure()

        # Adicionar linha do preço ao longo do evento
        fig.add_trace(go.Scatter(x=data_evento['ds'], y=data_evento['y'], mode='lines', name='Preço do Petróleo'))

        # Adicionar marcador para o Crash da Bolsa de Valores de Wall Street
        fig.add_trace(go.Scatter(x=[data_crash['ds']], y=[data_crash['y']],
                                mode='markers', name='Invasão do Kuwait pelo Iraque',
                                marker=dict(color='#363636', size=15)))

        # Adicionar marcador para o menor valor do ano
        fig.add_trace(go.Scatter(x=[data_maior_valor_ano['ds']], y=[data_maior_valor_ano['y']],
                                mode='markers', name='Maior valor causado pelo evento',
                                marker=dict(color='#800000', size=15)))

        # Configurar título e eixos
        fig.update_traces(line=dict(color='#FF4B4B'), hovertemplate='Data: %{x|%d-%m-%Y}<br>Preço: %{y}')  
        fig.update_layout(title=f'Preço do Petróleo Brent - {evento["evento"]} ({evento["ano"]})',
                        xaxis_title='Data', 
                        yaxis_title='Preço (USD)', 
                        paper_bgcolor='#d2d0d0',
                        xaxis=dict(tickformat='%B-%Y'),
                        legend=dict(orientation="h", yanchor="top", y=1.1, xanchor="center", x=0.5),
                        
                        )

        st.plotly_chart(fig,use_container_width=True)
    
    with st.expander("3 - Crise financeira asiática (1997)"):
        st.subheader(':red[Crise financeira asiática (1997)]'
                         , divider='red')
        st.markdown("""
            <div style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>

            A Crise Financeira Asiática de 1997 foi uma crise econômica que começou 
            na Tailândia e rapidamente se espalhou para outros países do Sudeste 
            Asiático, afetando severamente suas moedas, mercados de ações e economias 
            como um todo. A crise teve um impacto significativo nos preços do petróleo 
            Brent devido à redução acentuada na demanda por energia na região.

            Os preços do petróleo Brent caíram cerca de <strong style='font-size: 18px'>40%</strong> 
            durante o auge da crise, 
            de meados de 1997 até o final ano. De aproximadamente 
            <strong style='font-size: 18px'>25\$</strong> por 
            barril em janeiro de 1997, os preços despencaram para cerca de 
            <strong style='font-size: 18px'>10\$</strong> 
            por barril em dezembro de 1997. Esta diminuição foi impulsionada pela 
            combinação de excesso de oferta global de petróleo e redução drástica na 
            demanda asiática.

            Além disso, a crise desencadeou uma deflação generalizada nos preços das 
            commodities, incluindo o petróleo Brent, e pressionou os mercados de energia 
            globalmente. A recuperação foi lenta, com a OPEP lutando para ajustar sua 
            produção em resposta à queda na demanda.

            A Crise Financeira Asiática de 1997 resultou em uma queda substancial nos preços 
            do petróleo Brent, refletindo a redução na demanda por energia devido à crise 
            econômica nos países asiáticos afetados.
            </div>

            """,unsafe_allow_html=True,
            )
        
        # Evento específico de interesse
        evento = {
            'evento': 'Crise financeira asiática',
            'ano': 1997
        }

        # Filtrar os dados para o ano específico do evento
        data_evento = data[data['ds'].dt.year == evento['ano']]

        # Encontrar o menor valor de preço do ano
        menor_valor_ano = data_evento['y'].min()
        data_menor_valor_ano = data_evento[data_evento['y'] == menor_valor_ano].iloc[0]

        # Encontrar o maior valor de preço do ano
        maior_valor_ano = data_evento['y'].max()
        data_maior_valor_ano = data_evento[data_evento['y'] == maior_valor_ano].iloc[0]

        # Definir os limites do eixo x com base nas datas filtradas
        xlim_min = data_evento['ds'].min()
        xlim_max = data_evento['ds'].max()

        # Criar o gráfico de série temporal para o evento específico
        fig = go.Figure()

        # Adicionar linha do preço ao longo do evento
        fig.add_trace(go.Scatter(x=data_evento['ds'], y=data_evento['y'], mode='lines', name='Preço do Petróleo'))

        # Adicionar marcador para o menor valor do ano
        fig.add_trace(go.Scatter(x=[data_menor_valor_ano['ds']], y=[data_menor_valor_ano['y']],
                                mode='markers', name='Fim da Crise',
                                marker=dict(color='#363636', size=15)))

        # Adicionar marcador para o maior valor do ano
        fig.add_trace(go.Scatter(x=[data_maior_valor_ano['ds']], y=[data_maior_valor_ano['y']],
                                mode='markers', name='Inicio da Crise',
                                marker=dict(color='#800000', size=15)))

        # Configurar título e eixos
        fig.update_traces(line=dict(color='#FF4B4B'), hovertemplate='Data: %{x|%d-%m-%Y}<br>Preço: %{y}')
        fig.update_layout(title=f'Preço do Petróleo Brent - {evento["evento"]} ({evento["ano"]})',
                        xaxis_title='Data',
                        yaxis_title='Preço (USD)',
                        paper_bgcolor='#d2d0d0',
                        xaxis=dict(range=[xlim_min, xlim_max], tickformat='%B-%Y'),
                        legend=dict(orientation="h", yanchor="top", y=1.1, xanchor="center", x=0.5),
                        )

        st.plotly_chart(fig,use_container_width=True)
        
    with st.expander("4 - Ataques de 11 de setembro nos EUA (2001)"):
        st.subheader(':red[Ataques de 11 de setembro nos EUA (2001)]'
                         , divider='red')
       
        st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>

            Os ataques de 11 de setembro de 2001 nos Estados Unidos, perpetrados pela 
            Al-Qaeda, tiveram um impacto imediato e significativo nos mercados financeiros 
            globais, incluindo o petróleo Brent. Houve uma rápida escalada nos preços do 
            Brent devido ao aumento da incerteza e ao temor de interrupções no fornecimento 
            de petróleo.

            No dia dos ataques e nos dias seguintes, o preço do petróleo Brent caiu 
            cerca de <strong style='font-size: 18px'>3%</strong>, refletindo as preocupações 
            com a segurança global e potenciais 
            repercussões geopolíticas. No entanto, nos meses seguintes, os preços começaram 
            a cair à medida que a desaceleração econômica global e a diminuição na demanda 
            por energia se tornaram evidentes. 

            De setembro a novembro de 2001, os preços do petróleo Brent caíram 
            aproximadamente <strong style='font-size: 18px'>44%</strong>, 
            passando de cerca de <strong style='font-size: 18px'>29\$</strong> por barril em setembro 
            para cerca de <strong style='font-size: 18px'>16\$</strong> por barril em novembro. Esse declínio refletiu a 
            percepção de uma desaceleração econômica global e uma resposta reduzida na 
            demanda por petróleo.

            Os ataques de 11 de setembro de 2001 causaram uma resposta inicial de 
            alta nos preços do petróleo Brent, mas a subsequente desaceleração econômica 
            global resultou em uma diminuição significativa na demanda e, consequentemente, 
            na queda dos preços do petróleo.
            </h1>

            """,unsafe_allow_html=True,
            )
        

        # Evento específico de interesse
        evento = {
            'evento': 'Ataques de 11 de setembro nos EUA',
            'ano': 2001
        }

        # Filtrar os dados para o ano específico do evento
        data_evento = data[data['ds'].dt.year == evento['ano']]

        # Encontrar a data do menor valor de preço do ano
        menor_valor_ano = data_evento['y'].min()
        data_menor_valor_ano = data_evento[data_evento['y'] == menor_valor_ano].iloc[0]

        # Encontrar a data do dia 11 de setembro
        data_11_setembro = data_evento[(data_evento['ds'].dt.month == 9) & (data_evento['ds'].dt.day == 11)]

        # Verificar se a data do dia 11 de setembro está presente
        if not data_11_setembro.empty:
            data_11_setembro = data_11_setembro.iloc[0]
        else:
            data_11_setembro = None

        # Criar o gráfico de série temporal para o evento específico
        fig = go.Figure()

        # Adicionar linha do preço ao longo do evento
        fig.add_trace(go.Scatter(x=data_evento['ds'], y=data_evento['y'], mode='lines', name='Preço do Petróleo'))

        # Adicionar marcador para o dia 11 de setembro, se disponível
        if data_11_setembro is not None:
            fig.add_trace(go.Scatter(x=[data_11_setembro['ds']], y=[data_11_setembro['y']],
                                    mode='markers', name='11 de Setembro',
                                    marker=dict(color='#363636', size=15)))

        # Adicionar marcador para o menor valor do ano
        fig.add_trace(go.Scatter(x=[data_menor_valor_ano['ds']], y=[data_menor_valor_ano['y']],
                                mode='markers', name='Menor valor do ano',
                                marker=dict(color='#800000', size=15)))

        # Configurar título e eixos
        fig.update_traces(line=dict(color='#FF4B4B'), hovertemplate='Data: %{x|%d-%m-%Y}<br>Preço: %{y}')  
        fig.update_layout(title=f'Preço do Petróleo Brent - {evento["evento"]} ({evento["ano"]})',
                        xaxis_title='Data', 
                        yaxis_title='Preço (USD)', 
                        paper_bgcolor='#d2d0d0',
                        xaxis=dict(tickformat='%B-%Y'),
                        legend=dict(orientation="h", yanchor="top", y=1.1, xanchor="center", x=0.5),
                        )

        st.plotly_chart(fig,use_container_width=True)
        
    with st.expander("5 - Guerra no Iraque (2003)"):
        st.subheader(':red[Guerra no Iraque (2003)]'
                         , divider='red')
                
        

        # Evento específico de interesse
        evento = {
            'evento': 'Guerra no Iraque',
            'ano': 2003
        }

        # Filtrar os dados para o ano específico do evento
        data_evento = data[data['ds'].dt.year == evento['ano']]

        # Encontrar o menor valor de preço em maio de 2003
        menor_valor_maio = data_evento[data_evento['ds'].dt.month == 5]['y'].min()
        data_menor_valor_maio = data_evento[(data_evento['ds'].dt.month == 5) & (data_evento['y'] == menor_valor_maio)]

        # Criar o gráfico de série temporal para o evento específico
        fig = go.Figure()

        # Adicionar linha do preço ao longo do evento
        fig.add_trace(go.Scatter(x=data_evento['ds'], y=data_evento['y'], mode='lines', name='Preço do Petróleo'))

        # Adicionar marcador para o evento em 1º de março
        primeiro_de_marco = data_evento[data_evento['ds'].dt.month == 3].iloc[0]
        fig.add_trace(go.Scatter(x=[primeiro_de_marco['ds']], y=[primeiro_de_marco['y']],
                                mode='markers', name=f'Inicio da guerra',
                                marker=dict(color='#363636', size=15)))

        # Adicionar marcador para o menor valor de maio
        fig.add_trace(go.Scatter(x=[data_menor_valor_maio['ds'].iloc[0]], y=[data_menor_valor_maio['y'].iloc[0]],
                                mode='markers', name=f'Queda mais acentuada do período',
                                marker=dict(color='#800000', size=15)))

        # Configurar título e eixos
        

        fig.update_traces(line=dict(color='#FF4B4B'), hovertemplate='Data: %{x|%d-%m-%Y}<br>Preço: %{y}')  
        fig.update_layout(title=f'Preço do Petróleo Brent - {evento["evento"]} ({evento["ano"]})',
                        xaxis_title='Data', 
                        yaxis_title='Preço (USD)', 
                        paper_bgcolor='#d2d0d0',
                        xaxis=dict(tickformat='%B-%Y'),
                        legend=dict(orientation="h", yanchor="top", y=1.1, xanchor="center", x=0.5),
                        
                        )
        
        st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>

            A Guerra no Iraque de 2003 teve um impacto considerável nos preços do 
            petróleo Brent devido às preocupações com a segurança do fornecimento de 
            petróleo no Golfo Pérsico, uma região chave de produção de petróleo global.
            Antes da guerra, os preços já estavam subindo devido às tensões geopolíticas
            crescentes.

            No mês anterior à invasão, o preço do petróleo Brent variava entre 30 e <strong style='font-size: 18px'>33\$</strong> 
            por barril. Durante a guerra, esses preços subiram para cerca ate <strong style='font-size: 18px'>35\$</strong> por barril 
            devido às preocupações com a segurança do fornecimento no Golfo Pérsico, 
            uma região crucial para a produção global de petróleo.
                    
            Após a queda do regime de Saddam Hussein em abril de 2003 e o término das 
            principais operações militares, os preços começaram a se estabilizar e, 
            posteriormente, a cair registrando a queda  de <strong style='font-size: 18px'>34%</strong> 
            em comparação ao período do inicio da invasão.
            
            No ano seguinte à guerra, os preços do petróleo Brent 
            estavam novamente registrou uma media de <strong style='font-size: 18px'>38\$</strong> por barril, à medida que o mercado 
            global absorvia a normalização da produção e as condições geopolíticas.

            A Guerra no Iraque de 2003 resultou em um aumento temporário nos preços do 
            petróleo Brent devido às preocupações com o fornecimento, seguido por uma 
            estabilização e subsequente queda à medida que as condições de mercado se 
            ajustavam à nova realidade geopolítica da região.
            """,unsafe_allow_html=True,
            )
        
        st.plotly_chart(fig,use_container_width=True)
        
    with st.expander("6 - Furacão Katrina nos EUA (2005)"):
        st.subheader(':red[Furacão Katrina nos EUA (2005)]'
                         , divider='red')
        st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>

            O Furacão Katrina, que atingiu os Estados Unidos em 29 agosto de 2005, teve um impacto significativo 
            nos preços do petróleo Brent devido à interrupção das operações de produção e refino de petróleo na 
            região do Golfo do México, uma área crucial de produção de petróleo nos EUA.

            Durante e imediatamente após o furacão, os preços do petróleo Brent caíram devido às preocupações 
            com a interrupção do fornecimento de petróleo. A região do Golfo do México é responsável por uma parte 
            substancial da produção de petróleo dos EUA, e o fechamento temporário de plataformas de produção e 
            refinarias resultou em uma redução na oferta global de petróleo.

            Os preços do petróleo Brent caíram cerca de <strong style='font-size: 18px'>6%</strong> nos 
            10 dias seguintes ao furacão, passando de 
            aproximadamente <strong style='font-size: 18px'>65\$</strong> por barril antes do furacão para cerca de <strong style='font-size: 18px'>62\$</strong> por barril logo após o evento. 
            Esse queda refletiu as preocupações com os danos às infraestruturas de produção, refino e transporte de petróleo.

            O Furacão Katrina em 2005 resultou em um queda significativo nos preços do petróleo Brent devido 
            às interrupções na produção e refino de petróleo na região do Golfo do México, destacando a vulnerabilidade 
            do mercado de energia a desastres naturais de grande escala.</h1>

            """,unsafe_allow_html=True,
            )
        

        # Evento específico de interesse
        evento = {
            'evento': 'Furacão Katrina nos EUA',
            'ano': 2005
        }

        # Filtrar os dados para o ano específico do evento
        data_evento = data[data['ds'].dt.year == evento['ano']]

        # Encontrar a data do menor valor de setembro
        data_setembro = data_evento[data_evento['ds'].dt.month == 9]
        menor_valor_setembro = data_setembro['y'].min()
        data_menor_valor_setembro = data_setembro[data_setembro['y'] == menor_valor_setembro].iloc[0]

        # Encontrar a data do dia 29 de agosto
        data_furacao = data_evento[(data_evento['ds'].dt.month == 8) & (data_evento['ds'].dt.day == 29)].iloc[0]

        # Criar o gráfico de série temporal para o evento específico
        fig = go.Figure()

        # Adicionar linha do preço ao longo do evento
        fig.add_trace(go.Scatter(x=data_evento['ds'], y=data_evento['y'], mode='lines', name='Preço do Petróleo'))

        # Adicionar marcador para o dia 29 de agosto
        fig.add_trace(go.Scatter(x=[data_furacao['ds']], y=[data_furacao['y']],
                                mode='markers', name='Preço no Inicio do Furacão Katrina',
                                marker=dict(color='#363636', size=15)))

        # Adicionar marcador para o menor valor de setembro
        fig.add_trace(go.Scatter(x=[data_menor_valor_setembro['ds']], y=[data_menor_valor_setembro['y']],
                                mode='markers', name='Menor valor durante Evento',
                                marker=dict(color='#800000', size=15)))

        # Configurar título e eixos
        fig.update_traces(line=dict(color='#FF4B4B'), hovertemplate='Data: %{x|%d-%m-%Y}<br>Preço: %{y}')  
        fig.update_layout(title=f'Preço do Petróleo Brent - {evento["evento"]} ({evento["ano"]})',
                        xaxis_title='Data', 
                        yaxis_title='Preço (USD)', 
                        paper_bgcolor='#d2d0d0',
                        xaxis=dict(tickformat='%B-%Y'),
                        legend=dict(orientation="h", yanchor="top", y=1.1, xanchor="center", x=0.5),
                        )

        st.plotly_chart(fig,use_container_width=True)
        
    with st.expander("7 - Crise do Campo Petrolífero de Prudhoe Bay (2006)"):
        st.subheader(':red[Crise do Campo Petrolífero de Prudhoe Bay (2006)]'
                         , divider='red')
        st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>

            A Crise do Campo Petrolífero de Prudhoe Bay em 2006 foi desencadeada pela descoberta de corrosão severa 
            nos oleodutos do maior campo petrolífero dos Estados Unidos, localizado no Alasca. A BP, operadora do campo, 
            foi forçada a fechar temporariamente uma parte significativa da produção, reduzindo a oferta global de petróleo.

            Os preços do petróleo Brent subiram cerca de <strong style='font-size: 18px'>15%</strong> 
            imediatamente após o anúncio do fechamento parcial, 
            refletindo as preocupações com a redução na produção. No entanto, ao fim da crise os preços retornaram
            a cair registrando minima de <strong style='font-size: 18px'>57\$</strong>.
                    
            A Crise do Campo Petrolífero de Prudhoe Bay em 2006 resultou em um aumento temporário nos preços do petróleo 
            Brent, refletindo as preocupações com a redução na produção de petróleo devido à descoberta de corrosão 
            nos oleodutos do campo petrolífero no Alasca.</h1>

            """,unsafe_allow_html=True,
            )
        

        

        # Evento específico de interesse
        evento = {
            'evento': 'Crise do Campo Petrolífero de Prudhoe Bay 2006',
            'ano': 2006
        }

        # Filtrar os dados para o ano específico do evento
        data_evento = data[data['ds'].dt.year == evento['ano']]

        # Encontrar a data do menor valor entre março e setembro
        data_marco_setembro = data_evento[(data_evento['ds'].dt.month >= 3) & (data_evento['ds'].dt.month <= 9)]
        menor_valor_marco_setembro = data_marco_setembro['y'].min()
        data_menor_valor_marco_setembro = data_marco_setembro[data_marco_setembro['y'] == menor_valor_marco_setembro].iloc[0]

        # Encontrar a data de 6 de março
        data_6_marco = data_evento[(data_evento['ds'].dt.month == 3) & (data_evento['ds'].dt.day == 6)].iloc[0]

        # Criar o gráfico de série temporal para o evento específico
        fig = go.Figure()

        # Adicionar linha do preço ao longo do evento
        fig.add_trace(go.Scatter(x=data_evento['ds'], y=data_evento['y'], mode='lines', name='Preço do Petróleo'))

        # Adicionar marcador para 6 de março
        fig.add_trace(go.Scatter(x=[data_6_marco['ds']], y=[data_6_marco['y']],
                                mode='markers', name='Preço em 6 de Março',
                                marker=dict(color='#363636', size=15)))

        # Adicionar marcador para o menor valor de março a setembro
        fig.add_trace(go.Scatter(x=[data_menor_valor_marco_setembro['ds']], y=[data_menor_valor_marco_setembro['y']],
                                mode='markers', name='Menor valor durante o evento (Março-Setembro)',
                                marker=dict(color='#800000', size=15)))

        # Configurar título e eixos
        fig.update_traces(line=dict(color='#FF4B4B'), hovertemplate='Data: %{x|%d-%m-%Y}<br>Preço: %{y}')  
        fig.update_layout(title=f'Preço do Petróleo Brent - {evento["evento"]} ({evento["ano"]})',
                        xaxis_title='Data', 
                        yaxis_title='Preço (USD)', 
                        paper_bgcolor='#d2d0d0',
                        xaxis=dict(tickformat='%B-%Y'),
                        legend=dict(orientation="h", yanchor="top", y=1.1, xanchor="center", x=0.5),
                        )

        st.plotly_chart(fig,use_container_width=True)
        
    with st.expander("8 - Crise financeira global e bolha imobiliária nos EUA (2008)"):
        st.subheader(':red[Crise financeira global e bolha imobiliária nos EUA (2008)]'
                         , divider='red')
        st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>

            A Crise Financeira Global de 2008, desencadeada pela crise das hipotecas subprime nos Estados Unidos, 
            teve um impacto profundo nos mercados financeiros globais, incluindo o mercado de petróleo Brent. 
            O colapso de grandes instituições financeiras e a subsequente recessão global afetaram a demanda por 
            energia de maneira significativa.

            Antes da crise financeira, os preços do petróleo Brent estavam atingindo picos históricos, 
            com valores superiores a <strong style='font-size: 18px'>140\$</strong> por barril no inicio de julho de 2008. No entanto, à medida que a crise 
            financeira se intensificava e a demanda global por energia diminuía, os preços do petróleo Brent 
            despencaram rapidamente.

            Entre meados de 2008 e o final do ano, os preços do petróleo Brent caíram mais de <strong style='font-size: 18px'>77%</strong>, atingindo 
            mínimas abaixo de <strong style='font-size: 18px'>33\$</strong> por barril no final de 2008. Esse declínio acentuado refletiu uma 
            combinação de excesso de oferta global de petróleo e uma queda dramática na demanda por energia 
            devido à recessão econômica global.

            A Crise Financeira Global de 2008 resultou em uma queda dramática nos preços do 
            petróleo Brent, refletindo a desaceleração econômica global e a redução significativa na demanda 
            por energia em todo o mundo.

            Esses eventos históricos destacam a complexa interação entre fatores geopolíticos, econômicos 
            e ambientais que influenciam os preços do petróleo Brent, moldando o comportamento do mercado 
            global de energia ao longo das décadas.</h1>

            """,unsafe_allow_html=True,
            )
       
        

        # Filtrar os dados para os anos de 2008 e 2009
        data_2008_2009 = data[(data['ds'].dt.year >= 2008) & (data['ds'].dt.year <= 2009)]

        # Encontrar a data do menor valor durante esses dois anos
        menor_valor_2008_2009 = data_2008_2009['y'].min()
        data_menor_valor_2008_2009 = data_2008_2009[data_2008_2009['y'] == menor_valor_2008_2009].iloc[0]

        # Encontrar a data do primeiro dia de julho de 2008
        data_primeiro_julho_2008 = data_2008_2009[(data_2008_2009['ds'].dt.year == 2008) & (data_2008_2009['ds'].dt.month == 7)].iloc[0]

        # Criar o gráfico de série temporal
        fig = go.Figure()

        # Adicionar linha do preço ao longo dos anos de 2008 e 2009
        fig.add_trace(go.Scatter(x=data_2008_2009['ds'], y=data_2008_2009['y'], mode='lines', name='Preço do Petróleo'))

        # Adicionar marcador para o primeiro dia de julho de 2008
        fig.add_trace(go.Scatter(x=[data_primeiro_julho_2008['ds']], y=[data_primeiro_julho_2008['y']],
                                mode='markers', name='Início da Crise em Julho de 2008',
                                marker=dict(color='#363636', size=15)))

        # Adicionar marcador para o menor valor encontrado em 2008 e 2009
        fig.add_trace(go.Scatter(x=[data_menor_valor_2008_2009['ds']], y=[data_menor_valor_2008_2009['y']],
                                mode='markers', name='Menor Valor durante a Crise',
                                marker=dict(color='#800000', size=15)))

        # Configurar título e eixos
        fig.update_traces(line=dict(color='#FF4B4B'), hovertemplate='Data: %{x|%d-%m-%Y}<br>Preço: %{y}')  
        fig.update_layout(title='Preço do Petróleo Brent - Crise Financeira Global e Bolha Imobiliária nos EUA (2008-2009)',
                        xaxis_title='Data', 
                        yaxis_title='Preço (USD)', 
                        paper_bgcolor='#d2d0d0',
                        xaxis=dict(tickformat='%B-%Y'),
                        legend=dict(orientation="h", yanchor="top", y=1.1, xanchor="center", x=0.5),
                        )

        st.plotly_chart(fig,use_container_width=True)

        
    with st.expander("9 - Revolução Verde no Irã (2009)"):
        st.subheader(':red[Revolução Verde no Irã (2009)]'
                         , divider='red')
        st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>

            A Revolução Verde no Irã em 12 de junho 2009 foi uma série de protestos contra os resultados controversos 
            das eleições presidenciais no país. Embora não tenha impactado diretamente a produção de petróleo, 
            a instabilidade política e social no Irã, um importante produtor de petróleo, gerou preocupações 
            sobre a segurança do fornecimento global de petróleo.

            Os preços do petróleo Brent caíram cerca de <strong style='font-size: 18px'>14%</strong> durante o auge dos protestos, 
            refletindo as 
            preocupações com a potencial instabilidade política e sua influência nas exportações de petróleo do Irã.
            No entanto, os preços se estabilizaram à medida que os protestos diminuíram e a situação política 
            interna no Irã se acalmou. O movimento foi mais intenso durante os meses seguintes às eleições, 
            com os maiores protestos ocorrendo até o final de 2009, porem o valor do prefolio brent recuperou
            com um pico de aproximadamente <strong style='font-size: 18px'>78\$</strong> em outubro.

            A Revolução Verde no Irã em 2009 resultou em uma queda temporário nos preços do petróleo Brent, 
            refletindo as preocupações com a estabilidade política e suas possíveis repercussões nas exportações 
            de petróleo do Irã.</h1>

            """,unsafe_allow_html=True,
            )
        

        # Evento específico de interesse
        evento = {
            'evento': 'Revolução Verde no Irã',
            'ano': 2009
        }

        # Filtrar os dados para o ano específico do evento
        data_evento = data[data['ds'].dt.year == evento['ano']]

        # Encontrar a data do maior valor entre junho e agosto
        data_junho_agosto = data_evento[(data_evento['ds'].dt.month >= 6) & (data_evento['ds'].dt.month <= 10)]
        maior_valor_junho_agosto = data_junho_agosto['y'].max()
        data_maior_valor_junho_agosto = data_junho_agosto[data_junho_agosto['y'] == maior_valor_junho_agosto].iloc[0]

        # Encontrar a data do primeiro dia de junho
        data_primeiro_junho = data_evento[(data_evento['ds'].dt.month == 6) & (data_evento['ds'].dt.day == 1)].iloc[0]

        # Encontrar a data de 12 de junho de 2009
        data_12_junho = data_evento[(data_evento['ds'].dt.month == 6) & (data_evento['ds'].dt.day == 12)].iloc[0]

        # Encontrar o menor valor de julho de 2009
        data_julho = data_evento[(data_evento['ds'].dt.month == 7)]
        menor_valor_julho = data_julho['y'].min()
        data_menor_valor_julho = data_julho[data_julho['y'] == menor_valor_julho].iloc[0]

        # Criar o gráfico de série temporal para o evento específico
        fig = go.Figure()

        # Adicionar linha do preço ao longo do evento
        fig.add_trace(go.Scatter(x=data_evento['ds'], y=data_evento['y'], mode='lines', name='Preço do Petróleo'))

        # Adicionar marcador para o dia 12 de junho de 2009
        fig.add_trace(go.Scatter(x=[data_12_junho['ds']], y=[data_12_junho['y']],
                                mode='markers', name='12 de Junho de 2009',
                                marker=dict(color='#363636', size=15)))

        # Adicionar marcador para o menor valor de julho
        fig.add_trace(go.Scatter(x=[data_menor_valor_julho['ds']], y=[data_menor_valor_julho['y']],
                                mode='markers', name='Pico de queda em Julho',
                                marker=dict(color='#000080', size=15)))

        # Adicionar marcador para o maior valor entre junho e agosto
        fig.add_trace(go.Scatter(x=[data_maior_valor_junho_agosto['ds']], y=[data_maior_valor_junho_agosto['y']],
                                mode='markers', name='Maior valor durante evento',
                                marker=dict(color='#800000', size=15)))

        # Configurar título e eixos
        fig.update_traces(line=dict(color='#FF4B4B'), hovertemplate='Data: %{x|%d-%m-%Y}<br>Preço: %{y}')  
        fig.update_layout(title=f'Preço do Petróleo Brent - {evento["evento"]} ({evento["ano"]})',
                        xaxis_title='Data', 
                        yaxis_title='Preço (USD)', 
                        paper_bgcolor='#d2d0d0',
                        xaxis=dict(tickformat='%B-%Y'),
                        legend=dict(orientation="h", yanchor="top", y=1.1, xanchor="center", x=0.5),
                        )

        st.plotly_chart(fig,use_container_width=True)

        
    with st.expander("10 - Guerra Civil na Líbia (2011)"):
        st.subheader(':red[Guerra Civil na Líbia (2011)]'
                         , divider='red')
        st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>

            A Guerra Civil na Líbia em 2011 teve um impacto significativo nos preços do petróleo Brent 
            devido à interrupção na produção de petróleo em um dos maiores produtores da África. Os combates 
            e as sanções internacionais levaram à redução drástica na produção de petróleo, afetando a oferta 
            global.

            Os preços do petróleo Brent subiram cerca de <strong style='font-size: 18px'>14%</strong> nos 
            dois primeiros meses da guerra, 
            passando de cerca de <strong style='font-size: 18px'>97\$</strong> por barril para cerca de <strong style='font-size: 18px'>112\$</strong> por barril.
            Esse aumento refletiu as preocupações com a segurança do fornecimento de petróleo e as 
            interrupções na produção devido ao conflito armado na Líbia.

            A Guerra Civil na Líbia em 2011 resultou em um aumento significativo nos preços do petróleo Brent, 
            refletindo as preocupações com a interrupção na produção de petróleo devido ao conflito armado e às 
            sanções internacionais contra o país.</h1>

            """,unsafe_allow_html=True,
            )
        
        

        # Evento específico de interesse
        evento = {
            'evento': 'Guerra Civil na Líbia',
            'ano': 2011
        }

        # Filtrar os dados para o ano específico do evento
        data_evento = data[data['ds'].dt.year == evento['ano']]

        # Encontrar a data do primeiro dia de fevereiro
        data_primeiro_fevereiro = data_evento[(data_evento['ds'].dt.month == 2) & (data_evento['ds'].dt.day == 1)].iloc[0]

        # Encontrar a data do maior valor entre fevereiro e outubro
        data_fevereiro_outubro = data_evento[(data_evento['ds'].dt.month >= 2) & (data_evento['ds'].dt.month <= 10)]
        maior_valor_fevereiro_outubro = data_fevereiro_outubro['y'].max()
        data_maior_valor_fevereiro_outubro = data_fevereiro_outubro[data_fevereiro_outubro['y'] == maior_valor_fevereiro_outubro].iloc[0]

        # Encontrar a data do dia 1 de março
        data_primeiro_marco = data_evento[(data_evento['ds'].dt.month == 3) & (data_evento['ds'].dt.day == 1)].iloc[0]

        # Criar o gráfico de série temporal para o evento específico
        fig = go.Figure()

        # Adicionar linha do preço ao longo do evento
        fig.add_trace(go.Scatter(x=data_evento['ds'], y=data_evento['y'], mode='lines', name='Preço do Petróleo'))

        # Adicionar marcador para o primeiro dia de fevereiro
        fig.add_trace(go.Scatter(x=[data_primeiro_fevereiro['ds']], y=[data_primeiro_fevereiro['y']],
                                mode='markers', name='Início de Guerra Civil na Líbia',
                                marker=dict(color='#363636', size=15)))

        # Adicionar marcador para o maior valor entre fevereiro e outubro
        fig.add_trace(go.Scatter(x=[data_maior_valor_fevereiro_outubro['ds']], y=[data_maior_valor_fevereiro_outubro['y']],
                                mode='markers', name='Maior valor durante Evento',
                                marker=dict(color='#800000', size=15)))

        # Adicionar marcador para o dia 1 de março
        fig.add_trace(go.Scatter(x=[data_primeiro_marco['ds']], y=[data_primeiro_marco['y']],
                                mode='markers', name='2 meses apos inicio da guerra',
                                marker=dict(color='#000080', size=15)))

        # Configurar título e eixos
        fig.update_traces(line=dict(color='#FF4B4B'), hovertemplate='Data: %{x|%d-%m-%Y}<br>Preço: %{y}')  
        fig.update_layout(title=f'Preço do Petróleo Brent - {evento["evento"]} ({evento["ano"]})',
                        xaxis_title='Data', 
                        yaxis_title='Preço (USD)', 
                        paper_bgcolor='#d2d0d0',
                        xaxis=dict(tickformat='%B-%Y'),
                        legend=dict(orientation="h", yanchor="top", y=1.15, xanchor="center", x=0.5),
                        )

        st.plotly_chart(fig,use_container_width=True)

   
    with st.expander("11 - Sanções Econômicas contra o Irã (2012)"):
        st.subheader(':red[Sanções Econômicas contra o Irã (2012)]'
                         , divider='red')
        st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>

            A imposição de sanções econômicas contra o Irã em 2012 teve um impacto direto nos preços do 
            petróleo Brent devido à redução nas exportações de petróleo do país. As sanções visavam o programa 
            nuclear iraniano e restringiam severamente as transações financeiras e comerciais com o Irã.

            Os preços do petróleo Brent subiram cerca de <strong style='font-size: 18px'>10%</strong> 
            após a imposição das sanções, refletindo as preocupações 
            com a diminuição da oferta global de petróleo devido à redução nas exportações iranianas. 
            A incerteza sobre a resposta geopolítica e as implicações das sanções também contribuíram para o 
            aumento dos preços. Porem registrou maior declínio em julho descendo a aproximadamente <strong style='font-size: 18px'>88\$</strong>.

            As sanções econômicas contra o Irã em 2012 resultaram em um aumento nos preços do petróleo Brent, 
            refletindo as preocupações com a redução na oferta global de petróleo devido às restrições nas 
            exportações iranianas.</h1>

            """,unsafe_allow_html=True,
            )
        

        # Evento específico de interesse
        evento = {
            'evento': 'Sanções Econômicas contra o Irã',
            'ano': 2012
        }

        # Filtrar os dados para o ano específico do evento
        data_evento = data[data['ds'].dt.year == evento['ano']]

        # Encontrar a data do maior valor em janeiro
        data_maior_janeiro = data_evento[data_evento['ds'].dt.month == 1].nlargest(1, 'y')

        # Encontrar a data do menor valor do ano
        data_menor_ano = data_evento.nsmallest(1, 'y')

        # Definir os limites do eixo x com base nas datas filtradas
        xlim_min = data_evento['ds'].min()
        xlim_max = data_evento['ds'].max()


        # Criar o gráfico de série temporal para o evento específico
        fig = go.Figure()

        # Adicionar linha do preço ao longo do evento
        fig.add_trace(go.Scatter(x=data_evento['ds'], y=data_evento['y'], mode='lines', name='Preço do Petróleo'))

        # Adicionar marcador para o maior valor de janeiro
        fig.add_trace(go.Scatter(x=data_maior_janeiro['ds'], y=data_maior_janeiro['y'],
                                mode='markers', name='Inicio das sanções econômicas',
                                marker=dict(color='#363636', size=15)))

        # Adicionar marcador para o menor valor do ano
        fig.add_trace(go.Scatter(x=data_menor_ano['ds'], y=data_menor_ano['y'],
                                mode='markers', name='Maior queda durante Evento',
                                marker=dict(color='#800000', size=15)))



        # Configurar título e eixos
        fig.update_traces(line=dict(color='#FF4B4B'), hovertemplate='Data: %{x|%d-%m-%Y}<br>Preço: %{y}')
        fig.update_layout(title=f'Preço do Petróleo Brent - {evento["evento"]} ({evento["ano"]})',
                        xaxis_title='Data',
                        yaxis_title='Preço (USD)',
                        paper_bgcolor='#d2d0d0',
                        xaxis=dict(range=[xlim_min, xlim_max], tickformat='%B-%Y'),
                        legend=dict(orientation="h", yanchor="top", y=1.1, xanchor="center", x=0.5),
                        )
        st.plotly_chart(fig,use_container_width=True)

    
    with st.expander("12 - Excesso de oferta global devido ao boom do shale oil nos EUA (2014)"):
        st.subheader(':red[Excesso de oferta global devido ao boom do shale oil nos EUA (2014)]'
                         , divider='red')
        st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>

            O boom do shale oil nos Estados Unidos a partir de 2014 contribuiu para um excesso de oferta 
            global de petróleo, pressionando para baixo os preços do petróleo Brent. A tecnologia de extração 
            de petróleo de xisto permitiu aos EUA aumentar significativamente sua produção, alterando o 
            equilíbrio de poder no mercado de energia global.

            Os preços do petróleo Brent caíram mais de <strong style='font-size: 18px'>50%</strong> entre meados de 2014, passando 
            de cerca de <strong style='font-size: 18px'>115\$</strong> por barril para aproximadamente <strong style='font-size: 18px'>55\$</strong> ate o fim do ano do de 2014. 
            Esse declínio refletiu a rápida expansão da produção de petróleo de xisto nos EUA e a resposta 
            da OPEP para manter sua participação de mercado.

            O excesso de oferta global devido ao boom do shale oil nos EUA a partir de 2014 resultou em uma 
            queda dramática nos preços do petróleo Brent, refletindo a mudança na dinâmica de oferta e demanda 
            no mercado global de energia. </h1>

            """,unsafe_allow_html=True,
            )
        
        

        # Evento específico de interesse
        evento = {
            'evento': 'Excesso de oferta global devido ao boom do shale oil nos EUA',
            'ano': 2014
        }

        # Filtrar os dados para o ano de 2014
        data_evento = data[data['ds'].dt.year == 2014]

        # Encontrar a data do maior valor em 2014
        data_maior_2014 = data_evento.nlargest(1, 'y')

        # Encontrar a data do menor valor em 2014
        data_menor_2014 = data_evento.nsmallest(1, 'y')

        # Definir os limites do eixo x com base nas datas filtradas
        xlim_min = data_evento['ds'].min()
        xlim_max = data_evento['ds'].max()

        # Criar o gráfico de série temporal para o evento específico
        fig = go.Figure()

        # Adicionar linha do preço ao longo do evento
        fig.add_trace(go.Scatter(x=data_evento['ds'], y=data_evento['y'], mode='lines', name='Preço do Petróleo'))

        # Adicionar marcador para o maior valor em 2014
        fig.add_trace(go.Scatter(x=data_maior_2014['ds'], y=data_maior_2014['y'],
                                mode='markers', name='Inicio do Evento',
                                marker=dict(color='#363636', size=15)))

        # Adicionar marcador para o menor valor em 2014
        fig.add_trace(go.Scatter(x=data_menor_2014['ds'], y=data_menor_2014['y'],
                                mode='markers', name='Maior queda durante Evento',
                                marker=dict(color='#800000', size=15)))

        # Configurar título e eixos
        fig.update_traces(line=dict(color='#FF4B4B'), hovertemplate='Data: %{x|%d-%m-%Y}<br>Preço: %{y}')
        fig.update_layout(title=f'Preço do Petróleo Brent - {evento["evento"]} (2014)',
                        xaxis_title='Data',
                        yaxis_title='Preço (USD)',
                        paper_bgcolor='#d2d0d0',
                        xaxis=dict(range=[xlim_min, xlim_max], tickformat='%d-%m-%Y'),
                        legend=dict(orientation="h", yanchor="top", y=1.1, xanchor="center", x=0.5),
                        )

        st.plotly_chart(fig,use_container_width=True)
    
    with st.expander("13 - Acordo Nuclear com o Irã (2015)"):
        st.subheader(':red[Acordo Nuclear com o Irã (2015)]'
                         , divider='red')
        st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>

            A assinatura do Acordo Nuclear com o Irã 14 de julho em 2015 levou à suspensão das sanções econômicas 
            contra o país, permitindo um aumento nas exportações de petróleo iranianas. 
            Isso teve um impacto imediato nos preços do petróleo Brent, que caíram devido ao aumento na oferta 
            global de petróleo.

            Os preços do petróleo Brent caíram cerca de <strong style='font-size: 18px'>24%</strong> após o anúncio do acordo, passando de cerca de <strong style='font-size: 18px'>58\$</strong> 
            por barril para cerca de <strong style='font-size: 18px'>48\$</strong> por barril. Essa queda refletiu as expectativas de aumento na 
            produção e exportação de petróleo do Irã, após a suspensão das sanções. O preco do petroleo brent continuou
            a cair ate acordo entrar em vigor em 16 de janeiro, apos cumprimentos das condições estabelecidas. 
            Nesse período o preco continuava a cair e registrou minima de aproximadamente <strong style='font-size: 18px'>26\$</strong> no periodo.
                    

            O Acordo Nuclear com o Irã em 2015 resultou em uma queda nos preços do petróleo Brent, refletindo as 
            expectativas de aumento na oferta global de petróleo devido à retomada das exportações iranianas 
            após a suspensão das sanções econômicas.</h1>

            """,unsafe_allow_html=True,
            )
        

        

        # Evento específico de interesse
        evento = {
            'evento': 'Acordo Nuclear com o Irã',
            'ano': 2015
        }

        # Filtrar os dados para o período específico do evento
        data_evento = data[(data['ds'] >= '2015-01-01') & (data['ds'] <= '2016-02-29')]

        # Encontrar a data do maior valor em julho
        data_maior_julho = data_evento[(data_evento['ds'].dt.month == 7) & (data_evento['ds'].dt.day == 14)].nsmallest(1, 'y')
        data_menor_ano = data_evento.nsmallest(1, 'y')

        # Definir os limites do eixo x com base nas datas filtradas
        xlim_min = data_evento['ds'].min()
        xlim_max = data_evento['ds'].max()

        # Criar o gráfico de série temporal para o evento específico
        fig = go.Figure()

        # Adicionar linha do preço ao longo do evento
        fig.add_trace(go.Scatter(x=data_evento['ds'], y=data_evento['y'], mode='lines', name='Preço do Petróleo'))

        # Adicionar marcador para o início do evento (14 de julho)
        fig.add_trace(go.Scatter(x=data_maior_julho['ds'], y=data_maior_julho['y'],
                                mode='markers', name='Assinatura do Acordo',
                                marker=dict(color='#363636', size=15)))

        # Adicionar marcador para o menor valor do ano durante o evento
        fig.add_trace(go.Scatter(x=data_menor_ano['ds'], y=data_menor_ano['y'],
                                mode='markers', name='Menor valor durante Evento',
                                marker=dict(color='#800000', size=15)))

        # Configurar título e eixos
        fig.update_traces(line=dict(color='#FF4B4B'), hovertemplate='Data: %{x|%d-%m-%Y}<br>Preço: %{y}')
        fig.update_layout(title=f'Preço do Petróleo Brent - {evento["evento"]} ({evento["ano"]})',
                        xaxis_title='Data',
                        yaxis_title='Preço (USD)',
                        paper_bgcolor='#d2d0d0',
                        xaxis=dict(range=[xlim_min, xlim_max], tickformat='%B-%Y'),
                        legend=dict(orientation="h", yanchor="top", y=1.1, xanchor="center", x=0.5),
                        )

        st.plotly_chart(fig,use_container_width=True)



    
    with st.expander("14 - OPEP e Produção dos EUA: Impactos na Queda dos Preços do Petróleo Brent (2018 a 2019)"):
        st.subheader(':red[OPEP e Produção dos EUA: Impactos na Queda dos Preços do Petróleo Brent (2018 a 2019)]'
                         , divider='red')
        st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>

            Entre outubro de 2018 e janeiro de 2019, o preço do petróleo Brent experimentou uma significativa 
            queda de $85 para $50 por barril, um declínio marcante que refletiu diversos desafios no mercado global 
            de energia. Um dos principais fatores que contribuíram para essa queda foi o desequilíbrio entre oferta 
            e demanda. 
                    
            A decisão da OPEP (Organização dos Países Exportadores de Petróleo) e de outros grandes 
            produtores, como a Rússia, de não implementar cortes substanciais na produção de petróleo foi crucial. 
            Isso ocorreu em um contexto em que a produção de petróleo nos Estados Unidos atingiu níveis historicamente 
            altos, alimentada pela exploração de recursos de xisto.

            A saturação do mercado com oferta abundante exacerbou o impacto da desaceleração econômica global, 
            que estava começando a se manifestar naquela época. A incerteza econômica, especialmente em relação 
            às tensões comerciais entre os Estados Unidos e a China, também desempenhou um papel na redução da 
            demanda por petróleo.

            Além disso, fatores geopolíticos, como sanções internacionais e crises regionais, influenciaram 
            a dinâmica de preços, adicionando volatilidade ao mercado de petróleo durante esse período. 
            A combinação desses elementos criou um ambiente desafiador para os produtores de petróleo e os 
            investidores, levando a uma correção significativa nos preços do petróleo Brent.

            Essa queda destacou a sensibilidade do mercado de energia a fatores econômicos e geopolíticos globais,
            sublinhando a complexidade e a interconexão das forças que moldam os preços do petróleo em escala mundial.
            """,unsafe_allow_html=True,
            )
        

        

        # Evento específico de interesse
        evento = {
            'evento': 'OPEP e Produção dos EUA: Impactos na Queda dos Preços do Petróleo Brent',
            'ano': 2018
        }

        # Filtrar os dados para o período de janeiro de 2018 a fevereiro de 2019
        data_evento = data[(data['ds'] >= '2018-01-01') & (data['ds'] <= '2019-02-28')]

        # Encontrar a data do maior valor de janeiro de 2018
        data_maior_janeiro = data_evento[(data_evento['ds'].dt.year == 2018) & (data_evento['ds'].dt.month == 1)].nlargest(1, 'y')

        # Encontrar a data do menor valor do ano de 2018-2019
        data_menor_ano = data_evento.nsmallest(1, 'y')

        # Definir os limites do eixo x com base nas datas filtradas
        xlim_min = data_evento['ds'].min()
        xlim_max = data_evento['ds'].max()

        # Criar o gráfico de série temporal para o evento específico
        fig = go.Figure()

        # Adicionar linha do preço ao longo do evento
        fig.add_trace(go.Scatter(x=data_evento['ds'], y=data_evento['y'], mode='lines', name='Preço do Petróleo'))

        # Adicionar marcador para 01/10/2018 (outubro de 2018)
        fig.add_trace(go.Scatter(x=['2018-10-01'], y=[data_evento[data_evento['ds'] == '2018-10-01']['y'].values[0]],
                                mode='markers', name='Aumento da produção de Petróleo',
                                marker=dict(color='#363636', size=15)))

        # Adicionar marcador para o menor valor do ano
        fig.add_trace(go.Scatter(x=data_menor_ano['ds'], y=data_menor_ano['y'],
                                mode='markers', name='Menor Valor durante o acordo',
                                marker=dict(color='#800000', size=15)))

        # Configurar título e eixos
        fig.update_traces(line=dict(color='#FF4B4B'), hovertemplate='Data: %{x|%d-%m-%Y}<br>Preço: %{y}')
        fig.update_layout(title=f'Preço do Petróleo Brent - {evento["evento"]} (2018 a 2019)',
                        xaxis_title='Data',
                        yaxis_title='Preço (USD)',
                        paper_bgcolor='#d2d0d0',
                        xaxis=dict(range=[xlim_min, xlim_max], tickformat='%B-%Y'),
                        legend=dict(orientation="h", yanchor="top", y=1.1, xanchor="center", x=0.5),
                        )
        st.plotly_chart(fig,use_container_width=True)

        
    with st.expander("15 - Ataques às Instalações de Petróleo Sauditas (2019)"):
        st.subheader(':red[Ataques às Instalações de Petróleo Sauditas (2019)]'
                         , divider='red')
        st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>

            Os ataques às instalações de petróleo sauditas em setembro de 2019, atribuídos ao Irã ou seus 
            aliados no Iêmen, resultaram em uma redução drástica na produção de petróleo no maior exportador
            mundial de petróleo. Isso teve um impacto imediato e significativo nos preços do petróleo Brent.

            Os preços do petróleo Brent subiram cerca de <strong style='font-size: 18px'>15%</strong> logo após os ataques, 
            passando de cerca de 
            <strong style='font-size: 18px'>60\$</strong> por barril para cerca de <strong style='font-size: 18px'>70\$</strong> por barril. Essa escalada refletiu as preocupações 
            com a segurança do fornecimento global de petróleo e a resposta imediata do mercado às interrupções 
            na produção saudita.

            Os ataques às instalações de petróleo sauditas em 2019 resultaram em um aumento significativo nos 
            preços do petróleo Brent, refletindo as preocupações com a segurança do fornecimento global de petróleo 
            devido às interrupções na produção no maior exportador mundial de petróleo.</h1>

            """,unsafe_allow_html=True,
            )
        

        # Evento específico de interesse
        evento = {
            'evento': 'Ataques às Instalações de Petróleo Sauditas',
            'ano': 2019
        }

        # Filtrar os dados para o ano de 2019
        data_evento = data[(data['ds'].dt.year == 2019)]

        # Encontrar a data do maior valor durante setembro de 2019
        data_maior_setembro = data_evento[(data_evento['ds'] >= '2019-09-01') & (data_evento['ds'] <= '2019-09-30')].nlargest(1, 'y')

        # Criar o gráfico de série temporal para o evento específico
        fig = go.Figure()

        # Adicionar linha do preço ao longo do evento
        fig.add_trace(go.Scatter(x=data_evento['ds'], y=data_evento['y'], mode='lines', name='Preço do Petróleo'))

        # Adicionar marcador para 12/09/2019
        fig.add_trace(go.Scatter(x=['2019-09-12'], y=[data_evento[data_evento['ds'] == '2019-09-12']['y'].values[0]],
                                mode='markers', name='Ataques às Instalações de Petróleo Sauditas',
                                marker=dict(color='#363636', size=15)))

        # Adicionar marcador para o maior valor durante setembro de 2019
        fig.add_trace(go.Scatter(x=data_maior_setembro['ds'], y=data_maior_setembro['y'],
                                mode='markers', name='Aumento nos preços devido ao Evento',
                                marker=dict(color='#800000', size=15)))

        # Configurar título e eixos
        fig.update_traces(line=dict(color='#FF4B4B'), hovertemplate='Data: %{x|%d-%m-%Y}<br>Preço: %{y}')
        fig.update_layout(title=f'Preço do Petróleo Brent - {evento["evento"]} (2019)',
                        xaxis_title='Data',
                        yaxis_title='Preço (USD)',
                        paper_bgcolor='#d2d0d0',
                        xaxis=dict(tickformat='%d-%m-%Y'),
                        legend=dict(orientation="h", yanchor="top", y=1.1, xanchor="center", x=0.5),
                        )
        st.plotly_chart(fig,use_container_width=True)

    
    with st.expander("16 - Pandemia de COVID-19 (2020)"):
        st.subheader(':red[Pandemia de COVID-19 (2020)]'
                         , divider='red')
        st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>

            A pandemia de COVID-19 em 2020 teve um impacto sem precedentes nos mercados globais, 
            incluindo o mercado de petróleo Brent. O colapso na demanda por energia devido a bloqueios
            e restrições de viagem globais levou a uma queda dramática nos preços do petróleo.

            Os preços do petróleo Brent caíram mais de <strong style='font-size: 18px'>87%</strong> 
            no primeiro semestre de 2020, passando de cerca 
            de <strong style='font-size: 18px'>70\$</strong> por barril no início do ano para menos de <strong style='font-size: 18px'>9\$</strong> por barril em abril. 
            Essa queda histórica refletiu a combinação de uma demanda global deprimida e uma oferta 
            excessiva de petróleo no mercado.

            A pandemia de COVID-19 em 2020 resultou em uma queda dramática nos preços do petróleo Brent, 
            refletindo a redução sem precedentes na demanda por energia devido aos bloqueios globais e às 
            restrições de viagem para conter a propagação do vírus.</h1>

            """,unsafe_allow_html=True,
            )
        
        

        # Evento específico de interesse
        evento = {
            'evento': 'Pandemia de COVID-19',
            'ano': 2020
        }

        # Filtrar os dados para o ano de 2020
        data_evento = data[(data['ds'].dt.year == 2020)]

        # Encontrar a data de 11 de março de 2020
        data_11_marco = data_evento[data_evento['ds'] == '2020-03-02']

        # Encontrar o menor valor do ano de 2020
        menor_valor_2020 = data_evento.nsmallest(1, 'y')

        # Criar o gráfico de série temporal para o evento específico
        fig = go.Figure()

        # Adicionar linha do preço ao longo do evento
        fig.add_trace(go.Scatter(x=data_evento['ds'], y=data_evento['y'], mode='lines', name='Preço do Petróleo'))

        # Adicionar marcador para 11 de março de 2020
        fig.add_trace(go.Scatter(x=data_11_marco['ds'], y=data_11_marco['y'],
                                mode='markers', name='Inicio da Pandemia COVID-19',
                                marker=dict(color='#363636', size=15)))

        # Adicionar marcador para o menor valor do ano de 2020
        fig.add_trace(go.Scatter(x=menor_valor_2020['ds'], y=menor_valor_2020['y'],
                                mode='markers', name='Pico de queda durante pandemia',
                                marker=dict(color='#800000', size=15)))

        # Configurar título e eixos
        fig.update_traces(line=dict(color='#FF4B4B'), hovertemplate='Data: %{x|%d-%m-%Y}<br>Preço: %{y}')
        fig.update_layout(title=f'Preço do Petróleo Brent - {evento["evento"]} ({evento["ano"]})',
                        xaxis_title='Data',
                        yaxis_title='Preço (USD)',
                        paper_bgcolor='#d2d0d0',
                        xaxis=dict(tickformat='%B-%Y'),
                        legend=dict(orientation="h", yanchor="top", y=1.1, xanchor="center", x=0.5),
                        )

        st.plotly_chart(fig,use_container_width=True)

        
    with st.expander("17 - Invasão da Ucrânia pela Rússia e sanções subsequentes (2022-2024)"):
        st.subheader(':red[Invasão da Ucrânia pela Rússia e sanções subsequentes (2022-2024)]'
                         , divider='red')
        st.markdown("""
            <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>

            A invasão da Ucrânia pela Rússia em 24 de fevereiro 2022 e as sanções econômicas subsequentes 
            tiveram um impacto 
            significativo nos mercados globais, incluindo o mercado de petróleo Brent. Ao anunciar 
            a invasão o mercado teve uma subida ingrime de <strong style='font-size: 18px'>103\$</strong> ate <strong style='font-size: 18px'>130\$</strong> o preco
            do barril. 
                    
            Os preços do petróleo Brent estava em subida e chegou a <strong style='font-size: 18px'>130\$</strong> ate a sancoes economicas contra
            a Russia. subiram cerca de <strong style='font-size: 18px'>30%</strong> após o início da invasão da Ucrânia, 
            passando de cerca de 
            <strong style='font-size: 18px'>90\$</strong> por barril para cerca de <strong style='font-size: 18px'>130\$</strong> por barril. Essa escalada refletiu as preocupações 
            com a segurança do fornecimento global de petróleo e as implicações das sanções econômicas contra a 
            Rússia.

            Em resumo, a invasão da Ucrânia pela Rússia em 2022 e as sanções econômicas subsequentes resultaram em um 
            aumento nos preços do petróleo Brent, refletindo as preocupações com a segurança do fornecimento 
            global de petróleo devido às tensões geopolíticas e às sanções contra um dos principais produtores 
            mundiais de petróleo.

            Esses eventos destacam a complexidade e a interconectividade dos fatores que influenciam os preços 
            do petróleo Brent ao longo das décadas, desde crises geopolíticas até mudanças estruturais no mercado 
            global de energia.</h1>
                    
            

            """,unsafe_allow_html=True,
            )
        
        # Evento específico de interesse
        evento = {
            'evento': 'Invasão da Ucrânia pela Rússia e sanções subsequentes',
            'ano': '2022-2024'
        }

        # Filtrar os dados para o período de 2022 até o período atual
        data_evento = data[data['ds'].dt.year >= 2022]

        # Encontrar o maior valor de março de 2022
        maior_valor_marco_2022 = data_evento[(data_evento['ds'].dt.year == 2022) & (data_evento['ds'].dt.month == 3)].nlargest(1, 'y')

        # Encontrar o menor valor entre 2022 e 2024
        menor_valor_2022_2024 = data_evento[(data_evento['ds'].dt.year >= 2022) & (data_evento['ds'].dt.year <= 2024)].nsmallest(1, 'y')

        # Criar o gráfico de série temporal para o evento específico
        fig = go.Figure()

        # Adicionar linha do preço ao longo do evento
        fig.add_trace(go.Scatter(x=data_evento['ds'], y=data_evento['y'], mode='lines', name='Preço do Petróleo'))

        # Adicionar marcador para o maior valor de março de 2022
        fig.add_trace(go.Scatter(x=maior_valor_marco_2022['ds'], y=maior_valor_marco_2022['y'],
                                mode='markers', name='Sanções Econômicas Contra Russia',
                                marker=dict(color='#363636', size=15)))

        # Adicionar marcador para o menor valor entre 2022 e 2024
        fig.add_trace(go.Scatter(x=menor_valor_2022_2024['ds'], y=menor_valor_2022_2024['y'],
                                mode='markers', name='Menos valor durante período do Evento',
                                marker=dict(color='#800000', size=15)))

        # Configurar título e eixos
        fig.update_traces(line=dict(color='#FF4B4B'), hovertemplate='Data: %{x|%d-%m-%Y}<br>Preço: %{y}')
        fig.update_layout(title=f'Preço do Petróleo Brent - {evento["evento"]} ({evento["ano"]})',
                        xaxis_title='Data',
                        yaxis_title='Preço (USD)',
                        paper_bgcolor='#d2d0d0',
                        xaxis=dict(tickformat='%B-%Y'),
                        legend=dict(orientation="h", yanchor="top", y=1.1, xanchor="center", x=0.5),
                        )

        st.plotly_chart(fig,use_container_width=True)
        
