# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1539 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"&\x0b\xc5\xa2D\x94\xed\x8eG"
    list_0 = [bytes_0, bytes_0, bytes_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "p TL!O^2IsgbA"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "p TL!O^2IsgbA"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "Ow"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Ow"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "Ow"
    list_0 = module_0.func(*str_0)
    assert list_0 == "o"
    var_0 = module_0.func(*list_0)
    assert var_0 == "O"
#    module_1.object(**var_0)
