# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_894 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "jhd'}!"
    var_0 = module_0.func(*str_0)
    assert var_0 == "J"
    list_0 = [var_0, str_0, str_0, var_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == "j"
    var_2 = module_0.func(*var_1)
    assert var_2 == "J"
    var_3 = module_0.func(*list_0)
    assert var_3 == "j"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b">\x84\x8aiZ\x81\x9b\xb2"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


def test_case_3():
    str_0 = "csHx7.0%.F.!\x0bq!SM.k"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "csHx7.0%.F.!\x0bq!SM.k"


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = 'EHF!"@L.b'
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 'EHF!"@L.b'
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "\x0bIs]buo#\\q$\x0cU4<c}Y"
    var_0 = module_0.func(*str_0)
    assert var_0 == "\x0b"
    list_0 = [var_0, str_0, str_0, var_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == "\x0b"
    list_1 = [str_0, str_0]
    var_2 = module_0.func(*list_1)
    assert var_2 == "\x0bIs]buo#\\q$\x0cU4<c}Y"
#    module_1.object(*var_2)


#@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "pAB$YZ"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Pab$yz"
    var_1 = module_0.func(*list_0)
    assert var_1 == "Pab$yz"
    var_2 = module_0.func(*list_0)
    assert var_2 == "Pab$yz"
#    module_0.func()
