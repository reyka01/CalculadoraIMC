#imc

import streamlit as st

st.title('Calculadora de IMC')

peso = st.number_input('Digite seu peso: ', min_value=0.0, format="%.2f")
altura = st.number_input('Digite sua altura: ', min_value=0.0, format="%.2f")

if peso > 0 and altura > 0:
    imc = peso / (altura ** 2)
    st.write('Seu IMC é: {:.2f}'.format(imc))

    if imc >= 18.5 and imc < 25:
        st.write('Você está no peso ideal.')
    elif imc >= 25:
        st.write('Você está na acima do peso.')
    else:
        st.write('Você está abaixo do peso.')

else:
    st.write('Preencha peso e altura para calcular o IMC.')