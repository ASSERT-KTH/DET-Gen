# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1986 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "V\tW}w54/}c074."
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "V\tw54}c07s74."
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    none_type_0 = None
    module_1.object(*var_0, **none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "\tn75474/RIo4+0874u"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()
