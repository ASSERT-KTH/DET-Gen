# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1827 as module_0


def test_case_0():
    bool_0 = True
    str_0 = "\n%EB0yt0961.9;{"
    list_0 = [bool_0, bool_0, bool_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "I hate it"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "2Z[]+A\x0b-^}'"
    var_0 = module_0.func(*str_0)
    assert var_0 == "I hate that I love it"
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == "I hate it"
#    module_0.func()
