# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1534 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "hKt=oia Yk^P-%m"
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"


def test_case_1():
    bytes_0 = b"}H\xd6\xc9\xa3\xda\xa57\xf20 ~\xa6\x0f"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "ht=o\x0bel^PO%lo"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    module_1.object(**var_0)
