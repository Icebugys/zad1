import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
wine_food_path = "/mnt/data/wine_food_pairings.csv"
wine_quality_path = "/mnt/data/winequality-red.csv"

@st.cache_data
def load_data():
    df_pair = pd.read_csv(wine_food_path)
    df_quality = pd.read_csv(wine_quality_path)
    return df_pair, df_quality

pairings, quality = load_data()

st.title("Wine Analysis & Pairing App")

st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Go to:", ["Wine Pairings", "Wine Quality Analysis"])

if page == "Wine Pairings":
    st.header("Wine & Food Pairings")

    st.write("Dataset preview:")
    st.dataframe(pairings.head())

    wine_types = pairings['wine'].unique()
    selected_wine = st.selectbox("Select wine type:", wine_types)

    filtered = pairings[pairings['wine'] == selected_wine]
    st.subheader(f"Recommended food for {selected_wine}:")
    st.dataframe(filtered)

elif page == "Wine Quality Analysis":
    st.header("Red Wine Quality Dataset")
    st.write("Dataset preview:")
    st.dataframe(quality.head())

    numeric_cols = quality.select_dtypes(include=['float64', 'int64']).columns
    selected_feature = st.selectbox("Feature to visualize:", numeric_cols)

    fig, ax = plt.subplots()
    ax.hist(quality[selected_feature].dropna(), bins=20)
    ax.set_title(f"Distribution of {selected_feature}")
    ax.set_xlabel(selected_feature)
    ax.set_ylabel("Count")

    st.pyplot(fig)
