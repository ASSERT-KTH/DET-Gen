# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_177 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "_TDBqZtN\x0c0o!p<l(c"
    var_0 = module_0.func(*str_0)
    assert var_0 == 2
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xd0\xac'\xe3\x11my\x03\xad\xbee"
    module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = 'U>aL"1g!,J-,\rXo@Ie'
    var_0 = module_0.func(*str_0)
    assert var_0 == 1
    module_1.object(*var_0, **var_0)