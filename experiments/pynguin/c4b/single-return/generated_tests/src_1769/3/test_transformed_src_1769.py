# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1769 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    set_0 = {bool_0}
    list_0 = [set_0, bool_0, set_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ""
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x8d\x99"
    list_0 = [bytes_0, bytes_0]
    object_0 = module_1.object()
    list_1 = [list_0, object_0, object_0, object_0]
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
#def test_case_3():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "Z:2!P]d(R"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Z:2!P]D(R"
    var_1 = module_0.func(*list_0)
    assert var_1 == "Z:2!P]D(R"
#    module_0.func()
