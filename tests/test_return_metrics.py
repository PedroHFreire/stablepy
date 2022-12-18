import numpy as np
import pytest

from stable import return_metrics

def test_calculate_returns():
    # Test arithmetic returns
    prices = np.array([1, 2, 3])
    expected_returns = np.array([1, 0.5])
    returns = return_metrics.calculate_returns(prices, return_type="arithmetic")
    assert np.allclose(returns, expected_returns)
    
    # Test log returns
    prices = np.array([1, 2, 3])
    expected_returns = np.array([0, 0.69314718])
    returns = return_metrics.calculate_returns(prices, return_type="log")
    assert np.allclose(returns, expected_returns)
    
    # Test invalid return_type
    with pytest.raises(ValueError, match=r"Invalid return_type: invalid"):
        return_metrics.calculate_returns(prices, return_type="invalid")

def test_calculate_portfolio_returns():
    returns = np.array([[0.5, 0.5, 0.5], [0.1, 0.2, 0.3]])
    weights = np.array([0.5, 0.5])
    expected_return = 0.4
    portfolio_return = return_metrics.calculate_portfolio_returns(returns, weights)
    assert np.isclose(portfolio_return, expected_return)

def test_calculate_return_contribution():
    returns = np.array([[0.5, 0.5, 0.5], [0.1, 0.2, 0.3]])
    weights = np.array([0.5, 0.5])
    expected_contributions = np.array([0.2, 0.2])
    contributions = return_metrics.calculate_return_contribution(returns, weights)
    assert np.allclose(contributions, expected_contributions)

def test_calculate_periodic_returns():
    returns = np.array([0.5, 0.5, 0.5, 0.1, 0.2, 0.3])
    
    # Test daily returns
    expected_returns = returns
    periodic_returns = return_metrics.calculate_periodic_returns(returns, period="daily")
    assert np.allclose(periodic_returns, expected_returns)
    
    # Test weekly returns
    expected_returns = np.array([0.5, 0.6])
    periodic_returns = return_metrics.calculate_periodic_returns(returns, period="weekly")
    assert np.allclose(periodic_returns, expected_returns)
    
    # Test monthly returns
    expected_returns = np.array([0.45, 0.55])
    periodic_returns = return_metrics.calculate_periodic_returns(returns, period="monthly")
    assert np.allclose(periodic_returns, expected_returns)
    
    # Test yearly returns
    expected_returns = np.array([0.46])
    periodic_returns = return_metrics.calculate_periodic_returns(returns, period="yearly")
    assert np.allclose(periodic_returns, expected_returns)
    
    # Test invalid period
    with pytest.raises(ValueError, match=r"Invalid period: invalid"):
        return_metrics.calculate_periodic_returns(returns, period="invalid")