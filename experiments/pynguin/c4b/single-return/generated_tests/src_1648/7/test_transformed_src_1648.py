# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1648 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    str_0 = "qllkN*\\glQlguLj~_u"
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "qllkN*\\glQlguL@j~wu"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    var_1 = module_0.func(*var_0)
    assert var_1 == "NO"
    var_2 = module_0.func(*list_0)
    assert var_2 == "YES"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "}piV1'9ws%n5^L]Az"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    str_1 = "qllkN*\\glQlguLj~_u"
    var_1 = module_0.func(*str_1)
    assert var_1 == "NO"
#    module_1.object(**var_1)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "V7AHozr|4}/c?wr2beE"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    str_1 = "qllkN*\\glQlguLj~_u"
#    module_1.object(*list_0, **str_1)
