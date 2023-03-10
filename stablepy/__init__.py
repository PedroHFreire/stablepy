# Import necessary modules from the package
from .return_metrics import calculate_returns, calculate_portfolio_returns, calculate_return_contribution, calculate_periodic_returns
from .stabledb import execute_query

# Define any initialization code for the package
def initialize():
    print("Initializing stablepy package")

# Execute the initialization code when the package is imported
initialize()

# Package metadata
__version__ = "1.0.0"
__author__ = "Pedro Freire"
__license__ = "MIT"