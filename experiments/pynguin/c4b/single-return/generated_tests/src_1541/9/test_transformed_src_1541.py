# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1541 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xdc&\x861\xd8s\x17\x83\xd2Z\x9b\xf7\xfa"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 10
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"-\xef\xca]\xafY!\x1f\xdb\x052\x02>\x8e58"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 4
#    module_1.object(**var_0)
