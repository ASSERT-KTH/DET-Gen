# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_first_in_sorted as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"s\xdb\x16\x8c="
    module_0.find_first_in_sorted(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    var_0 = module_0.find_first_in_sorted(dict_0, dict_0)
    assert var_0 == -1
    module_0.find_first_in_sorted(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    object_0 = module_1.object()
    module_0.find_first_in_sorted(object_0, object_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    int_0 = -63
    bytes_0 = b"\xe3\x05s\x8fK\x08\xee\x8e\x10\xcaV\xdb\x06"
    tuple_0 = (bool_0, int_0, bytes_0)
    list_0 = [tuple_0, bytes_0]
    set_0 = {bytes_0}
    tuple_1 = (list_0, set_0, tuple_0)
    var_0 = module_0.find_first_in_sorted(tuple_1, set_0)
    assert var_0 == 1
    object_0 = module_1.object()
    none_type_0 = None
    module_0.find_first_in_sorted(object_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    dict_0 = {bool_0: bool_0}
    var_0 = module_0.find_first_in_sorted(dict_0, bool_0)
    assert var_0 == 0
    bytes_0 = b"!\x0eW5YM\xf4"
    module_0.find_first_in_sorted(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "YBU9T>Y9,d*\x0c(asK?e u"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == -1
    int_0 = -344
    module_0.find_first_in_sorted(str_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    bytes_0 = b"Gn\xaa!\xbd\xf0Ro3\x9f\xb0\xbb \x04\xee\xa7JG"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    bytes_1 = b"k\xb7\xb5\x05+\x81\x8a>\xdaL\xed\x99\xaf\xb1\xb7_\xc5"
    var_0 = module_0.find_first_in_sorted(list_0, bytes_1)
    assert var_0 == -1
    var_1 = module_0.find_first_in_sorted(list_0, bytes_0)
    assert var_1 == 0
    none_type_0 = None
    module_0.find_first_in_sorted(none_type_0, none_type_0)