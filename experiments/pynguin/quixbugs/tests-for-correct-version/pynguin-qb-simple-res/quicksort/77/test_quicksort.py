# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import quicksort as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    module_0.quicksort(bool_0)


def test_case_1():
    bool_0 = False
    var_0 = module_0.quicksort(bool_0)


def test_case_2():
    bytes_0 = b"\xeb\x8d1FO\x93;\x19\x18\xa2"
    var_0 = module_0.quicksort(bytes_0)
    bool_0 = False
    var_1 = module_0.quicksort(bool_0)