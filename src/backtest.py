import numpy as np

def calculate_trade_levels(signals, df):
    """Calculate stop loss and target for each signal"""
    trades = []
    
    for signal in signals:
        entry = signal['entry']
        low2 = signal['low2']
        date = signal['date']
        
        atr = df.loc[date, 'ATR']
        stop = low2 - atr
        risk = entry - stop
        target = entry + 2.5 * risk
        
        trades.append({
            'date': date,
            'entry': entry,
            'stop': stop,
            'target': target,
            'risk': risk,
            'reward': target - entry,
            'rr_ratio': (target - entry) / risk if risk != 0 else 0
        })
    
    return trades

def backtest_trades(trades, df):
    """Simulate trades and determine outcomes"""
    results = []
    
    for trade in trades:
        if np.isnan(trade['stop']):
            continue
            
        entry_date = trade['date']
        entry_idx = df.index.get_loc(entry_date)
        
        for i in range(1, 50):
            if entry_idx + i >= len(df):
                break
            
            high = df['High'].iloc[entry_idx + i]
            low = df['Low'].iloc[entry_idx + i]
            
            if high >= trade['target']:
                results.append({
                    'entry_date': entry_date,
                    'exit_date': df.index[entry_idx + i],
                    'outcome': 'WIN',
                    'pnl': trade['reward']
                })
                break
            
            if low <= trade['stop']:
                results.append({
                    'entry_date': entry_date,
                    'exit_date': df.index[entry_idx + i],
                    'outcome': 'LOSS',
                    'pnl': -trade['risk']
                })
                break
    
    return results

def print_results(results):
    """Print backtest performance metrics"""
    if not results:
        print("No completed trades")
        return
    
    wins = [r for r in results if r['outcome'] == 'WIN']
    losses = [r for r in results if r['outcome'] == 'LOSS']
    
    win_rate = len(wins) / len(results) * 100
    total_pnl = sum([r['pnl'] for r in results])
    avg_win = np.mean([r['pnl'] for r in wins]) if wins else 0
    avg_loss = np.mean([r['pnl'] for r in losses]) if losses else 0
    profit_factor = abs(sum([r['pnl'] for r in wins]) / sum([r['pnl'] for r in losses])) if losses else 0
    
    print(f"\n=== Backtest Results ===")
    print(f"Total Trades: {len(results)}")
    print(f"Wins: {len(wins)}")
    print(f"Losses: {len(losses)}")
    print(f"Win Rate: {win_rate:.2f}%")
    print(f"Total P&L: {total_pnl:.5f}")
    print(f"Average Win: {avg_win:.5f}")
    print(f"Average Loss: {avg_loss:.5f}")
    print(f"Profit Factor: {profit_factor:.2f}")