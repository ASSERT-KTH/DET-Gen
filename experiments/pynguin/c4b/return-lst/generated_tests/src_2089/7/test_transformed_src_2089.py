# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2089 as module_0


def test_case_0():
    bytes_0 = b"\x97\x1c3R\x9f\x9f"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)


def test_case_1():
    set_0 = set()
    list_0 = [set_0, set_0, set_0, set_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0, bool_0, bool_0, bool_0, bool_0]
    list_1 = [list_0, bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_1)
    bytes_0 = b"\x97\x1cR+\x9f"
    list_2 = [bytes_0, bytes_0, bool_0, bytes_0]
    var_1 = module_0.func(*list_2)
#    module_0.func(*var_1)
