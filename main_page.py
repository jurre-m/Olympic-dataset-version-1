import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns












"""
Hello, this is page 1. 
"""

data = [
    (2016, "Rio de Janeiro", -22.9068,  -43.1729),
    (2000, "Sydney",         -33.8688,  151.2093),
    (1996, "Atlanta",         33.7490,  -84.3880),
    (2008, "Beijing",         39.9042,  116.4074),
    (2004, "Athens",          37.9838,   23.7275),
    (2012, "London",          51.5074,   -0.1278),
    (1992, "Barcelona",       41.3874,    2.1686),
    (1988, "Seoul",           37.5665,  126.9780),
    (1972, "Munich",          48.1351,   11.5820),
    (1984, "Los Angeles",     34.0522, -118.2437),
    (1976, "Montreal",        45.5017,  -73.5673),
    (1968, "Mexico City",     19.4326,  -99.1332),
    (1980, "Moscow",          55.7558,   37.6173),
]

df_world = pd.DataFrame(data, columns=["year", "city", "lat", "lon"]).sort_values("year")
df_world["label"] = df_world["year"].astype(str) + " " + df_world["city"]

fig = px.scatter_geo(
    df_world,
    lat="lat",
    lon="lon",
    text="label",
    hover_name="city",
    hover_data={"year": True, "lat": False, "lon": False, "label": False},
    color="year",
    color_continuous_scale="Viridis",
    projection="natural earth",
)

fig.update_traces(
    marker=dict(size=10, line=dict(width=1.0, color="black")),
    textfont=dict(size=10, color="black"),
    textposition="top center",
)
fig.update_geos(showcountries=True, showland=True, landcolor="rgb(235,235,235)")
fig.update_layout(title="Olympic host cities 1968–2016", margin=dict(l=0, r=0, t=40, b=0))

st.plotly_chart(fig)
