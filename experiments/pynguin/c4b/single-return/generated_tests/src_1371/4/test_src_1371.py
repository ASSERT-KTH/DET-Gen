# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1371 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"CLLG\xe8BZ\x864"
    module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "G"
    var_0 = module_0.func(*str_0)
    assert var_0 == ".g"
    module_0.func()
