# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1892 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    none_type_0 = None
    list_0 = [none_type_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = ":0\tOb"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "h1"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = " 8O[\\f[L\t4}~"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "aiI]"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "hcA"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "81~ot^Tc'["
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "a1"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    str_1 = "8c~ot^|c'"
    list_1 = [str_1, str_1, str_1, str_1]
    var_1 = module_0.func(*list_1)
    module_1.object(*var_1)


@pytest.mark.xfail(strict=True)
def test_case_9():
    str_0 = "a8"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_10():
    str_0 = "h8"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    module_0.func()
