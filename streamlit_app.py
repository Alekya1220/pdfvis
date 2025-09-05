import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

st.title("📊 1D, 2D, 3D Visualization App")

# Sample data
np.random.seed(42)
df = pd.DataFrame({
    "X": np.random.randn(100),
    "Y": np.random.randn(100),
    "Z": np.random.randn(100) * 10,
})

st.write("### Data Preview")
st.write(df.head())

# Sidebar selection
viz_type = st.sidebar.selectbox("Choose Visualization Type", ["1D", "2D", "3D"])

# 1D
if viz_type == "1D":
    plot_type = st.sidebar.selectbox("Choose 1D Plot", ["Histogram", "Line", "Bar"])
    col = st.sidebar.selectbox("Select Column", df.columns)

    fig, ax = plt.subplots()
    if plot_type == "Histogram":
        ax.hist(df[col], bins=20, color="skyblue", edgecolor="black")
    elif plot_type == "Line":
        ax.plot(df[col], marker="o")
    elif plot_type == "Bar":
        ax.bar(df.index, df[col], color="orange")
    st.pyplot(fig)

# 2D
elif viz_type == "2D":
    plot_type = st.sidebar.selectbox("Choose 2D Plot", ["Scatter", "Box"])
    x_col = st.sidebar.selectbox("X-axis", df.columns)
    y_col = st.sidebar.selectbox("Y-axis", df.columns)

    fig, ax = plt.subplots()
    if plot_type == "Scatter":
        ax.scatter(df[x_col], df[y_col], c="red", alpha=0.6)
    elif plot_type == "Box":
        df[[x_col, y_col]].plot(kind="box", ax=ax)
    st.pyplot(fig)

# 3D
elif viz_type == "3D":
    plot_type = st.sidebar.selectbox("Choose 3D Plot", ["3D Scatter", "3D Surface"])
    x_col = st.sidebar.selectbox("X-axis", df.columns)
    y_col = st.sidebar.selectbox("Y-axis", df.columns)
    z_col = st.sidebar.selectbox("Z-axis", df.columns)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    if plot_type == "3D Scatter":
        ax.scatter(df[x_col], df[y_col], df[z_col], c="blue", alpha=0.6)
    elif plot_type == "3D Surface":
        X, Y = np.meshgrid(df[x_col], df[y_col])
        Z = np.sin(X) + np.cos(Y)
        ax.plot_surface(X, Y, Z, cmap="viridis")
    st.pyplot(fig)
