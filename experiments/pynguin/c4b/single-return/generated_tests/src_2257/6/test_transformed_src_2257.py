# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2257 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"!\x88\x18\x99u"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == b"!\x88\x18\x99u"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x96"
    list_0 = [bytes_0, bytes_0, bytes_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xd0\x88E"
    list_0 = [bytes_0, bytes_0, bytes_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"fk\xb9"
    list_0 = [bytes_0]
    list_1 = [list_0, bytes_0, bytes_0]
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"=\xe4\x8f\x07D\x7f\x02\xf8\xf7"
    list_0 = [bytes_0]
    list_1 = [list_0, bytes_0, bytes_0]
#    module_0.func(*list_1)
