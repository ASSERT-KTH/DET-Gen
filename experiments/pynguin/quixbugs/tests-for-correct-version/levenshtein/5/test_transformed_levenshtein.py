# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import levenshtein as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "~)n7n>%wn#NrmJU7q"
    var_0 = module_0.levenshtein(str_0, str_0)
    assert var_0 == 0
    str_1 = ",UoK?Zne#4OyHj{9Xd\x0b"
#    module_0.levenshtein(str_1, var_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 722
#    module_0.levenshtein(int_0, int_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "_guHmA6 \rfDhX\x0c"
    tuple_0 = (str_0,)
#    module_0.levenshtein(tuple_0, str_0)
