# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_353 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xd7\xde\x91\x8cj\xc9V\xae\xef\x9f\xc4\x85M\xe5\x9b\xfas|="
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 43
    module_0.func(*var_0)


def test_case_1():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
