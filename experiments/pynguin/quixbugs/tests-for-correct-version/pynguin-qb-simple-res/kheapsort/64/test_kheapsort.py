# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kheapsort as module_0
import builtins as module_1


def test_case_0():
    bool_0 = True
    var_0 = module_0.kheapsort(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    complex_0 = 3943.8703 - 1387.2307664517355j
    str_0 = "#SDeb+\\>8Xr(J&B:"
    str_1 = ""
    list_0 = []
    bool_0 = False
    var_0 = module_0.kheapsort(list_0, bool_0)
    str_2 = "G"
    dict_0 = {str_0: complex_0, str_1: complex_0, str_2: var_0}
    module_1.object(*var_0, **dict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    complex_0 = 3943.8703 - 1394.535j
    str_0 = 'E"^an%..D'
    list_0 = [str_0]
    bool_0 = True
    var_0 = module_0.kheapsort(list_0, bool_0)
    str_1 = "G"
    dict_0 = {str_0: complex_0, str_1: complex_0, str_1: var_0}
    module_1.object(*var_0, **dict_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    complex_0 = 3943.8703 - 1387.2307664517355j
    str_0 = 'E"^an%..D'
    str_1 = ""
    list_0 = [str_1]
    bool_0 = False
    var_0 = module_0.kheapsort(list_0, bool_0)
    str_2 = "G"
    dict_0 = {str_0: complex_0, str_1: complex_0, str_2: var_0}
    module_1.object(*var_0, **dict_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = 'E"^an%..D'
    str_1 = ""
    list_0 = [str_1, str_0, str_0, str_0]
    bool_0 = True
    none_type_0 = None
    var_0 = module_0.kheapsort(list_0, none_type_0)
    str_2 = "G"
    dict_0 = {str_0: bool_0, str_1: bool_0, str_2: var_0}
    module_1.object(*var_0, **dict_0)