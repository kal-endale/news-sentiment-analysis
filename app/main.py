import streamlit as st
from utils import (
    load_data,
    filter_data,
    plot_temperature_trend,
    plot_precipitation_boxplot,
    plot_variable_trend,
    plot_correlation_heatmap
)

# -----------------------------------
# Page config
# -----------------------------------
st.set_page_config(
    page_title="African Climate Dashboard",
    layout="wide"
)

st.title("African Climate Trends Dashboard")
st.markdown("""
This dashboard analyzes climate trends across:

- Ethiopia  
- Kenya  
- Nigeria  
- Sudan  
- Tanzania  

The analysis supports climate vulnerability insights for COP32 preparation.
""")

# -----------------------------------
# Load data
# -----------------------------------
df = load_data()

# -----------------------------------
# Sidebar filters
# -----------------------------------
st.sidebar.header("Dashboard Filters")

countries = st.sidebar.multiselect(
    "Select Countries",
    options=df["Country"].unique(),
    default=df["Country"].unique()
)

min_year = int(df["YEAR"].min())
max_year = int(df["YEAR"].max())

year_range = st.sidebar.slider(
    "Select Year Range",
    min_year,
    max_year,
    (min_year, max_year)
)

variable = st.sidebar.selectbox(
    "Select Climate Variable",
    [
        "T2M",
        "PRECTOTCORR",
        "RH2M",
        "WS2M",
        "T2M_MAX",
        "T2M_MIN"
    ]
)

# -----------------------------------
# Filter data
# -----------------------------------
filtered_df = filter_data(df, countries, year_range)

# -----------------------------------
# Show dataset preview
# -----------------------------------
st.subheader("Dataset Preview")
st.dataframe(filtered_df.head())

# -----------------------------------
# Key metrics
# -----------------------------------
st.subheader("Summary Metrics")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Temperature",
    f"{filtered_df['T2M'].mean():.2f} °C"
)

col2.metric(
    "Average Rainfall",
    f"{filtered_df['PRECTOTCORR'].mean():.2f} mm"
)

col3.metric(
    "Average Humidity",
    f"{filtered_df['RH2M'].mean():.2f}%"
)

# -----------------------------------
# Charts
# -----------------------------------
plot_temperature_trend(filtered_df)

plot_precipitation_boxplot(filtered_df)

plot_variable_trend(filtered_df, variable)

plot_correlation_heatmap(filtered_df)

# -----------------------------------
# Footer
# -----------------------------------
st.markdown("---")
st.write("Built for 10 Academy Week 0 Climate Challenge")