import streamlit as st
import pandas as pd
from datetime import datetime
import socket

# Page title
st.title("Sales Dashboard")

# Read dataset
df = pd.read_csv("sales.csv")

# Show dataset
st.subheader("Sales Data")
st.dataframe(df)

# Total sales
st.subheader("Total Sales")
st.write(df["Sales"].sum())

# Total profit
st.subheader("Total Profit")
st.write(df["Profit"].sum())

# Sales chart
st.subheader("Monthly Sales Chart")
st.line_chart(df["Sales"])

# Profit chart
st.subheader("Monthly Profit Chart")
st.bar_chart(df["Profit"])

# Deployment info
st.subheader("Deployment Info")

st.write("Container ID:", socket.gethostname())

st.write("Deployment Time:", datetime.now())

st.success("Dashboard Deployment Successful using Jenkins + Docker")