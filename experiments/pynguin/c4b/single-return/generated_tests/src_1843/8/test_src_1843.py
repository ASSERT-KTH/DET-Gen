# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1843 as module_0


def test_case_0():
    bytes_0 = b"ac+\xa2\xc7\xa5Hc\xca\xa8C\xea\x7ft\xf6\xa4"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 9


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()
