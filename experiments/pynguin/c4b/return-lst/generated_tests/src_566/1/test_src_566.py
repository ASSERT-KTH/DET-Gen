# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_566 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 1781
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xa0\xc9\xe1\xa6\ty\xaa\x8f\x1b\xea\xa9\xb3\xfe& \xeb\xe2\x7f\x9f\xf2"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x0e\xeb\x9aA\xd7\x99\xd4\xdf"
    var_0 = module_0.func(*bytes_0)
    module_1.object(*var_0, **var_0)