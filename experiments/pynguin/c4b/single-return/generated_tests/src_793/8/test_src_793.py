# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_793 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"qzW\x89\\y\x93\xb6\x19\xb8<\xef"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 56
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"qzW\x89\\y\x93\xb6\x19\xb8<\xef"
    bytes_1 = b"\xa8\xe1$\xd1\x9a-\xa1\n}\xb5\xe9\x94\x11\xb13\xfc\xe0z\x90"
    var_0 = module_0.func(*bytes_1)
    assert var_0 == 83
    var_1 = module_0.func(*bytes_0)
    assert var_1 == 56
    module_0.func()
