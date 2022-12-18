# stablepy

Stablepy is a Python package for investment analysis from the stable system. It provides tools for calculating returns, portfolio statistics, and risk metrics.

## Installation

To install stablepy, use pip:

```bash
pip install stablepy
```

## Usage

Here is an example of how to use the stablepy package:

```python
import stablepy

# Calculate returns from a timeseries of prices
returns = stablepy.calculate_returns(prices)

# Calculate portfolio returns and return contribution by asset
portfolio_returns = stablepy.calculate_portfolio_returns(returns, weights)
return_contribution = stable.calculate_return_contribution(returns, weights)

# Calculate monthly returns
monthly_returns = stablepy.calculate_periodic_returns(returns, period="monthly")
```

## Modules
The stablepy package consists of the following modules:

return_metrics: Contains functions for calculating returns and portfolio statistics.


## License
Stablepy is released under the MIT License. See the LICENSE file for more information.
