# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_263 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"AE\x8c\x92h\xacU:\xc9\xdf\x99\xe6Nd\xab\xbb.\xf6x$"
    set_0 = {bytes_0, bytes_0, bytes_0}
    list_0 = [set_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "Y_p|kby56vr7R*.&~"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*str_0)
    assert var_0 == 1
    var_1 = module_0.func(*list_0)
    assert var_1 == 17
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    list_0 = []
#    module_0.func(*list_0)
