import pytest

from stablepy import stabledb

def test_execute_query():
    # Test that the function returns the expected results
    results = stabledb.execute_query('queries/portfolios.sql')
    assert results == [('portfolio1', 100, 0.5), ('portfolio2', 200, 0.6)]

    # Test that the function raises an error when passed an invalid file path
    with pytest.raises(FileNotFoundError):
        stabledb.execute_query('invalid_path.sql')