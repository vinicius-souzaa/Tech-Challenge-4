import streamlit as st
from util.layout import layout_saida


st.set_page_config(
    page_title="Introdução | Tech Challenge 4",
    layout="wide",page_icon="📰"
)

layout_saida()



with st.container():
    st.header(":red[Introdução]")
    
    st.markdown(
        """
        <h1 style='text-align:justify; 
            font-size:15px;
            font-family: Arial, sans-serif; 
            font-weight: normal;
            line-height:1.5'>

        Nesta introdução, são descritos alguns tópicos importantes para o entendimento do projeto,
        dentre eles oque é o petróleo Brent, IPEA, bibliotecas utilizadas e Insights Esperados</h1>
        """,unsafe_allow_html=True
        )
    
    st.markdown("""<style>.stTabs [data-baseweb="tab-list"] 
                        button [data-testid="stMarkdownContainer"] 
                        p {font-size:14.5px;
                            font-family: Arial,    
                            sans-serif;
                            font-weight: normal;
                            color-scheme: light;
                            }
                        </style>
                        """, unsafe_allow_html=True)

    tab0, tab1, tab2, tab3, tab4 = st.tabs(
        tabs=[
            "Petróleo Brent",
            "IPEA",
            "Prophet (Meta)",
            "Insights Esperados",
            "Bibliotecas"
        ]
    )

    with tab0:
        st.subheader(':red[Petróleo Brent: Origens, Importância e Impactos Globais]'
                         , divider='red')
        st.markdown("""
                        <h1 style='text-align:justify; 
                                    font-size:15px;
                                    font-family: Arial, sans-serif; 
                                    font-weight: normal;
                                    line-height:1.5'>
                        
                O petróleo é uma das commodities mais valiosas e disputadas do mundo, 
                desempenhando um papel crucial no funcionamento da economia global. 
                Dentre os diversos tipos de petróleo bruto extraídos ao redor do mundo, 
                o petróleo Brent se destaca como um dos mais importantes e amplamente negociados. 
                Este texto explora a origem, a importância e os impactos globais do petróleo Brent, 
                proporcionando uma visão abrangente sobre esta commodity vital.</h1>
                """, unsafe_allow_html=True)

        st.subheader(':red[Origem do Petróleo Brent]'
                        , divider='red')
        st.markdown("""
                    <h1 style='text-align:justify; 
                                font-size:15px;
                                font-family: Arial, sans-serif; 
                                font-weight: normal;
                                line-height:1.5'>
                    
            O petróleo Brent é uma mistura de petróleo cru extraído do Mar do Norte, 
            especificamente das áreas de Brent, Oseberg, Forties e Ekofisk, 
            localizadas entre a Noruega e o Reino Unido. O nome "Brent" deriva de um 
            campo de petróleo situado no Mar do Norte, descoberto pela Shell em 1971. 
            Este campo foi um dos primeiros grandes campos de petróleo a ser explorado
            na região e, ao longo do tempo, o nome Brent tornou-se sinônimo do petróleo
            extraído de toda a área circundante.</h1>
            """, unsafe_allow_html=True)

        st.subheader(':red[Características do Petróleo Brent]'
                        , divider='red')
        st.markdown("""
                    <h1 style='text-align:justify; 
                                font-size:15px;
                                font-family: Arial, sans-serif; 
                                font-weight: normal;
                                line-height:1.5'>  
                        
            O petróleo Brent é classificado como um petróleo leve e doce. 
            A classificação "leve" refere-se à sua baixa densidade e à capacidade de fluir 
            facilmente, enquanto "doce" indica um baixo teor de enxofre. 
            Estas características tornam o Brent particularmente atraente para refinarias, 
            pois o petróleo leve e doce é mais fácil e menos custoso de processar em produtos 
            refinados de alta qualidade, como gasolina e diesel. Além disso, a localização dos 
            campos de petróleo do Mar do Norte em relação aos grandes mercados consumidores da Europa 
            e da América do Norte adiciona uma camada de conveniência logística.</h1>
                    """, unsafe_allow_html=True)

        st.subheader(':red[Importância do Petróleo Brent]'
                        , divider='red')
        st.markdown("""
                    <h1 style='text-align:justify; 
                                font-size:15px;
                                font-family: Arial, sans-serif; 
                                font-weight: normal;
                                line-height:1.5'> 
                        
            O petróleo Brent é considerado um benchmark (referência) no mercado global de petróleo. 
            Os benchmarks são utilizados para precificar diferentes tipos de petróleo cru 
            extraídos em várias partes do mundo. Além do Brent, outros benchmarks importantes
            incluem o West Texas Intermediate (WTI) nos Estados Unidos e o Dubai/Oman no Oriente Médio. 
            O preço do petróleo Brent é amplamente utilizado como referência para mais de dois terços 
            dos contratos globais de petróleo bruto, refletindo sua significância no comércio 
            internacional de petróleo.</h1>
                    """, unsafe_allow_html=True)

        st.subheader(':red[Negociação e Formação de Preços]'
                        , divider='red')
        st.markdown("""
                    <h1 style='text-align:justify; 
                                font-size:15px;
                                font-family: Arial, sans-serif; 
                                font-weight: normal;
                                line-height:1.5'>   
                        
            A negociação do petróleo Brent ocorre principalmente no mercado futuro, onde contratos 
            são comprados e vendidos em bolsas de valores, como a Intercontinental Exchange (ICE). 
            O preço do Brent é influenciado por uma variedade de fatores, incluindo a oferta e 
            demanda globais de petróleo, eventos geopolíticos, condições econômicas e políticas 
            de produção de países membros da Organização dos Países Exportadores de Petróleo (OPEP) 
            e aliados, conhecidos como OPEP+.</h1>
                    """, unsafe_allow_html=True)

        st.subheader(':red[Fatores Geopolíticos e Econômicos]'
                        , divider='red')
        st.markdown("""
                    <h1 style='text-align:justify; 
                                font-size:15px;
                                font-family: Arial, sans-serif; 
                                font-weight: normal;
                                line-height:1.5'>
                    
            Os preços do petróleo Brent são altamente sensíveis a eventos geopolíticos. Conflitos,
            instabilidade política, sanções econômicas e decisões estratégicas de grandes 
            produtores de petróleo podem causar flutuações significativas nos preços. 
            Por exemplo, tensões no Oriente Médio, uma região crucial para a produção 
            e exportação de petróleo, frequentemente resultam em aumentos nos preços 
            devido ao medo de interrupções no fornecimento.
                    
            Além disso, fatores econômicos globais desempenham um papel crucial na formação dos preços. 
            Durante períodos de crescimento econômico, a demanda por petróleo tende a aumentar, 
            pressionando os preços para cima. Em contrapartida, durante recessões econômicas, 
            a demanda por petróleo pode diminuir, resultando em preços mais baixos. A pandemia 
            de COVID-19 é um exemplo recente de como eventos econômicos podem impactar os preços
            do petróleo. Durante o auge da pandemia, a demanda por petróleo caiu drasticamente 
            devido às restrições de mobilidade e à desaceleração econômica global, 
            levando a uma queda acentuada nos preços do Brent.</h1>
                    """, unsafe_allow_html=True)

        st.subheader(':red[Impactos Ambientais e Transição Energética]'
                        , divider='red')
        st.markdown("""
                    <h1 style='text-align:justify; 
                                font-size:15px;
                                font-family: Arial, sans-serif; 
                                font-weight: normal;
                                line-height:1.5'>
                    
            Enquanto o petróleo Brent continua a ser uma peça fundamental da economia global, 
            sua produção e consumo estão associados a impactos ambientais significativos. 
            A extração, transporte e refino do petróleo podem causar derramamentos e poluição, 
            enquanto a queima de combustíveis fósseis é uma das principais fontes de emissões 
            de gases de efeito estufa, contribuindo para as mudanças climáticas.\n

            Em resposta a essas preocupações, há um movimento crescente em direção à transição energética, 
            com muitos países e empresas investindo em fontes de energia renovável e tecnologias de baixa 
            emissão de carbono. No entanto, a transição energética é um processo complexo e gradual, 
            e o petróleo Brent ainda deve desempenhar um papel importante na matriz energética
            global nas próximas décadas, mesmo com a crescente adoção de energias alternativas.</h1>
            """, unsafe_allow_html=True)

        st.subheader(':red[O Futuro do Petróleo Brent]'
                        , divider='red')
        st.markdown("""
                    <h1 style='text-align:justify; 
                                font-size:15px;
                                font-family: Arial, sans-serif; 
                                font-weight: normal;
                                line-height:1.5'>
                    
            O futuro do petróleo Brent será moldado por uma confluência de fatores econômicos, tecnológicos, 
            geopolíticos e ambientais. À medida que o mundo avança em direção a uma economia de 
            baixo carbono, a demanda por petróleo pode eventualmente diminuir, pressionando os 
            preços para baixo. No entanto, a inovação tecnológica e a adaptação da indústria do 
            petróleo às novas realidades energéticas podem prolongar a relevância do Brent.

            A digitalização e a inteligência artificial estão começando a desempenhar papéis 
            significativos na indústria do petróleo, otimizando processos de extração, 
            transporte e refino, reduzindo custos e minimizando impactos ambientais. 
            Além disso, a indústria está explorando formas de capturar e armazenar carbono 
            para mitigar as emissões associadas ao uso de petróleo.</h1>
                            """, unsafe_allow_html=True)

        st.subheader(':red[Considerações Finais]'
                        , divider='red')
        st.markdown("""
                    <h1 style='text-align:justify; 
                                font-size:15px;
                                font-family: Arial, sans-serif; 
                                font-weight: normal;
                                line-height:1.5'>
                    
            O petróleo Brent, com sua origem no Mar do Norte e sua posição como benchmark global, 
            é um componente vital da economia mundial. Sua importância transcende o simples 
            valor econômico, influenciando a política internacional, a segurança energética 
            e as estratégias de desenvolvimento sustentável. Enquanto o mundo navega pelas 
            complexidades da transição energética e das mudanças climáticas, o papel do 
            petróleo Brent evoluirá, refletindo as novas realidades e desafios do século XXI.\n

            Apesar dos desafios ambientais e das incertezas econômicas, o Brent continuará a ser 
            uma commodity essencial, adaptando-se às novas demandas e inovando em resposta 
            às pressões globais. A compreensão profunda de sua dinâmica e impacto é crucial 
            para formuladores de políticas, economistas, ambientalistas e todos aqueles que 
            buscam um futuro sustentável e equilibrado para a energia global.</h1>
                            """, unsafe_allow_html=True)
    
    with tab1:
        st.subheader(
                ":red[Instituto de Pesquisa Econômica Aplicada (IPEA)]", divider="red"
            )
        st.markdown("""
                    <h1 style='text-align:justify; 
                                font-size:15px;
                                font-family: Arial, sans-serif; 
                                font-weight: normal;
                                line-height:1.5'>
                    
            O Instituto de Pesquisa Econômica Aplicada (IPEA) é uma instituição pública brasileira, 
            vinculada ao Ministério da Economia, que desempenha um papel crucial na análise e formulação 
            de políticas públicas no Brasil. Fundado em 1964, o IPEA é responsável por conduzir pesquisas 
            e estudos econômicos, sociais e ambientais, oferecendo suporte técnico e científico ao governo 
            federal na elaboração de estratégias de desenvolvimento nacional.

            A missão do IPEA é fornecer informações e análises baseadas em evidências que auxiliem na 
            tomada de decisões informadas, promovendo um crescimento econômico sustentável e a redução 
            das desigualdades sociais. Seus estudos abrangem uma vasta gama de áreas, incluindo economia, 
            educação, saúde, meio ambiente, infraestrutura, segurança pública, entre outros.

            O IPEA também se destaca pela produção de indicadores e estatísticas econômicas que são 
            amplamente utilizados por pesquisadores, acadêmicos e formuladores de políticas. 
            Entre suas publicações mais notáveis estão o "Boletim de Conjuntura", que analisa o panorama 
            econômico atual, e o "Comunicado do IPEA", que aborda temas específicos de interesse público.

            Além de suas pesquisas, o IPEA realiza eventos, seminários e debates que fomentam a troca de 
            conhecimentos e a disseminação de informações relevantes para o desenvolvimento do país. 
            Dessa forma, o IPEA contribui significativamente para o avanço do conhecimento e a 
            implementação de políticas públicas eficazes no Brasil, sendo um pilar essencial para o 
            planejamento e a avaliação de ações governamentais.</h1>
                                    
        """,
            unsafe_allow_html=True,
        )

    with tab2:
        st.subheader(
                ":red[Prophet]", divider="red"
            )
        st.markdown("""
                    <h1 style='text-align:justify; 
                                font-size:15px;
                                font-family: Arial, sans-serif; 
                                font-weight: normal;
                                line-height:1.5'>
                    
            A biblioteca Prophet, desenvolvida pela Meta (anteriormente conhecida como Facebook), 
            é uma ferramenta poderosa para a previsão de séries temporais. Lançada em 2017, 
            essa biblioteca de código aberto foi projetada para lidar com dados que possuem 
            padrões sazonais diários, semanais e anuais, além de acomodar feriados e eventos 
            especiais que possam afetar a série temporal.

            Uma das principais características do Prophet é sua facilidade de uso. 
            Ela foi criada para ser acessível tanto para analistas de dados quanto para desenvolvedores, 
            mesmo aqueles com pouca experiência em modelagem de séries temporais. A biblioteca oferece 
            uma interface simples para ajustar modelos de previsão, permitindo aos usuários especificar 
            de forma intuitiva os componentes sazonais e os eventos que desejam incluir na análise.

            O Prophet é baseado em um modelo aditivo onde componentes sazonais são modelados como 
            somas de funções periódicas. Isso permite uma grande flexibilidade na captura de padrões 
            sazonais complexos. Além disso, o Prophet é robusto a dados ausentes e mudanças em tendências, 
            o que o torna adequado para uma ampla gama de aplicações no mundo real.

            Outra vantagem significativa da biblioteca é sua capacidade de fornecer previsões com 
            intervalos de confiança, ajudando os usuários a entender a incerteza associada às suas 
            previsões. O Prophet também facilita a detecção de pontos de mudança na tendência, 
            permitindo ajustes automáticos no modelo quando ocorrem mudanças significativas na 
            série temporal.

            Em resumo, a biblioteca Prophet da Meta é uma ferramenta valiosa para a previsão de 
            séries temporais, combinando facilidade de uso, flexibilidade e robustez. 
            Ela é amplamente utilizada em diversas indústrias para prever demanda, vendas, tráfego 
            da web e muitos outros tipos de dados temporais, ajudando as organizações a tomar 
            decisões mais informadas e baseadas em dados.</h1>                 
            """,
                unsafe_allow_html=True,
            )
    
    with tab3:
        st.subheader(
                ":red[Insights Esperados]", divider="red"
            )
        st.markdown("""
                    <h1 style='text-align:justify; 
                                font-size:15px;
                                font-family: Arial, sans-serif; 
                                font-weight: normal;
                                line-height:1.5'>
                    
                    Durante a análise dos dados históricos, esperamos identificar e destacar insights como:

                    1 - Impactos Geopolíticos: Analisar como eventos como guerras, sanções e tensões políticas 
                    afetaram os preços do petróleo.

                    2 - Crises Econômicas: Investigar a correlação entre recessões econômicas globais 
                    e variações no preço do petróleo.

                    3 - Demandas de Energia: Estudar como mudanças na demanda global por energia 
                    influenciaram os preços.

                    4 - Padrões Sazonais e Tendências: Identificar padrões sazonais e tendências de longo prazo nos preços do petróleo.</h1>
                                                    
                        """,
            unsafe_allow_html=True,
        )    
    
    with tab4:

        st.subheader(':red[Bibliotecas]'
                        , divider='red')
        st.markdown("""
                    <h1 style='text-align:justify; 
                                font-size:15px;
                                font-family: Arial, sans-serif; 
                                font-weight: normal;
                                line-height:1.5'>    
                    Segue abaixo as outras principais bibliotecas utilizadas no projeto: 
                    """, unsafe_allow_html=True)

        st.subheader(':red[Pandas]'
                        , divider='red')
        st.markdown("""
                    <h1 style='text-align:justify; 
                                font-size:15px;
                                font-family: Arial, sans-serif; 
                                font-weight: normal;
                                line-height:1.5'>    
                    A biblioteca Pandas é uma ferramenta poderosa e essencial para a manipulação e 
                    análise de dados em Python. Ela oferece estruturas de dados de alto desempenho, 
                    como DataFrames e Series, que facilitam a organização, filtragem, agregação e transformação 
                    de grandes conjuntos de dados. Com Pandas, é possível ler e escrever dados de diversos 
                    formatos, como CSV, Excel e SQL, além de realizar operações de limpeza e preparação de 
                    dados de maneira eficiente. A sintaxe intuitiva e as funcionalidades robustas da biblioteca 
                    tornam-na uma escolha popular entre cientistas de dados e analistas, permitindo a exploração 
                    e visualização de dados de forma ágil e eficaz.
                    """, unsafe_allow_html=True)
        
        st.subheader(':red[Numpy]'
                        , divider='red')
        st.markdown("""
                    <h1 style='text-align:justify; 
                                font-size:15px;
                                font-family: Arial, sans-serif; 
                                font-weight: normal;
                                line-height:1.5'>    
                    NumPy é uma biblioteca fundamental para computação científica em Python. Fornece suporte para 
                    arrays e matrizes multidimensionais, além de uma coleção de funções matemáticas para operações 
                    rápidas em grandes volumes de dados. É amplamente utilizada em diversos campos, como física, 
                    engenharia e análise de dados. NumPy permite manipulação eficiente de dados numéricos, com funções 
                    para álgebra linear, transformadas de Fourier e geração de números aleatórios. Sua capacidade de 
                    integração com outras bibliotecas científicas, como SciPy e pandas, torna-o uma ferramenta essencial 
                    para desenvolvimento de soluções avançadas em ciência de dados e aprendizado de máquina
                    """, unsafe_allow_html=True)
        
        st.subheader(':red[Missingno]'
                        , divider='red')
        st.markdown("""
                    <h1 style='text-align:justify; 
                                font-size:15px;
                                font-family: Arial, sans-serif; 
                                font-weight: normal;
                                line-height:1.5'>
                    A biblioteca missingno é uma ferramenta poderosa para visualização de dados faltantes em conjuntos 
                    de dados. Facilita a identificação e análise de padrões de ausência de dados através de gráficos 
                    intuitivos, como matrizes de calor, dendrogramas e gráficos de barras. Utilizando o missingno, 
                    os cientistas de dados podem rapidamente detectar a quantidade e a localização de valores ausentes, 
                    entender melhor a estrutura do conjunto de dados e decidir sobre estratégias de imputação ou exclusão
                    de dados faltantes. Esta visualização clara e eficiente é essencial para preparar dados de forma 
                    adequada, garantindo análises mais precisas e modelos de machine learning mais robustos.
                    """, unsafe_allow_html=True)

        st.subheader(':red[Stats Models]'
                        , divider='red')
        st.markdown("""
                    <h1 style='text-align:justify; 
                                font-size:15px;
                                font-family: Arial, sans-serif; 
                                font-weight: normal;
                                line-height:1.5'>
                    A biblioteca Statsmodels é uma ferramenta poderosa para a análise estatística em Python, 
                    oferecendo uma ampla gama de métodos para modelagem estatística, teste de hipóteses e 
                    exploração de dados. Com ela, é possível realizar regressões lineares e não lineares, 
                    análise de séries temporais, modelos de efeito fixo e aleatório, entre outros. 
                    Statsmodels se destaca por sua capacidade de fornecer resultados detalhados, 
                    incluindo estatísticas de resumo, intervalos de confiança e testes de significância.
                    Além disso, integra-se bem com outras bibliotecas populares, como Pandas e NumPy, 
                    facilitando a manipulação e análise de dados complexos em projetos de ciência de dados 
                    e econometria.
                    """, unsafe_allow_html=True)
        
      

        st.subheader(':red[Plotly]'
                        , divider='red')
        st.markdown("""
                    <h1 style='text-align:justify; 
                                font-size:15px;
                                font-family: Arial, sans-serif; 
                                font-weight: normal;
                                line-height:1.5'>    
                    A Plotly é uma biblioteca de visualização de dados altamente interativa e versátil, 
                    amplamente utilizada em Python. Ela permite a criação de gráficos dinâmicos e complexos 
                    com facilidade, suportando uma vasta gama de tipos de gráficos, como linhas, barras, 
                    dispersão, mapas, entre outros. Um dos grandes destaques da Plotly é a capacidade de criar 
                    gráficos interativos que podem ser incorporados em dashboards web, facilitando a análise 
                    e apresentação de dados. Além disso, ela oferece integração com bibliotecas populares 
                    como pandas e NumPy, tornando-se uma ferramenta poderosa para cientistas de dados e 
                    desenvolvedores que buscam apresentar suas análises de forma visualmente atraente e 
                    informativa.
                    """, unsafe_allow_html=True)
        
        st.subheader(':red[Streamlit]'
                        , divider='red')
        st.markdown("""
                    <h1 style='text-align:justify; 
                                font-size:15px;
                                font-family: Arial, sans-serif; 
                                font-weight: normal;
                                line-height:1.5'>
                    Streamlit é uma biblioteca de código aberto em Python, ideal para criar aplicativos web 
                    interativos de maneira rápida e simples. Focada em cientistas de dados e desenvolvedores, 
                    Streamlit permite transformar scripts de dados em aplicativos web funcionais com poucas 
                    linhas de código. Com suporte para widgets interativos como sliders, seletores de datas 
                    e gráficos dinâmicos, Streamlit facilita a visualização de dados em tempo real. 
                    É altamente integrável com outras bibliotecas de visualização como Plotly, Matplotlib 
                    e Altair. Sua simplicidade e eficiência têm tornado o Streamlit uma escolha popular 
                    para criar dashboards e ferramentas de análise de dados interativas.
                    """, unsafe_allow_html=True)
        
    
