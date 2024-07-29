import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados
file_path = "Planilha.csv"
df = pd.read_csv(file_path)

# Título do aplicativo
st.title('🌟 Exploração de Termos Culturais 🌟')

# Barra lateral para seleção de termo e outras opções
st.sidebar.header('Opções de Exploração')
selected_term = st.sidebar.selectbox('Selecione um Termo:', df['Conceito'].unique())

# Tabela completa na barra lateral
st.sidebar.write('### Tabela Completa')
st.sidebar.dataframe(df)

# Seção principal
st.header(f'🔍 Detalhes do Termo: {selected_term}')
filtered_df = df[df['Conceito'] == selected_term]

if not filtered_df.empty:
    st.write(f"**Definição:** {filtered_df.iloc[0]['Definição']}")
    st.write(f"**Termos Alternativos:** {filtered_df.iloc[0]['Termos Alternativos']}")
    st.write(f"**Relação:** {filtered_df.iloc[0]['Relação']}")
    st.write(f"**Categoria:** {filtered_df.iloc[0]['Categoria']}")

    # Verificar se as colunas necessárias existem
    if 'Relação' in filtered_df.columns and 'Valor' in filtered_df.columns and 'Categoria' in filtered_df.columns:
        # Exemplo de gráfico interativo com Plotly
        st.write("### Visualização da Relação")
        fig = px.bar(filtered_df, x='Relação', y='Valor', color='Categoria', 
                     labels={'Relação': 'Relações', 'Valor': 'Valores'},
                     title=f'Relações para o termo: {selected_term}')
        st.plotly_chart(fig)
    else:
        st.write("Os dados necessários para o gráfico não estão disponíveis.")

else:
    st.write("Termo não encontrado.")

# Rodar a aplicação com o comando: streamlit run nome_do_arquivo.py
