# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_866 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b';\x84w]"\xe1\r)'
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 34279


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


def test_case_3():
    bytes_0 = b"\x8b\xce\xb0R\xfd\x02\xee\x7f\xa6=\xba\xfcU\x96\xf1\t}"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 447719
    list_0 = [var_0, var_0, bytes_0]
    var_1 = module_1.object()
    var_2 = module_0.func(*list_0)
