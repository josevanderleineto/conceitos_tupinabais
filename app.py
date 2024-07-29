import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados
file_path = "Planilha.csv"
df = pd.read_csv(file_path)

# Adicionar estilo customizado para a largura da barra lateral
st.markdown("""
    <style>
    .css-1d391kg {
        width: 200px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Título do aplicativo
st.title('🌟  Mapeamento de Conceitos sobre Culinária e Meios de Subsistência dos Tupinambá de Olivença 🌟')

# Barra lateral para seleção de termo e outras opções
st.sidebar.header('Opções de Exploração')
selected_term = st.sidebar.selectbox('Selecione um Termo:', df['Conceito'].unique())

# Adicionar a imagem típica da cultura Tupinambá na parte inferior da barra lateral
st.sidebar.image('https://imgs.search.brave.com/sBOhv8CMzJwXZJGc0hpuZZEjsgX_H7miZpxN5ADhyh0/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9zdGF0/aWMucHJlcGFyYWVu/ZW0uY29tLzIwMjIv/MDgvcG92b3MtaW5k/aWdlbmFzLWJyYXNp/bC5qcGc', use_column_width=True)

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
    # A mensagem de dados não disponíveis foi removida

else:
    st.write("Termo não encontrado.")

# Mostrar a tabela completa no final
st.write('### Tabela Completa')
st.dataframe(df)
