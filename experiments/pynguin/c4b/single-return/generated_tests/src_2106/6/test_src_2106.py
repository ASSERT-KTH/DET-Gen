# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2106 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xeef}U$\xbaH$m8LX\xe4\xfd\xc9\xcf\xd0\xf7"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ""
    set_0 = {str_0, str_0}
    module_0.func(*set_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
