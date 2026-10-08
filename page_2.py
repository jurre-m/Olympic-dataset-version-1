import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
import requests











"""
Hello, this is page 2
"""




url_1 = "https://raw.githubusercontent.com/jurre-m/Olympic-dataset-version-1/refs/heads/main/df_usable_case2.csv"

df = pd.read_csv(url_1)

resp = requests.get(url_1)
resp.raise_for_status()
df = pd.read_csv(io.StringIO(resp.text))


@st.cache_data
def load_data(url):
    return pd.read_csv(url)

df = load_data(url_1)
st.dataframe(df)


