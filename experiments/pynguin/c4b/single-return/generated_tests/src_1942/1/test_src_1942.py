# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1942 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b'\xd6"\xac=4\xcd\x99\xe3)l\xb5\n\xb4'
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 1
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\t!\x88\x1a\xdaA\x92\xb9Gt\xf14\xaa"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 37
    module_0.func()
