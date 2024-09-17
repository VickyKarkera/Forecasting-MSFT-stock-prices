![image](https://github.com/user-attachments/assets/bbdfff95-45cc-4d3b-9653-5829c66df772)

# Time Series Analysis on Microsoft Stock Data

This project analyzes Microsoft's stock data using time series techniques. The following are methods I used and their intended purpose:

Seasonal Decomposition - To see the patterns inside the data broken down into - trend, seasonality, and Residuals

Differencing data - first and logarithmic - to make the data stationary for use by ARIMA models

Auto Correlation Function and Partial Auto Correlation Function plots - to see stationarity and get hyperparameters for ARIMA model

Augmented Dickey Fuller test - to see stationarity of data using statistical measure, after visual inspection (via ACF)

Autoregressive Integrated Moving Average - to build predictive model

Exponential Smoothing ETS (Error Trend Season) - to build predictive model without the need for applying techniques to make data stationary

The goal is to predict future stock prices and evaluate model performance.

## Overview
- Dataset: Monthly average stock prices of Microsoft from 01/01/2024 to 08/31/2024.
- Techniques: Time series Trend Seasonal Error decomposition, ARIMA, Exponential Smoothing ETS.
- Key Findings: ARIMA model with simple first differencing proved to be better for our use case in comparison to the other more complex techniques.

## Technologies Used
- Python (Pandas, NumPy, Matplotlib)
- ARIMA, ExponentialSmoothing
