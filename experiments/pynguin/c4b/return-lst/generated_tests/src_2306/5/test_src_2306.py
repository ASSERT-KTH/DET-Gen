# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2306 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xfe\x9aJ$\xaeNkJ\x7f\roQ E)\x94\xe8\r"
    var_0 = module_0.func(*bytes_0)
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"r,\xe1\x92\xb6\xe4\xce\x83yp"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*bytes_0)
    module_0.func()
