# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_894 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "LZ|.}]sFc<1pLSK?8TP"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "LZ|.}]sFc<1pLSK?8TP"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "xW\x0cz"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "xW\x0cz"
    object_0 = module_1.object()
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "#\n5. "
    list_0 = [str_0]
    var_0 = module_0.func(*str_0)
    assert var_0 == "#"
    var_1 = module_0.func(*list_0)
    assert var_1 == "#\n5. "
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "B05&ORX$\rr\\V<b%BM"
    var_0 = module_0.func(*str_0)
    assert var_0 == "b"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "xW\x0c"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Xw\x0c"
    object_0 = module_1.object()
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "o\x0b"
    var_0 = module_0.func(*str_0)
    assert var_0 == "O"
    object_0 = module_1.object()
#    module_1.object(*object_0)