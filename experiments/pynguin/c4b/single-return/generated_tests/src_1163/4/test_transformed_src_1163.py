# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1163 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xe3\xf9\xc9\xbb8\xb1\xdb\\\xe87X\xcfI\xe4\xa8"
    set_0 = {bytes_0, bytes_0}
    bool_0 = False
    list_0 = [set_0, set_0, bool_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "@/D^KW m)c.a"
    var_0 = module_0.func(*str_0)
    assert var_0 == 1
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 2833
    list_0 = [int_0]
#    module_0.func(*list_0)
