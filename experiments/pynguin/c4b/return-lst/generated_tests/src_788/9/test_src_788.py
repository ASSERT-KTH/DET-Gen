# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_788 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    list_0 = []
    list_1 = [list_0, list_0]
    var_0 = module_0.func(*list_1)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = 'C9==p!r6uzlDb"l-'
    set_0 = {str_0}
    list_0 = [set_0, set_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    list_0 = []
    list_1 = [list_0, list_0]
    var_0 = module_0.func(*list_1)
    var_1 = module_0.func(*var_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = 'C9==p!r6uzlDb"l-'
    set_0 = {str_0}
    list_0 = [str_0, set_0, str_0, set_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "*/^A<mFN'1tnSNfA[zU"
    set_0 = set()
    list_0 = [str_0, set_0, set_0, set_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
    module_0.func()
