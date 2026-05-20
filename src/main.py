from src.data_fetch import download_stock_data, calculate_atr
from src.indicators import find_sr_levels
from src.pattern_detection import detect_double_bottom
from src.backtest import calculate_trade_levels, backtest_trades, print_results

def main():
    # Parameters
    ticker = "EURUSD=X"
    start_date = "2018-01-01"
    end_date = "2024-01-01"
    
    # Fetch and prepare data
    print("Fetching data...")
    df = download_stock_data(ticker, start_date, end_date)
    df = calculate_atr(df)
    df.to_csv("data/eurusd_data.csv")
    
    # Find support/resistance
    print("Calculating S/R levels...")
    support, resistance = find_sr_levels(df)
    print(f"Support levels: {len(support)}, Resistance levels: {len(resistance)}")
    
    # Detect patterns
    print("Detecting double bottom patterns...")
    signals = detect_double_bottom(df, support)
    print(f"Signals found: {len(signals)}")
    
    # Backtest
    print("Running backtest...")
    trades = calculate_trade_levels(signals, df)
    trades = [t for t in trades if not np.isnan(t['stop'])]
    results = backtest_trades(trades, df)
    
    # Print results
    print_results(results)

if __name__ == "__main__":
    import numpy as np
    main()