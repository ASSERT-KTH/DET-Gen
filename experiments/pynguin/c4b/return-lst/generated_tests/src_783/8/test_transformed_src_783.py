# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_783 as module_0


def test_case_0():
    int_0 = 1382
    int_1 = 2181
    list_0 = [int_0, int_0, int_0, int_1]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"'p\xc1\x97e\xa0#\x84X+7[x\xbb"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()