# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import quicksort as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xeb\xeeH"
    dict_0 = {bytes_0: bytes_0}
    module_0.quicksort(dict_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_0.quicksort(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "5f4H&zygM&C"
    var_0 = module_0.quicksort(str_0)
    var_1 = module_0.quicksort(var_0)
    int_0 = 858
    module_0.quicksort(int_0)