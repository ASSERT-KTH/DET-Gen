# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1495 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = 'P9w"S}lmz~%)n. f'
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 'P9w"S}lmz~%)n. f'
    var_1 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = 'P9w"S}lmz~%)n. f'
    var_0 = module_0.func(*str_0)
    assert var_0 == "p"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "\t2T(UO9%\\)"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "\t2t(uo9%\\)"
    module_1.object(*list_0)
