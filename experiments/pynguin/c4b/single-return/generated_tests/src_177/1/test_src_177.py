# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_177 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b'\x07\x04\x08\xd8"\x8aM\x9c3\xbf\xe6v]'
    bool_0 = True
    list_0 = [bytes_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 14
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "Rjt7O~44*l"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 6
    module_0.func()