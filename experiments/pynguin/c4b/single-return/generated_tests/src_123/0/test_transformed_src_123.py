# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_123 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"j\xb8R\xd6.>\x91#'S\xdcn^:;\x91"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 80139286383178377475869705764864
    bytes_1 = b"\xde\xde\r\xab{\xaf\xd9\xbf\xe4f9\xc7\xc6"
    var_1 = module_0.func(*bytes_1)
    assert var_1 == 6657711438921599646559005312627040143160149312353464127108472111104
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -1665.39
    list_0 = [float_0]
#    module_0.func(*list_0)
