import streamlit as st
import BSE
import data.contact as contact
import data.simulation as sim
import data.workshop as work
import data.about as about
import data.future as future



st.sidebar.title('BSE Simulator')

st.sidebar.markdown('# ')

if st.sidebar.button('About'):
    about.about();
if st.sidebar.button('Workshop'):
    st.write('Hello Workshop')
if st.sidebar.button('Simulation'):
    st.write('Hello Simulation')
if st.sidebar.button('Future'):
    st.write('Hello Contact')

st.sidebar.markdown('# ')
st.sidebar.markdown('# ')


with st.sidebar.expander('Contact'):
    st.button('Email', on_click=contact.email)
    st.button('LinkedIn', on_click=contact.linkedin)
    st.button('Portfolio', on_click=contact.portfolio)