# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2396 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "%\rP']{.>msz2I"
    var_0 = module_0.func(*str_0)
    assert var_0 == ".%"
    var_1 = module_0.func(*str_0)
    assert var_1 == ".%"
    var_2 = module_0.func(*str_0)
    assert var_2 == ".%"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "%\rP']{.<msz2I"
    str_1 = "cU6"
    list_0 = [str_0, str_1, str_1]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".%.\r.p.'.].{...<.m.s.z.2"
    module_1.object(*list_0, **var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "cU6"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".c.6"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "%\rP']{.<msz2I"
    str_1 = "Y"
    var_0 = module_0.func(*str_1)
    assert var_0 == "."
    var_1 = module_0.func(*str_0)
    assert var_1 == ".%"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "%\rP']{.<msz2I"
    str_1 = "o"
    var_0 = module_0.func(*str_1)
    assert var_0 == "."
    var_1 = module_0.func(*str_0)
    assert var_1 == ".%"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "OE"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "."
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "184A2"
    str_1 = "cU6"
    list_0 = [str_0, str_1, str_1]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".1.8.4.2"
    module_1.object(*list_0, **var_0)
