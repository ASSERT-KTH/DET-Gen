# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1532 as module_0


def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 1023.39
    bytes_0 = b"\x06\x13\xca\x9c\x1a\r\xfd\xba\x80v3"
    list_0 = [float_0, bytes_0, float_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 1022.0538835354786
    bytes_0 = b"\x13\xca\xca\x1a\r\xfd\xba\x80v3"
    list_0 = [float_0, bytes_0, float_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = 7.796077957236662
    bytes_0 = b"M\xa1`{/\xec\x12\x90\x06H\xba\x0c\x9a!\x136\xcb%"
    list_0 = [float_0, bytes_0, bytes_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
#    module_0.func()
