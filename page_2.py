import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
import requests

st.title("Data exploration and preparation")

st.subheader("We started with data from 3 different datasets")

st.markdown("The first dataset holds information on participants in Olympic games. It holds 70.000 rows and 15 columns.",
            "The second dataset is mainly a key to convert Olympic country codes into corresponding country names (like 'GER' into 'Germany')",
            "Both can be found on https://www.kaggle.com/datasets/bhanupratapbiswas/olympic-data")
st.markdown("The third dataset holds demographic data. It has 234 rows and 17 columns.",
            "Can be found on https://www.kaggle.com/datasets/tanishqdublish/world-data-population")



# st.header("Driving question:")

# st.subheader("From our dataset we noticed that inhabitants of different countries or continents do not have equal chances to participate in the Olympic games.")





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


