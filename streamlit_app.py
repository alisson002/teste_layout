import streamlit as st
import dataInput as dti

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

inicio = st.Page("paginas/inicio.py", title="Inicio", icon="🏠", default=True)
lista = st.Page("paginas/Lista de Espera.py", title="Lista de Espera", icon="📝")
agenda = st.Page("paginas/Agenda.py", title="Agenda", icon=":material/logout:")

dashboard = st.Page("paginas/Triagem/Geral.py", title="Geral", icon="👩🏾‍💼")
bugs = st.Page("paginas/Triagem/UFRN.py", title="UFRN", icon="🎓")

search = st.Page("paginas/SIGRH/search.py", title="Geral", icon="👨🏾‍💼")
history = st.Page("paginas/SIGRH/history.py", title="UFRN", icon="🎓")

pg = st.navigation(
        {
            "": [inicio, lista, agenda],
            "Triagem": [dashboard, bugs],
            "SIGRH": [search, history],
        }
    )
#pg = st.navigation([inicio])

dti.dataInput_session()

pg.run()