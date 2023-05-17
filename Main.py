import streamlit as st
from streamlit_option_menu import option_menu
import BSE

st.title('BSE Simulator')

st.sidebar.radio('Select the type of simulation', ('Single', 'Multiple'))