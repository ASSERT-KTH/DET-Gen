# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import levenshtein as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "&}"
    str_1 = "\r3T4YLxK~`;O22A"
    var_0 = module_0.levenshtein(str_0, str_1)
    assert var_0 == 15
    str_2 = "Os2W9"
    dict_0 = {str_0: str_0, str_2: str_0}
#    module_1.object(**dict_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
#    module_0.levenshtein(tuple_0, tuple_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = 'zNL]"<;<HXR$B;q(68+'
    var_0 = module_0.levenshtein(str_0, str_0)
    assert var_0 == 0
#    module_0.levenshtein(var_0, var_0)
