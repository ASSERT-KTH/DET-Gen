# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import pascal as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 414
    var_0 = module_0.pascal(int_0)
    module_0.pascal(var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -960
    var_0 = module_0.pascal(int_0)
    bytes_0 = b"a9WX\xaeCn\xc7}o\x01\xfe/\xb5\xc2"
    var_1 = module_0.pascal(int_0)
    module_0.pascal(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.pascal(none_type_0)