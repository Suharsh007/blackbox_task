import pandas as pd
import numpy as np

# Load the trade log data from the CSV file
trade_log = pd.read_csv('tradelog.csv')

# Define the initial portfolio value and risk-free interest rate
initial_portfolio_value = 6500
risk_free_rate = 0.05

# Parameter 1: Total Trades
total_trades = len(trade_log)

# Parameter 2: Profitable Trades
profitable_trades = len(trade_log[(trade_log['Exit Price']-trade_log['Entry Price']) > 0])

# Parameter 3: Loss-Making Trades
loss_making_trades = len(trade_log[(trade_log['Exit Price']-trade_log['Entry Price']) < 0])

# Parameter 4: Win Rate
win_rate = profitable_trades / total_trades

# Parameter 5: Average Profit per Trade
average_profit_per_trade = (trade_log['Exit Price']-trade_log['Entry Price']).mean()

# Parameter 6: Average Loss per Trade
average_loss_per_trade = (trade_log['Exit Price']-trade_log['Entry Price'])[(trade_log['Exit Price']-trade_log['Entry Price']) < 0].mean()

# Parameter 7: Risk Reward Ratio
risk_reward_ratio = -average_profit_per_trade / average_loss_per_trade

# Parameter 8: Expectancy
loss_rate = 1 - win_rate
expectancy = (win_rate * average_profit_per_trade) - (loss_rate * average_loss_per_trade)

# Parameter 9: Average ROR per Trade
# Calculate daily returns (assuming daily data)
daily_return = (trade_log['Exit Price'] / trade_log['Entry Price']) - 1
adjusted_daily_return = daily_return - (risk_free_rate / total_trades)
average_ror_per_trade = adjusted_daily_return.mean() / adjusted_daily_return.std()

# Parameter 10: Sharpe Ratio
sharpe_ratio = (average_ror_per_trade - risk_free_rate) / daily_return.std()

# Parameter 11: Max Drawdown
cumulative_returns = (1 + daily_return).cumprod()
peak_values = cumulative_returns.cummax()
drawdown = cumulative_returns - peak_values
max_drawdown = drawdown.min()
max_drawdown_percentage = (max_drawdown / initial_portfolio_value) * 100


# Parameter 12: Max Drawdown Percentage
max_drawdown_percentage = (max_drawdown / initial_portfolio_value) * 100

# Parameter 13: CAGR (Compound Annual Growth Rate)
cagr = (cumulative_returns.iloc[-1] / cumulative_returns.iloc[0]) ** (1 / total_trades) - 1

# Parameter 14: Calmar Ratio
calmar_ratio = cagr / max_drawdown_percentage

# Print the calculated parameters
print("Total Trades:", total_trades)
print("Profitable Trades:", profitable_trades)
print("Loss-Making Trades:", loss_making_trades)
print("Win Rate:", win_rate)
print("Average Profit per Trade:", average_profit_per_trade)
print("Average Loss per Trade:", average_loss_per_trade)
print("Risk Reward Ratio:", risk_reward_ratio)
print("Expectancy:", expectancy)
print("Average ROR per Trade:", average_ror_per_trade)
print("Sharpe Ratio:", sharpe_ratio)
print("Max Drawdown:", max_drawdown)
print("Max Drawdown Percentage:", max_drawdown_percentage)
print("CAGR:", cagr)
print("Calmar Ratio:", calmar_ratio)
