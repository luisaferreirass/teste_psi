import streamlit as st
from perguntas import perguntas_temp


respostas_analisadas = {
    "Colérico": 0,
    "Sanguíneo": 0,
    "Melancólico": 0,
    "Fleumático": 0
}

colerico ={ 1, 3, 5, 8, 11, 14, 15, 25, 30, 36, 37, 38, 42, 43, 44, 50, 53,
54, 56, 60, 66, 67, 73, 81, 83, 84, 86, 90, 92, 96, 105, 108, 112, 115,
116, 117, 118, 121, 123, 124, 125, 127, 130, 132, 133, 134, 135, 138,
140, 143, 144, 154, 155, 156, 157, 158, 167, 168, 172, 176, 177, 183,
191, 192, 194, 196, 200, 207, 209, 213, 218, 219, 222, 224, 227}

sanguineo = {1, 3, 5, 9, 10, 11, 14, 17, 18, 23, 26, 29, 30, 32, 36, 37, 38,
41, 43, 46, 47, 48, 49, 50, 56, 59, 68, 69, 71, 76, 77, 79, 80, 82, 87,
89, 91, 92, 93, 94, 95, 104, 107, 110, 112, 113, 114, 116, 117, 118,
120, 121, 129, 131, 136, 138, 139, 142, 144, 145, 146, 148, 149, 152,
157, 159, 160, 161, 175, 178, 179, 180, 203, 206, 212, 214, 220, 223,
226, 228, 230, 231}

melancolico = {2, 7, 8, 12, 13, 16, 19, 20, 21, 22, 24, 27, 28, 31, 33, 34,
39, 40, 42, 48, 51, 52, 54, 57, 62, 63, 70, 72, 73, 74, 75, 78, 79, 80,
81, 88, 98, 99, 101, 106, 109, 111, 122, 131, 133, 141, 150, 151, 153,
159, 163, 165, 166, 170, 173, 176, 181, 182, 184, 186, 187, 190, 193,
197, 202, 204, 208, 210, 215, 216, 221, 222, 227}

fleumatico = {2, 4, 6, 9, 10, 21, 26, 28, 30, 31, 35, 39,45, 52, 55, 58,61,
63, 64, 65, 68, 70, 72, 75, 78, 85, 88, 97, 98, 100, 102, 103, 106, 107,
110, 111, 113, 119, 122, 126, 128, 129, 131, 137, 139, 147, 153, 160,
162, 166, 169, 171, 173, 174, 175, 185, 186, 188, 189, 195, 198, 199,
201, 204, 205, 206, 210, 211, 215, 217, 219, 221, 225, 226, 228, 232}

def check_empate(ranking):
    empatados = []
    maior = ranking[0][1]
    for i in range(len(ranking)):
        if ranking[i][1] == maior:
            empatados.append(ranking[i])
    return empatados

st.title("Indicador de temperamento")
st.write(
    "Marque todas as afirmações abaixo com as quais você se identifica. "
    "Ao terminar, clique em **Ver resultado**."
)

def arm_resposta(numero):
    if numero in colerico:
        respostas_analisadas["Colérico"] += 1
    elif numero in sanguineo:
        respostas_analisadas["Sanguíneo"] += 1
    elif  numero in melancolico:
        respostas_analisadas["Melancólico"] += 1
    elif  numero in fleumatico:
        respostas_analisadas["Fleumático"] += 1


for i, pergunta in enumerate(perguntas_temp):
    num = i + 1
    marcado = st.checkbox(pergunta, key=f"q_{i+1}")
    if marcado:
        arm_resposta(num)

if st.button("Ver resultado"):

    ranking = sorted(respostas_analisadas.items(), key=lambda x: x[1], reverse=True)

    st.subheader("Pontuação:")
    for temp, valor in ranking:
        st.write(f"**{temp}:** {valor}")

    empate = check_empate(ranking)

    st.divider()
    if len(empate) > 1:
        st.write(f"Você possui **{len(empate)} temperamentos primários:**")
        for temp, _ in empate:
            st.write(f"• {temp}")
    else:
            st.success(f"Temperamento principal: **{ranking[0][0]}**")