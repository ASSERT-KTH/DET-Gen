# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import levenshtein as module_0
import builtins as module_1


def test_case_0():
    str_0 = "5"
    var_0 = module_0.levenshtein(str_0, str_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.levenshtein(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "q"
    bytes_0 = b"\xce\xef\xe3\xcf\xeee\xc6\xf1"
    var_0 = module_0.levenshtein(str_0, str_0)
    assert var_0 == 0
    var_1 = module_1.object()
    module_0.levenshtein(bytes_0, str_0)