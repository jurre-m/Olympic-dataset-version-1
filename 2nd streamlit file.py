import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('df_usable.csv')                       # needs to be replaced by a github uploaded version.

# Define the pages
introduction = st.Page("main_page.py", title="Main Page", icon="🎈")
hypothesis = st.Page("page_2.py", title="Page 2", icon="❄️")
answer = st.Page("page_3.py", title="Page 3", icon="🎉")

# Set up navigation
pg = st.navigation([introduction, hypothesis, answer])

# Run the selected page
pg.run()

