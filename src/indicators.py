from scipy.signal import argrelextrema
import numpy as np

def find_sr_levels(df, order=10):
    """Find support and resistance levels from pivot points"""
    close = df['Close'].squeeze().values
    
    pivot_highs = argrelextrema(close, np.greater, order=order)[0]
    pivot_lows = argrelextrema(close, np.less, order=order)[0]
    
    resistance_levels = close[pivot_highs]
    support_levels = close[pivot_lows]
    
    return support_levels, resistance_levels

def is_near_support(price, support_levels, tolerance=0.02):
    """Check if price is near a support level"""
    for level in support_levels:
        if abs(price - level) / level < tolerance:
            return True
    return False