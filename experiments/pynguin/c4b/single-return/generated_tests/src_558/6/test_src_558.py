# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_558 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xa7\x08\xfe\xf9jkW\xc4\xe0_\x1a%\x13\xf1\xeb"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 13
    var_1 = module_0.func(*bytes_0)
    assert var_1 == 13
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"~\xe7\x99J\x84#\xc2)\xb0\xf3"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 2
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"Sl\xa7h\xb7\xa6\x14\xd9\xd3\xeb\xb7\xea\xc5j\x15\n]\xaaG\xb9"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 5
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"Cx\x0f9\x00\xf9b\x88z\xe6\xb0\x02\xe4\x8dk\xcdX"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
    var_1 = module_1.object()
    module_1.object(*var_0, **var_0)
