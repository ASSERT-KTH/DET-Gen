# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_79 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    str_0 = 'V,g}c.|#0M(i="O&m'
    tuple_0 = (bool_0, str_0)
    module_0.func(*tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "83()}vU(a\n@C'\r'j[)2"
    module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "07\n =|d*|XLbA~9B\x0c()"
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*str_0)
    module_1.object(*var_0)
