# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import flatten as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"o_O\xda\x1dQ?to6@\xe3\xc992\xd1"
    var_0 = module_0.flatten(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    tuple_0 = (bool_0, bool_0, bool_0)
    var_0 = module_0.flatten(tuple_0)
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    none_type_0 = None
    var_0 = module_0.flatten(none_type_0)
    tuple_0 = (bool_0, list_0, bool_0)
    var_1 = module_0.flatten(tuple_0)
    module_1.object(*var_1)