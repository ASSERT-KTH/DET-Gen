# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_156 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x9d\x89"
    var_0 = module_0.func(*bytes_0)
    none_type_0 = None
    module_0.func(*none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xe0\x1a\x95%\xd0\xf49\xf3\x04\x02B\xf7\x1a\xa0\xc3x"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*var_0)
    module_0.func()
