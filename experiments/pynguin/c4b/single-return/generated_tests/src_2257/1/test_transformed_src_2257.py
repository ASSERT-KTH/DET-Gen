# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2257 as module_0


def test_case_0():
    str_0 = "u$\r*BE,z:bs*Br\x0cjE*"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "u$\r*BE,z:bs*Br\x0cjE*"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = "u$\r*BE,z:bs*Br\x0cjE*"
    var_0 = module_0.func(*str_0)
    assert var_0 == "U"


def test_case_3():
    str_0 = "u$\r*BE,z:bs*Br\x0cjE*"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "u$\r*BE,z:bs*Br\x0cjE*"
    list_1 = module_0.func(*var_0)
    assert list_1 == "U"
    var_1 = module_0.func(*list_1)
    assert var_1 == "u"


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x08\xd2T\xf0~\x0e\x14\xb6"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
#    module_0.func(*list_0)
