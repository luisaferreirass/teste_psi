import streamlit as st
from perguntas import perguntas_mul

LINGUAGENS = {
    "A": "💬 Palavras de Afirmação",
    "B": "⏳ Tempo de Qualidade",
    "C": "🎁 Presentes",
    "D": "🤝 Atos de Serviço",
    "E": "🤗 Toque Físico",
}

def calcular_pontuacao(respostas_selecionadas: list) -> dict:
    contagem = {k: 0 for k in LINGUAGENS}
    for letra in respostas_selecionadas:
        if letra in contagem:
            contagem[letra] += 1
    return contagem

def check_empate(ranking):
    maior = ranking[0][1]
    return [(t, v) for t, v in ranking if v == maior]


# ── Header ────────────────────────────────────────────────────────────────────
st.title("💑 Linguagens do Amor")
st.markdown(
    "Para cada par de afirmações abaixo, escolha aquela que **mais se aplica a você**."
)
st.divider()

# ── Perguntas ─────────────────────────────────────────────────────────────────
respostas_selecionadas = []

for i, pergunta in enumerate(perguntas_mul):
    opcoes_texto = list(pergunta.keys())

    st.markdown(f"**{i + 1} de {len(perguntas_mul)}**")
    escolha = st.radio(
        label=f"pergunta_{i}",
        options=opcoes_texto,
        index=None,             # nenhuma pré-selecionada
        label_visibility="collapsed",
        key=f"q_{i}"
    )

    respostas_selecionadas.append(pergunta[escolha] if escolha else None)
    st.divider()

# ── Botão ─────────────────────────────────────────────────────────────────────
respondidas = sum(1 for r in respostas_selecionadas if r is not None)
total = len(perguntas_mul)

st.markdown(f"Respondidas: **{respondidas} / {total}**")

if respondidas < total:
    st.info("Responda todas as perguntas para ver seu resultado.")

if st.button("Ver resultado ➜", disabled=respondidas < total, use_container_width=True):

    contagem = calcular_pontuacao(respostas_selecionadas)
    ranking = sorted(contagem.items(), key=lambda x: x[1], reverse=True)
    empate = check_empate(ranking)

    st.divider()
    st.subheader("Seu resultado")

    # Barra de progresso para cada linguagem
    for letra, valor in ranking:
        nome = LINGUAGENS[letra]
        percentual = valor / total
        st.markdown(f"**{nome}**  —  {valor} ponto{'s' if valor != 1 else ''}")
        st.progress(percentual)

    st.divider()

    if len(empate) > 1:
        nomes = " e ".join(LINGUAGENS[l] for l, _ in empate)
        st.success(f"Você possui **{len(empate)} linguagens primárias:** {nomes}")
    else:
        st.success(f"Sua linguagem primária é: **{LINGUAGENS[ranking[0][0]]}**")