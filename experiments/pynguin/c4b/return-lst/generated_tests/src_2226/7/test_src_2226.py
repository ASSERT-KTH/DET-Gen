# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2226 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xfa\x9f\xc7\xd1f\xc2\xfd\xcer\xc2\x8e\x12"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"q\x9f\xc7Y\xc2\xfdy\xcer\xc2\x8e\x12"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x9d\xfe\x07\xb0\xfd!R\xd30\xf3[\xc6\x19"
    var_0 = module_0.func(*bytes_0)
    module_1.object(*bytes_0)
