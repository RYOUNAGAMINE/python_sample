import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('Display Image')

if st.checkbox('Show Image'):
  image = Image.open("S__21364751.jpg")
  st.image(image, caption='Mituba Mitu', use_column_width=True)