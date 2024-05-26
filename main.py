import streamlit as st
import backend

st.title(backend.title)

st.image(backend.image_filepath)

st.write(backend.explanation)