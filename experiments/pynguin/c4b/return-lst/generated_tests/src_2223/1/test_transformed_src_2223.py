# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2223 as module_0


def test_case_0():
    str_0 = "\\&p_&My\x0cAK"
    var_0 = module_0.func(*str_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = "\\&p_&My\x0cAK"
    str_1 = ""
    var_0 = module_0.func(*str_0)
    str_2 = "\td4"
    list_0 = [str_1, str_2]
    var_1 = module_0.func(*list_0)
