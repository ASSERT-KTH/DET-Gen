# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import powerset as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"'8\xb6\x84\xd5y4\x1b\xd6\t"
    list_0 = [bytes_0]
    var_0 = module_0.powerset(list_0)
    int_0 = 2540
    module_0.powerset(int_0)


def test_case_1():
    set_0 = set()
    var_0 = module_0.powerset(set_0)
