# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2396 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x8dDk\xe5\xe1\xa43\xd3\xed\xe4.{\\\xdb"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = '8T818D\t[Sed:N"a3F\t\x0c_'
    var_0 = module_0.func(*str_0)
    assert var_0 == ".8"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = '8T818D\t[Sed:N"a3F\t\x0c_'
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == '.8.t.8.1.8.d.\t.[.s.d.:.n.".3.f.\t.\x0c._'
    var_1 = module_0.func(*str_0)
    assert var_1 == ".8"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "g\r=3\t\t9k-4>sdX^mU"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".g.\r.=.3.\t.\t.9.k.-.4.>.s.d.x.^.m"
    list_1 = []
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = '8TRO8D\t[Sud:N"a3F.\x0c_'
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == '.8.t.r.8.d.\t.[.s.d.:.n.".3.f...\x0c._'
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "Uy/WI@.*\t\x0bu7"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "./.w.@...*.\t.\x0b.7"
    module_0.func()
