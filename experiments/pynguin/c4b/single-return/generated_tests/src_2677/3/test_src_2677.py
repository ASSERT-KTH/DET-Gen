# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2677 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "<B^j"
    bool_0 = False
    list_0 = [str_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "undefined"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "<B^j"
    bool_0 = True
    list_0 = [str_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "cw"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "<_b.j"
    bool_0 = False
    list_0 = [str_0, bool_0, bool_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = ">4:;:\x0b\\E+P2"
    bool_0 = True
    list_0 = [str_0, bool_0, bool_0, str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "^p<B^j"
    bool_0 = True
    list_0 = [str_0, bool_0, str_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "ccw"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "<B<j"
    bool_0 = False
    list_0 = [str_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "undefined"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "v)8g"
    bool_0 = False
    list_0 = [str_0, bool_0, bool_0]
    module_0.func(*list_0)
