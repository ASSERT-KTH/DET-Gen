# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import quicksort as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    complex_0 = -1190.3454 + 1412.674j
    module_0.quicksort(complex_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_0.quicksort(none_type_0)


def test_case_2():
    bytes_0 = b" T\xf88K\x1c>\x117"
    var_0 = module_0.quicksort(bytes_0)
    var_1 = module_0.quicksort(bytes_0)
    var_2 = module_0.quicksort(var_0)
