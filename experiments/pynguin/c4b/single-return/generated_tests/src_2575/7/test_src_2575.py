# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2575 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "},lY%lm:&g|\nq$"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = 'KK:!r\tO"t, [d'
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    module_1.object(*var_0, **var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "IyiGI-l|VVu\\gzz^y?b"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    str_1 = "V/,"
    var_1 = module_0.func(*str_1)
    assert var_1 == 0
    module_0.func()
