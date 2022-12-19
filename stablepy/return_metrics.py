# module: return_metrics.py

import numpy as np

def calculate_returns(prices: np.ndarray, return_type: str = "arithmetic") -> np.ndarray:
    """
    Calculate returns from a timeseries of prices.
    
    Parameters:
        prices: A 1D numpy array of prices.
        return_type: Type of return to calculate. Can be "arithmetic" or "log".
        
    Returns:
        A 1D numpy array of returns.
    """
    if return_type == "arithmetic":
        returns = prices[1:] / prices[:-1] - 1
    elif return_type == "log":
        returns = np.log(prices[1:] / prices[:-1])
    else:
        raise ValueError(f"Invalid return_type: {return_type}")
        
    return returns

def calculate_portfolio_returns(returns: np.ndarray, weights: np.ndarray) -> float:
    """
    Calculate the return of a portfolio given timeseries of asset returns and weights.
    
    Parameters:
        returns: A 2D numpy array of asset returns, with rows representing different assets and columns representing time.
        weights: A 1D numpy array of weights for the assets in the portfolio.
        
    Returns:
        The return of the portfolio.
    """
    return np.dot(returns, weights)

def calculate_return_contribution(returns: np.ndarray, weights: np.ndarray) -> np.ndarray:
    """
    Calculate the contribution of each asset to the overall portfolio return.
    
    Parameters:
        returns: A 2D numpy array of asset returns, with rows representing different assets and columns representing time.
        weights: A 1D numpy array of weights for the assets in the portfolio.
        
    Returns:
        A 1D numpy array of return contributions for each asset.
    """
    return weights * returns

def calculate_periodic_returns(returns: np.ndarray, period: str) -> np.ndarray:
    """
    Calculate periodic returns from a timeseries of returns.
    
    Parameters:
        returns: A 1D numpy array of returns.
        period: The period to calculate returns for. Can be "daily", "weekly", "monthly", or "yearly".
        
    Returns:
        A 1D numpy array of periodic returns.
    """
    if period == "daily":
        pass  # returns are already daily
    elif period == "weekly":
        returns = returns.reshape(-1, 5).mean(axis=1)
    elif period == "monthly":
        returns = returns.reshape(-1, 21).mean(axis=1)
    elif period == "yearly":
        returns = returns.reshape(-1, 252).mean(axis=1)
    else:
        raise ValueError(f"Invalid period: {period}")
        
    return returns