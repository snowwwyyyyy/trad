from scipy.signal import argrelextrema
import numpy as np
from src.indicators import is_near_support

def detect_double_bottom(df, support_levels, order=1, tolerance=0.08):
    """Detect double bottom patterns with support confluence"""
    close = df['Close'].values
    low = df['Low'].values
    
    pivot_lows = argrelextrema(close, np.less, order=order)[0]
    signals = []
    
    for i in range(1, len(pivot_lows)):
        idx1 = pivot_lows[i-1]
        idx2 = pivot_lows[i]
        
        low1 = low[idx1]
        low2 = low[idx2]
        
        # Condition 1: two lows within tolerance
        if abs(low1 - low2) / low1 > tolerance:
            continue
            
        # Condition 2: peak in between
        peak_between = close[idx1:idx2].max()
        if peak_between < low1 * 0.8:
            continue
        
        # Condition 3: near support
        if not is_near_support(low2, support_levels, tolerance):
            continue
        
        # Condition 4: neckline breakout
        neckline = peak_between
        breakout_idx = None
        for j in range(1, 3):
            if idx2 + j < len(close):
                if close[idx2 + j] > neckline:
                    breakout_idx = idx2 + j
                    break
        
        if breakout_idx is None:
            continue
        
        signals.append({
            'date': df.index[breakout_idx],
            'entry': close[breakout_idx],
            'low1': low1,
            'low2': low2,
            'neckline': neckline
        })
    
    return signals