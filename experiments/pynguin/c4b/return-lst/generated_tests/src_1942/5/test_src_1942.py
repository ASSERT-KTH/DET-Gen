# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1942 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"1\xb4]\x0e\xc2\x16\x06\xba\xbc\xd87\xfe\xeb\x7f\x183t"
    list_0 = module_0.func(*bytes_0)
    var_0 = module_1.object()
    list_1 = []
    module_0.func(*list_1)