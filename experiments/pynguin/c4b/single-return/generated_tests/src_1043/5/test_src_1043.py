# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1043 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"S\x81\x055\x05\xcdc\xef\xff\xa8\x9c|!\xd9\xc1\xb1\x04\xd7~\xa7"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "Sheldon"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -193.97
    list_0 = [float_0]
    module_0.func(*list_0)
