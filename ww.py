import streamlit as st
import pandas as pd # pip install pandas
from matplotlib import pyplot as plt # pip install matplotlib
import time

plt.style.use("ggplot")




col = st.sidebar.selectbox('Select a Column',['A','B','C','D','E'])

