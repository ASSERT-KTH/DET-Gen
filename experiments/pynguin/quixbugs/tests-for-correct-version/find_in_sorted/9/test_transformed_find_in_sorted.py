# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_in_sorted as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "v_\x0bbZsa6 K<*TbLF3"
    var_0 = module_0.find_in_sorted(str_0, str_0)
    assert var_0 == -1
    var_1 = module_0.find_in_sorted(str_0, str_0)
    assert var_1 == -1
#    module_0.find_in_sorted(var_0, var_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b'\x93z\xa8!\x0fB"\xe0\xd9\xf8\xcd\x91V6\x11\xc7Z\xce\x8e'
    none_type_0 = None
#    module_0.find_in_sorted(bytes_0, none_type_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
#    module_0.find_in_sorted(none_type_0, none_type_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = ';#O9phRN"b1S'
    none_type_0 = None
    var_0 = module_0.find_in_sorted(str_0, str_0)
    assert var_0 == -1
#    module_0.find_in_sorted(str_0, none_type_0)


def test_case_4():
    bytes_0 = b"\xb4\xe9l"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.find_in_sorted(list_0, bytes_0)
    assert var_0 == 1
