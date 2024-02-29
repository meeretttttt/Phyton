# Streamlit hello world app
import streamlit as st
import numpy as np

def main():
    st.title('Hello World!')
    st.write('This is a simple hello world app in Streamlit.')
    st.write('To run this app, use the following command:')
    st.code('streamlit run hello_world.py')
    st.button("Reset", type="primary")
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
with st.chat_message("user"):
    st.write("Hello 👋")
    st.toast('Your edited image was saved!', icon="🎉")
    on = st.toggle('Activate feature')
    age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')
if on:
    st.write('Feature activated!')
agree = st.checkbox('I agree')
if agree:
    st.write('Great!')
    st.balloons()
option = st.selectbox(
    'Was ist Deine Lieblingsfarbe?',
    ('Blau', 'Grün', 'Pink'))
st.write('You selected:', option)
if __name__ == '__main__':
    main()
