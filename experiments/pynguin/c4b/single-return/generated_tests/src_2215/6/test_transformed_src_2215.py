# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2215 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xfe\x0e\x0f\x00Z"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "2541415090"
#    module_0.func()


def test_case_1():
    bytes_0 = b"\x0b\xb1\x17\xb9\n\xda\x0c\xe3\xd7\x13"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "1117723185102181222721519"
    var_1 = module_0.func(*var_0)
    assert var_1 == "1"
    var_2 = module_0.func(*var_0)
    assert var_2 == "1"


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    tuple_0 = (bool_0,)
    bool_1 = False
    bool_2 = True
    list_0 = [tuple_0, bool_1, bool_2]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x18\x9e\x99\x97\xf6\x9aW\x07)+\x89\x9b\xa0o\x8c\x06"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "2415815315124615487741431371551601111399"
#    module_1.object(**list_0)
