# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kheapsort as module_0
import builtins as module_1


def test_case_0():
    int_0 = 1444
    var_0 = module_0.kheapsort(int_0, int_0)


def test_case_1():
    list_0 = []
    none_type_0 = None
    var_0 = module_0.kheapsort(list_0, none_type_0)
    object_0 = module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    var_0 = module_0.kheapsort(bool_0, bool_0)
    list_0 = [bool_0, bool_0]
    none_type_0 = None
    var_1 = module_0.kheapsort(list_0, none_type_0)
    bytes_0 = b"h%=i\xe0\xd8E\xe7\xa9\x9e`aS"
    var_2 = module_0.kheapsort(bytes_0, bytes_0)
    var_3 = module_0.kheapsort(var_2, bytes_0)
    var_4 = module_0.kheapsort(bytes_0, bytes_0)
    var_5 = module_0.kheapsort(bytes_0, bytes_0)
    var_6 = module_0.kheapsort(var_4, var_4)
    bool_1 = True
    var_7 = module_0.kheapsort(var_2, bool_1)
    var_8 = module_0.kheapsort(var_2, var_6)
    dict_0 = {}
    object_0 = module_1.object(**dict_0)
    module_1.object(*var_1)