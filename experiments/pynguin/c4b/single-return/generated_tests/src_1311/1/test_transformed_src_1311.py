# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1311 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"H?v%\xdb\x99S\xf2\xe40\xca\xb85w\xe7\xff"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 12
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()
