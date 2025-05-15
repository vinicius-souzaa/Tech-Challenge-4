import streamlit as st
import locale
from st_pages import show_pages, Page


def format_number(number, format='%0.0f'):
    return locale.format(format, number, grouping=True)

def layout_saida():

    st.html("<style>[data-testid='stHeaderActionElements'] {display: none;}</style>")
    
    show_pages(
        [
            Page("./main.py", "Tech Challenge 4", "🛠️"),
            Page("./paginas/intro.py","Introdução", "📰"),
            Page("./paginas/historia.py","Historia", "📚"),
            Page("./paginas/analise.py","Analise Exploratória de Dados (EDA)","📊"),
            Page("./paginas/modelo.py", "Modelo Preditivo", "💻"),
            Page("./paginas/conclusao.py","Conclusão","☁️"),
        ]
    )

    with st.sidebar:
        st.subheader("Alunos - Grupo 22 - Turma 3DTAT")
        
        st.markdown("""
                    <h1 style=font-size:16px; 
                    font-family: Arial, sans-serif; 
                    font-weight: normal;>

                    Vinicius Abreu Ernestino Souza\n
                    RM 353049
                    </h1>
                    """, unsafe_allow_html=True)
       
        
        

