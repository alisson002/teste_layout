import streamlit as st
import pandas as pd

def dataInput_session():
    # Verifique e defina o estado inicial das datas se necessário
    if 'data_inicio' not in st.session_state: # Verifica se a chave 'data_inicio' está no estado da sessão. Se não estiver, a chave é adicionada com a data inicial 2023-01-01.
        st.session_state['data_inicio'] = pd.to_datetime('2023-01-01')

    if 'data_fim' not in st.session_state: #Faz o mesmo para a chave 'data_fim', definindo a data final como 2024-06-06.
        st.session_state['data_fim'] = pd.to_datetime('2024-06-06')

    # Inputs de data na barra lateral
    data_inicio = st.sidebar.date_input(
        "Data de início",
        value=st.session_state['data_inicio'], # Data inicial
        min_value=pd.to_datetime('2023-01-01'),
        max_value=pd.to_datetime('2024-06-06'),
        format="YYYY-MM-DD",
        help="Data mínima provisória. Será alterada de acordo com desenvolvimento do sistema."
    )

    data_fim = st.sidebar.date_input(
        "Data de término",
        value=st.session_state['data_fim'], # Data final
        min_value=pd.to_datetime('2023-01-01'),
        max_value=pd.to_datetime('2024-06-06'),
        format="YYYY-MM-DD",
        help="Data máxima provisória. Será alterada de acordo com desenvolvimento do sistema."
    )


    """st.session_state

    É um objeto que permite armazenar e compartilhar dados entre diferentes execuções do código em uma sessão do usuário. Ele atua como uma memória persistente que mantém o estado entre as interações do usuário dentro da mesma sessão do navegador.

    'st.session_state' permite armazenar dados que devem persistir entre diferentes execuções do script dentro da mesma sessão do usuário. Por exemplo, se um usuário seleciona uma data em uma página e navega para outra página, o valor da data selecionada pode ser mantido usando 'st.session_state'.

    https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state

    """
    # Atualizar o estado se as datas mudarem
    if data_inicio != st.session_state['data_inicio']: #Verifica se a data de início selecionada pelo usuário é diferente da armazenada no estado da sessão.
        st.session_state['data_inicio'] = data_inicio #Se a data for diferente, atualiza o estado da sessão com a nova data.

    if data_fim != st.session_state['data_fim']: #Faz o mesmo para a data de término.
        st.session_state['data_fim'] = data_fim
