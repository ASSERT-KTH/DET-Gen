# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import flatten as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"z\xc4\x9c\xdd\xa5"
    var_0 = module_0.flatten(bytes_0)
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b'O+}"A^\x1aK\xe1(\xda'
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0}
    var_0 = module_0.flatten(dict_0)
    int_0 = -1745
    list_0 = [bytes_0, bytes_0, int_0, int_0]
    str_0 = "R\x0c~=:MB"
    bool_0 = True
    tuple_0 = (int_0, list_0, str_0, bool_0)
    var_1 = module_0.flatten(tuple_0)
    module_1.object(*var_1)