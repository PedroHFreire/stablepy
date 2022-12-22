# import numpy as np

# from stablepy.return_metrics import calculate_returns, calculate_portfolio_returns, calculate_return_contribution, calculate_periodic_returns

# def generate_return_report(prices: np.ndarray, weights: np.ndarray, period: str):
#     """
#     Generate a report of the portfolio and asset returns.
    
#     Parameters:
#         prices: A 2D numpy array of asset prices, with rows representing different assets and columns representing time.
#         weights: A 1D numpy array of weights for the assets in the portfolio.
#         period: The period to calculate returns for. Can be "daily", "weekly", "monthly", or "yearly".
#     """
#     # Calculate asset returns
#     asset_returns = calculate_returns(prices, return_type="arithmetic")
    
#     # Calculate portfolio returns
#     portfolio_returns = calculate_portfolio_returns(asset_returns, weights)
    
#     # Calculate periodic returns
#     portfolio_periodic_returns = calculate_periodic_returns(portfolio_returns, period)
    
#     # Calculate return contributions
#     return_contributions = calculate_return_contribution(asset_returns, weights)
    
#     # Print report
#     print("Asset Returns:")
#     for i, asset_return in enumerate(asset_returns):
#         print(f" - Asset {i+1}: {asset_return:.2f}")
        
#     print(f"\nPortfolio Returns: {portfolio_returns:.2f}")
#     print(f"\nPeriodic Returns ({period}): {portfolio_periodic_returns:.2f}")
    
#     print("\nReturn Contributions:")
#     for i, return_contribution in enumerate(return_contributions):
#         print(f" - Asset {i+1}: {return_contribution:.2f}")

# # Generate random prices and weights
# num_assets = 3
# num_days = 252
# prices = np.random.rand(num_assets, num_days)
# weights = np.random.rand(num_assets)
# weights /= weights.sum()

# print(prices)
# print(weights)
# # Generate return report
# #generate_return_report(prices, weights, period="daily")

## Try again
import sqlite3

# Connect to the database
conn = sqlite3.connect('../risk-system-db/stable.db')

# Create a cursor
cursor = conn.cursor()

query = "SELECT * FROM portfolios;"
# Select all rows from the table
cursor.execute(query)

# Fetch the results
results = cursor.fetchall()

print(results)