import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import os


# -----------------------------------
# Load all country datasets
# -----------------------------------
@st.cache_data
def load_data():
    countries = [
        "ethiopia",
        "kenya",
        "nigeria",
        "sudan",
        "tanzania"
    ]

    dfs = []

    for country in countries:
        file_path = f"data/{country}_clean.csv"

        if os.path.exists(file_path):
            df = pd.read_csv(file_path)

            # Convert date column
            if "Date" in df.columns:
                df["Date"] = pd.to_datetime(df["Date"])

            dfs.append(df)

    combined_df = pd.concat(dfs, ignore_index=True)
    return combined_df


# -----------------------------------
# Filter dataframe
# -----------------------------------
def filter_data(df, selected_countries, year_range):
    filtered = df[
        (df["Country"].isin(selected_countries)) &
        (df["YEAR"] >= year_range[0]) &
        (df["YEAR"] <= year_range[1])
    ]

    return filtered


# -----------------------------------
# Temperature trend plot
# -----------------------------------
def plot_temperature_trend(df):
    st.subheader("Temperature Trend Over Time")

    monthly_temp = df.groupby("Date")["T2M"].mean().reset_index()

    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(monthly_temp["Date"], monthly_temp["T2M"])

    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Average Temperature Trend")

    st.pyplot(fig)


# -----------------------------------
# Rainfall distribution boxplot
# -----------------------------------
def plot_precipitation_boxplot(df):
    st.subheader("Precipitation Distribution by Country")

    fig, ax = plt.subplots(figsize=(10,5))

    sns.boxplot(
        data=df,
        x="Country",
        y="PRECTOTCORR",
        ax=ax
    )

    ax.set_ylabel("Precipitation (mm/day)")
    st.pyplot(fig)


# -----------------------------------
# Variable trend plot
# -----------------------------------
def plot_variable_trend(df, variable):
    st.subheader(f"{variable} Trend Over Time")

    trend_data = df.groupby("Date")[variable].mean().reset_index()

    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(trend_data["Date"], trend_data[variable])

    ax.set_xlabel("Date")
    ax.set_ylabel(variable)

    st.pyplot(fig)


# -----------------------------------
# Correlation heatmap
# -----------------------------------
def plot_correlation_heatmap(df):
    st.subheader("Correlation Heatmap")

    numeric_df = df.select_dtypes(include=["number"])

    corr = numeric_df.corr()

    fig, ax = plt.subplots(figsize=(10,6))

    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        ax=ax
    )
    
    st.pyplot(fig)