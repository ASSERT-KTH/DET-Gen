# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lcs_length as module_0


def test_case_0():
    str_0 = "XCXqk6A(g\r7K\\=:o\x0c"
    var_0 = module_0.lcs_length(str_0, str_0)
    assert var_0 == 17


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    var_0 = module_0.lcs_length(list_0, list_0)
    assert var_0 == 0
    dict_0 = {}
    var_1 = module_0.lcs_length(list_0, dict_0)
    assert var_1 == 0
    none_type_0 = None
    module_0.lcs_length(none_type_0, none_type_0)