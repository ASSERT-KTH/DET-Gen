# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2111 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b'\x07\xae\x9c\x89\x96d\xe4"\x92~\xeb>Z\x08\xe0\x8c<\x8f\x81'
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "@dz)qu_HRn\x0c'k+`a"
    list_0 = [str_0, str_0, str_0]
    module_0.func(*list_0)
