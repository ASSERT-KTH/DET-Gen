# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1422 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x04h\xeb"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "11"
#    module_0.func(*var_0)


def test_case_1():
    bytes_0 = b"\x04h\xeb"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "11"


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


def test_case_3():
    bytes_0 = b"\xdb"
    var_0 = module_0.func(*bytes_0)
    assert (
        var_0
        == "7111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
    )
    var_1 = module_0.func(*var_0)
    assert var_1 == "711"


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x02"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "1"
#    module_1.object(**list_0)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"\x04h\xeb"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "11"
    bytes_1 = b"\xba\xf8\x85\x858\xfb"
    var_1 = module_0.func(*bytes_1)
    assert (
        var_1
        == "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
    )
#    module_1.object(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_6():
    bytes_0 = b"\x03"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "7"
    var_1 = module_0.func(*var_0)
    assert var_1 == "711"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_7():
    bytes_0 = b"\x06"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "111"
#    module_0.func(*var_0)


def test_case_8():
    bytes_0 = b"\x05=\x04h\xeb"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "71"
    var_1 = module_0.func(*var_0)
    assert var_1 == "711"
