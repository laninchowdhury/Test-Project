import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import numpy as np
import scipy.special as sp

# Read the dataset's csv file
df =pd.read_csv(r"C:\Users\nsuka\Desktop\Project\vehicles_us.csv")

# Add a header
st.header("Car Analysis Dashboard")

# Plotly Express Histogram
fig_hist = px.histogram(df, x='price', title='Price Distribution')
st.plotly_chart(fig_hist)

# Plotly Express Scatter Plot
fig_scatter = px.scatter(df, x='odometer', y='price', color='condition', title='Price vs Odometer')
st.plotly_chart(fig_scatter)

# Checkbox to filter data
if st.checkbox('Show only SUVs'):
    df = df[df['type'] == 'suv']
    st.write(df)