# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import max_sublist_sum as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "#eC<$&o57!-n\\vRx"
    module_0.max_sublist_sum(str_0)


def test_case_1():
    bytes_0 = b"\xc8q\xc3\xea"
    var_0 = module_0.max_sublist_sum(bytes_0)
    assert var_0 == 742
    bool_0 = False
    set_0 = {bool_0}
    var_1 = module_0.max_sublist_sum(set_0)
    assert var_1 == 0
