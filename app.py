import streamlit as st
import pandas as pd

# Configuração da Página
st.set_page_config(page_title="Treino do Leo", page_icon="💪")

# Título e Estilo
st.title("🏋️‍♂️ Plano de Treino - Leonnardo")
st.write("Descanso sugerido: **60–90 segundos**")

# Estrutura dos Treinos
treinos = {
    "TREINO A — PEITO + TRÍCEPS": [
        ("Supino Máquina", "4x 8–12", "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueGZ4eGZ4&ep=v1_gifs_search&rid=giphy.gif"),
        ("Supino Inclinado", "3x 10–12", ""),
        ("Peck Deck", "3x 12–15", ""),
        ("Tríceps Barra", "3x 10–12", ""),
        ("Tríceps Corda", "3x 12–15", "")
    ],
    "TREINO B — COSTAS + BÍCEPS": [
        ("Puxada Frente", "4x 8–12", ""),
        ("Remada Máquina", "4x 10–12", ""),
        ("Remada Baixa", "3x 10–12", ""),
        ("Rosca Barra", "3x 10–12", ""),
        ("Rosca Martelo", "3x 12", "")
    ],
    "TREINO C — PERNAS + OMBRO": [
        ("Leg Press", "4x 10–12", ""),
        ("Cadeira Extensora", "3x 12–15", ""),
        ("Mesa Flexora", "3x 10–12", ""),
        ("Stiff", "4x 8–12", ""),
        ("Abdutora", "3x 12–15", ""),
        ("Adutora", "3x 12–15", ""),
        ("Panturrilha", "3x 15–20", ""),
        ("Elevação Lateral", "3x 12–15", "")
    ]
}

# Seleção do Treino do Dia
opcao_treino = st.selectbox("Escolha o Treino:", list(treinos.keys()))

# Exibição dos Exercícios
st.subheader(f"Lista de Exercícios: {opcao_treino}")

for exercicio, series, link_video in treinos[opcao_treino]:
    with st.expander(f"📌 {exercicio} ({series})"):
        col1, col2 = st.columns([1, 1])
        
        with col1:
            carga = st.number_input(f"Carga (kg) - {exercicio}", min_value=0, key=f"carga_{exercicio}")
            reps = st.number_input(f"Reps Feitas - {exercicio}", min_value=0, key=f"reps_{exercicio}")
        
        with col2:
            obs = st.text_area(f"Observações - {exercicio}", key=f"obs_{exercicio}")
            
        if st.button(f"Salvar Série de {exercicio}"):
            st.success(f"Registrado: {carga}kg | {reps} reps")

# Rodapé de Saúde
st.divider()
st.info("💡 Lembrete: Mantenha a postura e hidrate-se. Se sentir desconforto abdominal (gases), evite prender a respiração durante o esforço (manobra de valsalva).")
