# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2163 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "rM$#g\nLI"
    bytes_0 = b"\xa47_\xebc\xbf\x91O\x10\xc0"
    dict_0 = {bytes_0: str_0, bytes_0: bytes_0, bytes_0: bytes_0}
    list_0 = [str_0, str_0, dict_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "[Um\x0bniE'+HI[: ;\")"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
#    module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "Hq5i\\k?bu_d)V{9Y%X)Z"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*str_0)
    assert var_0 == 0
    var_1 = module_0.func(*list_0)
    assert var_1 == 1
    list_1 = [list_0]
    var_2 = module_0.func(*list_1)
    assert var_2 == 2
#    module_0.func()
