# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import quicksort as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -1170
    module_0.quicksort(int_0)


def test_case_1():
    list_0 = []
    var_0 = module_0.quicksort(list_0)


def test_case_2():
    bytes_0 = b"#\x9a\xd7\xeb\xd2\tA\x01\\\x8f\x182B\x14#"
    var_0 = module_0.quicksort(bytes_0)
    var_1 = module_0.quicksort(bytes_0)
    var_2 = module_0.quicksort(bytes_0)
    var_3 = module_0.quicksort(bytes_0)
    var_4 = module_0.quicksort(bytes_0)
