# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kheapsort as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"o \x12\x80\x00S\xfa\xfa\x97g\xf7Ch!"
    var_0 = module_0.kheapsort(bytes_0, bytes_0)


def test_case_1():
    list_0 = []
    none_type_0 = None
    var_0 = module_0.kheapsort(list_0, none_type_0)
    object_0 = module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    complex_0 = 1627.5083523639114 + 128.3515946721942j
    none_type_0 = None
    var_0 = module_0.kheapsort(complex_0, none_type_0)
    var_1 = module_0.kheapsort(complex_0, complex_0)
    var_2 = module_0.kheapsort(complex_0, complex_0)
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    none_type_1 = None
    var_3 = module_0.kheapsort(list_0, none_type_1)
    module_1.object(*var_3)


@pytest.mark.xfail(strict=True)
def test_case_3():
    complex_0 = -518.0483406989575 - 2060.84j
    list_0 = [complex_0]
    bool_0 = True
    var_0 = module_0.kheapsort(list_0, bool_0)
    module_1.object(*var_0)