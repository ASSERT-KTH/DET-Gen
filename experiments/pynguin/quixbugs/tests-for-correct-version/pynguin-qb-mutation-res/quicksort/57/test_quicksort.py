# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import quicksort as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = -2460.4
    module_0.quicksort(float_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_0.quicksort(none_type_0)
    var_1 = module_0.quicksort(var_0)
    var_2 = module_0.quicksort(var_0)
    bytes_0 = b"<#"
    var_3 = module_0.quicksort(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"~H\xf3I\xf6\x87\xa3\x06\x96/\t\x8aZ"
    var_0 = module_0.quicksort(bytes_0)
    var_1 = module_0.quicksort(bytes_0)
    var_2 = module_0.quicksort(var_0)
    var_3 = module_0.quicksort(bytes_0)
    module_1.object(*bytes_0)