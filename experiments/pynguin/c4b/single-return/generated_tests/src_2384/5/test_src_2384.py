# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2384 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    set_0 = {bool_0, bool_0}
    list_0 = [set_0, bool_0, set_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xbf\xa0\xb0\xcdn#\xce\x14"
    list_0 = [bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    list_0 = []
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "\\w&<C5Cr_}_ ]23;6O"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "\\w&<C5Cr_}_ ]23;6O"
    module_1.object(**var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "\\w&<C5Cr_}_ ]23;6O"
    var_0 = module_0.func(*str_0)
    assert var_0 == "\\"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = 'zL`",piR7'
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 'zL`",piR7'
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = '"*9USC'
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == '"*9usc'
    var_1 = module_0.func(*var_0)
    assert var_1 == '"'
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = 'zL`",piR7'
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 'zL`",piR7'
    var_1 = module_0.func(*var_0)
    assert var_1 == "Z"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "lWY.\x0c3K?X"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Lwy.\x0c3k?x"
    var_1 = module_0.func(*var_0)
    assert var_1 == "l"
    module_0.func()
