import pytest
import rolldie

#pytest.skip()
def test_terminate():
    assert rolldie.terminate(True) == 0

def test_result():
    num = 2
    assert rolldie.format_result(num) == f"Result {num}"

