import yfinance as yf
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

# Fetch Microsoft stock data from 2014 to 2024
ticker = 'MSFT'
msft_data = yf.download(ticker, start="2014-01-01", end="2024-08-31")

# Resample data to monthly and calculate average closing price
msft_monthly = msft_data['Close'].resample('M').mean()

# Convert to a DataFrame
msft_monthly_df = pd.DataFrame({'Date': msft_monthly.index, 'Average Monthly Close': msft_monthly.values})

# Save to an Excel file
msft_monthly_df.to_excel('Microsoft_Stock_Data.xlsx', index=False)

print("Data exported to Excel successfully!")
