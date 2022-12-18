# Import necessary modules from the package
from .financial_analysis import calculate_returns, calculate_risk
from .stock_data import retrieve_stock_data, process_stock_data

# Define any initialization code for the package
def initialize():
    print("Initializing stable package")

# Execute the initialization code when the package is imported
initialize()