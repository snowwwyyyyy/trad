import yfinance as yf
import pandas as pd

def download_stock_data(ticker, start_date, end_date):
    """Download forex data from yfinance"""
    df = yf.download(ticker, start=start_date, end=end_date, interval="1d")
    df.columns = df.columns.get_level_values(0)  # flatten multiindex
    return df

def calculate_atr(df, period=14):
    """Calculate Average True Range"""
    high = df['High'].squeeze()
    low = df['Low'].squeeze()
    close = df['Close'].squeeze()
    
    tr1 = high - low
    tr2 = (high - close.shift(1)).abs()
    tr3 = (low - close.shift(1)).abs()
    
    tr = pd.DataFrame({'tr1': tr1, 'tr2': tr2, 'tr3': tr3}).max(axis=1)
    df['ATR'] = tr.rolling(window=period).mean()
    return df