# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import re as module_0
import to_base as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    var_0 = module_0.purge()
    assert module_0.ASCII == module_0.RegexFlag.ASCII
    assert module_0.A == module_0.RegexFlag.ASCII
    assert module_0.IGNORECASE == module_0.RegexFlag.IGNORECASE
    assert module_0.I == module_0.RegexFlag.IGNORECASE
    assert module_0.LOCALE == module_0.RegexFlag.LOCALE
    assert module_0.L == module_0.RegexFlag.LOCALE
    assert module_0.UNICODE == module_0.RegexFlag.UNICODE
    assert module_0.U == module_0.RegexFlag.UNICODE
    assert module_0.MULTILINE == module_0.RegexFlag.MULTILINE
    assert module_0.M == module_0.RegexFlag.MULTILINE
    assert module_0.DOTALL == module_0.RegexFlag.DOTALL
    assert module_0.S == module_0.RegexFlag.DOTALL
    assert module_0.VERBOSE == module_0.RegexFlag.VERBOSE
    assert module_0.X == module_0.RegexFlag.VERBOSE
    assert module_0.TEMPLATE == module_0.RegexFlag.TEMPLATE
    assert module_0.T == module_0.RegexFlag.TEMPLATE
    assert module_0.DEBUG == module_0.RegexFlag.DEBUG
    var_1 = var_0.__dir__()
    module_1.to_base(bool_0, var_1)


def test_case_1():
    bool_0 = False
    var_0 = module_1.to_base(bool_0, bool_0)
    assert var_0 == ""
    var_1 = module_1.to_base(bool_0, bool_0)
    assert var_1 == ""


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_1.to_base(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 1270
    var_0 = module_1.to_base(int_0, int_0)
    assert var_0 == "10"
    var_0.substitute(int_0)