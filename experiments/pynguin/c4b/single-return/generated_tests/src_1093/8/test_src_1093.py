# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1093 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xb0\x9ee\xbd\x90\x11\x0b\xb7\xcf\xb7\xa3\xb6w\xed\xaf7H\x89\xdei"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
