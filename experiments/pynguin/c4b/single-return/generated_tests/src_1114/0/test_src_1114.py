# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1114 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = '\tc,"Zv72&="UG|?F@?&K'
    var_0 = module_0.func(*str_0)
    assert var_0 == "\t"
    module_0.func()


def test_case_1():
    str_0 = '\tc,"Zv72&="UG|?F@?&K'
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == '\tc,"Zv72&="UG|?F@?&K'


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "D83aiHN6wXI3nir\n^r|B"
    var_0 = module_0.func(*str_0)
    assert var_0 == "d"
    object_0 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xd3|\xe5\xc1\xbeX\xfb\xff\x14"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    str_0 = '\tc,"Zv72&="UG|?F@?&K'
    list_1 = [str_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == '\tc,"Zv72&="UG|?F@?&K'
    str_1 = "wAxUcJ.P(U)J"
    var_2 = module_0.func(*str_1)
    assert var_2 == "W"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = 'hIA~O4GG$0\r"7'
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 'Hia~o4gg$0\r"7'
    var_1 = module_0.func(*str_0)
    assert var_1 == "H"
    module_0.func()