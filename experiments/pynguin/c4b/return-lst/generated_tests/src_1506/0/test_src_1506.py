# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1506 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "\n<Q\x0bW4+@a(LGZ"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = '!#c"?Dq#>93[[Oy'
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    tuple_0 = (bool_0,)
    list_0 = [tuple_0, tuple_0]
    var_0 = module_0.func(*list_0)
    bool_1 = True
    module_0.func(*bool_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "i^r3Hm/`e\r{:T#J#"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    list_1 = [str_0]
    list_2 = [str_0]
    var_1 = module_0.func(*list_2)
    var_2 = module_0.func(*list_1)
    module_1.object(**var_1)
