# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_462 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    module_0.func(*bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    bytes_0 = b"\xdd\x859\xe5,J*\xf6\x04\xf7\x1e^u"
    list_0 = [bool_0, bool_0, bool_0, bytes_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*bytes_0)
    module_0.func()
