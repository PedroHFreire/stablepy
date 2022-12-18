# stable

Stable is a Python package for investment analysis. It provides tools for calculating returns, portfolio statistics, and risk metrics.

## Installation

To install stable, use pip:

```bash
pip install stable
```

## Usage

Here is an example of how to use the stable package:

```python
import stable

# Calculate returns from a timeseries of prices
returns = stable.calculate_returns(prices)

# Calculate portfolio returns and return contribution by asset
portfolio_returns = stable.calculate_portfolio_returns(returns, weights)
return_contribution = stable.calculate_return_contribution(returns, weights)

# Calculate monthly returns
monthly_returns = stable.calculate_periodic_returns(returns, period="monthly")
```

## Modules
The stable package consists of the following modules:

return_metrics: Contains functions for calculating returns and portfolio statistics.


## License
Stable is released under the MIT License. See the LICENSE file for more information.
