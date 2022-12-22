import pytest

from stablepy import stabledb

def test_execute_query():
    # Test that the function returns the expected results
    results = stabledb.execute_query('queries/portfolios.sql')
    assert results == [(1, 'Dummy Stock Portfolio', '2018-12-31', 'Equal weight portfolio of stocks')]

    # Test that the function raises an error when passed an invalid file path
    with pytest.raises(FileNotFoundError):
        stabledb.execute_query('invalid_path.sql')