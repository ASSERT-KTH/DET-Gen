# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import levenshtein as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    set_0 = set()
    str_0 = "\nCDE\x0b"
    var_0 = module_0.levenshtein(str_0, str_0)
    assert var_0 == 0
#    module_0.levenshtein(set_0, set_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    none_type_0 = None
#    module_0.levenshtein(bool_0, none_type_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    str_0 = "~Ndax"
#    module_0.levenshtein(list_0, str_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "x8m:u_uM2'o"
    bytes_0 = b"\x89c\xa3\xc8\x05vr\xcf\xa1\xb2\xf6\xfb"
#    module_0.levenshtein(str_0, bytes_0)
