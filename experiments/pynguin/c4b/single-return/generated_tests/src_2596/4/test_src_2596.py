# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2596 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xda\xd2\x8aI6\x82ost\xa7Q\x9fZR\xde(\x1co\x15"
    var_0 = module_0.func(*bytes_0)
    assert (
        var_0
        == "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
    )
    none_type_0 = None
    module_1.object(**none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xda\xd2\x8aI6\x82ost\xa7Q\x9fZR\xde(\x1co\x15"
    var_0 = module_0.func(*bytes_0)
    assert (
        var_0
        == "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
    )
    object_0 = module_0.func(*var_0)
    assert object_0 == "7"
    module_0.func()
