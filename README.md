Financial News and Stock Data Analysis
This project involves a comprehensive analysis of financial news headlines and historical stock market data. It combines natural language processing (NLP) techniques with quantitative financial analysis to extract insights from textual data and identify patterns in stock performance.

Table of Contents
Introduction
Data Sources
Analysis Steps
Descriptive Statistics
Text Analysis (Keyword & Topic Modeling)
Time Series Analysis of News Volume
Publisher Analysis
Quantitative Analysis of Stock Data (AAPL)
Data Preparation
Technical Indicators with TA-Lib
Additional Financial Metrics with PyNance
Libraries Used
Introduction
This notebook demonstrates a workflow for analyzing financial news and correlating it with stock market data. It covers various aspects from initial data loading and cleaning to advanced NLP for text insights and quantitative analysis for financial metrics and technical indicators.

Data Sources
raw_analyst_ratings.csv: Contains financial news headlines, URLs, publishers, dates, and associated stock tickers.
Stock Data CSVs (e.g., AAPL.csv, AMZN.csv, GOOG.csv, META.csv, NVDA.csv): Historical daily stock price data (Open, High, Low, Close, Volume) for several major technology companies.
Analysis Steps
Descriptive Statistics
Performed initial descriptive analysis on the df_news DataFrame:

Calculated headline character count distribution.
Identified the most active publishers.
Analyzed publication date trends (articles per day).
Text Analysis (Keyword & Topic Modeling)
Applied NLP techniques to financial news headlines:

Common Keywords: Used CountVectorizer to identify and list the top 20 most frequent keywords after removing stop words.
Topic Modeling (LDA): Employed LatentDirichletAllocation to extract significant topics and their defining keywords from the headlines, using a sample for performance.
Time Series Analysis of News Volume
Examined news publication frequency over time:

Plotted daily news publication volume to observe trends.
Illustrated hourly news publication distribution to identify active publishing times.
Publisher Analysis
Investigated publisher contributions:

Identified the top 20 most active publishers by article count.
Extracted unique domains from email-like publisher names to understand organizational sources.
Quantitative Analysis of Stock Data (AAPL)
Focused on the df_AAPL dataset for in-depth financial analysis. (Similar steps are pending for AMZN, GOOG, META, NVDA).

Data Preparation
Converted the 'Date' column to datetime objects and set it as the DataFrame index.
Ensured all relevant financial columns (Open, High, Low, Close, Volume) were numeric.
Handled missing values using forward-fill and then dropping any remaining NaN rows.
Technical Indicators with TA-Lib
Calculated and visualized several standard technical indicators:

Simple Moving Average (SMA): 20-day and 50-day.
Exponential Moving Average (EMA): 20-day and 50-day.
Relative Strength Index (RSI): 14-day period.
Moving Average Convergence Divergence (MACD): Standard 12, 26, 9 periods.
Bollinger Bands: 20-day period.
Plots were generated to visualize close prices with moving averages and Bollinger Bands, RSI, and MACD separately.

Additional Financial Metrics with PyNance
Utilized the pynance library (and some manual calculations for clarity) to derive more financial metrics:

Daily Return: Percentage change in daily closing prices.
Annual Volatility: 20-day rolling annualized standard deviation of daily returns.
Cumulative Return: The product of (1 + daily return) over time.
Plots were created to visualize the Annual Volatility and Cumulative Return.

Libraries Used
pandas
numpy
matplotlib.pyplot
seaborn
sklearn (for CountVectorizer, LatentDirichletAllocation, TfidfVectorizer)
talib (for technical indicators)
pynance (for additional financial metrics)
re (for regular expressions in publisher analysis)