# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_196 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    str_0 = "5:,]iw!!."
    var_0 = module_0.func(*str_0)
    assert var_0 == "0 0 0 0"


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "5:,]iw!!."
    list_0 = [str_0, str_0, str_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = '"-)NsIFa@"/gRkr'
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "0 0 0 0"
#    module_1.object(**var_0)


def test_case_4():
    str_0 = "!a!-"
    var_0 = module_0.func(*str_0)
    assert var_0 == "0 0 0 0"


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = 'Fs7!}VG\t"7zVPW\rmT'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
#    module_0.func(*dict_0)
