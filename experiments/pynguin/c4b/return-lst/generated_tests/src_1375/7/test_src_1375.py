# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1375 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"l\x1c\xe6\xe5bu\xb7,\xf7\xf5Q\xb79&Y\xf7\xe7\xad\xc2y"
    var_0 = module_0.func(*bytes_0)
    module_0.func()