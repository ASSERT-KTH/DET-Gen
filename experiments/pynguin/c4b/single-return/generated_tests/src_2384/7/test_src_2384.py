# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2384 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    list_0 = [bool_0]
    list_1 = [list_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "cnLu=X"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    list_0 = [str_0, dict_0, dict_0, dict_0, dict_0, dict_0, dict_0, dict_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "cnLu=X"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "cnLu=X"
    dict_0 = module_0.func(*str_0)
    assert dict_0 == "C"
    list_0 = [str_0, dict_0, dict_0, dict_0, dict_0, dict_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "cnLu=X"
    list_1 = []
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = 'V6"'
    var_0 = module_0.func(*str_0)
    assert var_0 == "v"
    list_0 = [str_0, var_0, var_0, var_0, var_0, var_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == 'v6"'
    var_2 = module_0.func(*var_0)
    assert var_2 == "V"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "cnLu=X"
    var_0 = module_0.func(*str_0)
    assert var_0 == "C"
    list_0 = [str_0, var_0, var_0, var_0, var_0, var_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == "cnLu=X"
    var_2 = module_0.func(*var_0)
    assert var_2 == "c"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "nL=|X"
    var_0 = module_0.func(*str_0)
    assert var_0 == "N"
    list_0 = [str_0, var_0, var_0, var_0, var_0, var_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == "Nl=|x"
    list_1 = []
    module_0.func(*list_1)
