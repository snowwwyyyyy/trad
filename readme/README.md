
# Double Bottom Trading Strategy with ATR Risk Management

Algorithmic trading system that detects double bottom chart patterns on EUR/USD forex data and backtests performance using ATR-based stops and 2.5:1 risk-reward ratios.

Built as part of quantitative finance learning for fintech internship applications.

## Strategy Overview

**Core Logic:**
- Detect double bottom patterns at key support levels
- Enter on neckline breakout confirmation
- Exit with ATR-based stops and fixed 2.5:1 risk-reward

**Risk Management:**
- Stop Loss: Second bottom low - ATR(14)
- Target: Entry + 2.5 × Risk
- Position Sizing: 1% capital risk per trade

## Technical Pipeline

1. **Data Acquisition**: Historical EUR/USD data (2018-2024) via yfinance
2. **Feature Engineering**: ATR calculation, support/resistance detection from pivot points
3. **Pattern Recognition**: Double bottom detection with 4-stage filter:
   - Two lows within 8% price tolerance
   - Significant peak between bottoms
   - Second low near historical support
   - Neckline breakout within 3 candles
4. **Backtesting Engine**: Simulates trade execution, tracks P&L

## Backtest Results

| Metric | Value |
|--------|-------|
| Period | 2018-2024 |
| Total Signals | 279 |
| Completed Trades | 125 |
| Win Rate | **20.80%** |
| Wins | 26 |
| Losses | 99 |
| Total P&L | -0.423 |
| Average Win | +0.0419 |
| Average Loss | -0.0153 |
| Profit Factor | **0.72** |

## Key Findings

**What Worked:**
- ATR-based stops effectively adapted to market volatility
- Modular code structure enables rapid parameter iteration
- Backtesting framework accurately simulates historical performance

**What Didn't Work:**
- 20.8% win rate insufficient for 2.5:1 R:R (breakeven ≈ 29%)
- Pattern-only approach lacks context (trend, volume, macro conditions)
- Forex mean-reversion patterns may require shorter timeframes

**Lessons Learned:**
- Pure technical pattern trading requires additional confluence factors
- Risk management framework matters more than pattern accuracy
- Quantitative validation prevents emotional/biased strategy development

## Project Structure

## Tech Stack

- **Python 3.11**
- **pandas** - Data manipulation
- **numpy** - Numerical computation
- **scipy** - Signal processing for pattern detection
- **yfinance** - Market data API

## Installation & Usage

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/algo-trading-double-bottom.git
cd algo-trading-double-bottom

# Install dependencies
pip install -r requirements.txt

# Run backtest
python src/main.py
```

## Future Enhancements

- [ ] Multi-timeframe confirmation (daily pattern + 4H trend)
- [ ] Trend filter (50/200 EMA) to avoid counter-trend trades
- [ ] Volume analysis for breakout validation
- [ ] Machine learning classifier for pattern quality scoring
- [ ] Real-time paper trading via Alpaca/Zerodha API
- [ ] Monte Carlo simulation for parameter robustness testing

## Academic Context

Developed to demonstrate:
- Quantitative strategy development workflow
- Python proficiency in financial applications
- Understanding of risk-adjusted performance metrics
- Ability to iterate based on empirical results

Intended for educational purposes and internship portfolio demonstration (JPMC Summer Analyst application).

## Disclaimer

This project is for educational purposes only. Past performance does not guarantee future results. Do not use this strategy with real capital without proper due diligence and risk assessment.



*Built with focus on clean code, reproducible research, and honest evaluation of strategy performance.*