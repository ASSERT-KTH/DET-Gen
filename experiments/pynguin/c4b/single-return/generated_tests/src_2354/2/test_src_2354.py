# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2354 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "f<)&W$=x"
    var_0 = module_0.func(*str_0)
    assert var_0 == ".f"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "f<)&W$=x"
    var_0 = module_0.func(*str_0)
    assert var_0 == ".f"
    bool_0 = True
    list_0 = [var_0, var_0, bool_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == "...f"
    var_2 = module_0.func(*list_0)
    assert var_2 == "...f"
    var_3 = module_0.func(*list_0)
    assert var_3 == "...f"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "EI\x0baU"
    var_0 = module_0.func(*str_0)
    assert var_0 == ""
    bool_0 = True
    list_0 = [var_0, var_0, bool_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == ""
    module_0.func(*var_0)
