# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_549 as module_0


def test_case_0():
    bytes_0 = b"\x13+\x1b9\xc37%\xbc\xbe\x1e\xe4\xb8\x81\x87'T1"
    var_0 = module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x14\n\n\xbb\x14\xe4\xe2\x97=%$\x04\xc6nrGO"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*var_0)
#    module_0.func()
