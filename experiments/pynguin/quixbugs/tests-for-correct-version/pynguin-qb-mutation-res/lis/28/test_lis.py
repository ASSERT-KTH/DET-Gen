# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lis as module_0


def test_case_0():
    float_0 = -1683.0
    tuple_0 = (float_0,)
    var_0 = module_0.lis(tuple_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = 1723.505
    dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0, float_0: float_0}
    var_0 = module_0.lis(dict_0)
    assert var_0 == 1
    tuple_0 = ()
    bool_0 = True
    tuple_1 = (tuple_0, bool_0, bool_0)
    module_0.lis(tuple_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.lis(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "J7*D2D! \\'\"8OI#"
    var_0 = module_0.lis(str_0)
    assert var_0 == 4
    var_1 = module_0.lis(str_0)
    assert var_1 == 4
    module_0.lis(var_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    bool_1 = False
    tuple_0 = (bool_0, bool_1)
    var_0 = module_0.lis(tuple_0)
    assert var_0 == 1
    str_0 = "Pm6\n\rg&\x0c~>4k,!B`\x0cvN?"
    var_1 = module_0.lis(str_0)
    assert var_1 == 7
    var_2 = module_0.lis(str_0)
    assert var_2 == 7
    module_0.lis(var_2)