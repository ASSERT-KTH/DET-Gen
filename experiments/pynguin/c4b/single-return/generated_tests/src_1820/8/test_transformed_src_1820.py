# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1820 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xb2\xc8\xef\xbf\xb1\xed\xea\xdc\x1e\x80\xfb\x89\xa2\xb7Q\xde\xb8\xdd)"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "NO"
#    module_0.func()


def test_case_1():
    int_0 = -1252
    bool_0 = False
    list_0 = [int_0, int_0, bool_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x9c\x0b`\x8d\xbc<M\xa0\xf66\xa3!T"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "YES"
#    module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b'\x07\xc3`\xbf\x05R\x9aV\xddi+"1y\xa0<Z\xd8\x9d'
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "YES"
    object_0 = module_1.object()
    var_1 = module_0.func(*bytes_0)
    assert var_1 == "YES"
    object_1 = module_1.object()
#    module_0.func(*object_1)
