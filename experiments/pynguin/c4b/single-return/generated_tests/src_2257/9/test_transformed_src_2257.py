# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2257 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "Xo/2_MF_"
    var_0 = module_0.func(*str_0)
    assert var_0 == "x"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b";\xc0_T\xb5\xd1\x85\x05!P"
    list_0 = [bytes_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    list_0 = []
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = ",xphkSGRs`/m>%s&~"
    var_0 = module_0.func(*str_0)
    assert var_0 == ","
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = ",xphkSGRs`/m>%s&~"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ",xphkSGRs`/m>%s&~"
#    module_0.func()
