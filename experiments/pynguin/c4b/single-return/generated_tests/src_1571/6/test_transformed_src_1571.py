# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1571 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"N\xd7"
    bool_0 = True
    list_0 = [bytes_0, bytes_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == b"n\xd7"
#    module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    bytes_0 = b"q\xf8N2\x98K&\xbe\xc741\x84~4\xcf\xec]\xf1L"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == b"q\xf8N2\x98K&\xbe\xc741\x84~4\xcf\xec]\xf1L"


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "sD\t>T&;"
    var_0 = module_0.func(*str_0)
    assert var_0 == "S"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b""
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_1.object()
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "e_\x0cEI9[#"
    bool_0 = True
    list_0 = [str_0, str_0, bool_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "E_\x0cei9[#"
    list_1 = [str_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "E_\x0cei9[#"
#    module_0.func()
