# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_908 as module_0


def test_case_0():
    str_0 = "|-}An0Au/"
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    bytes_0 = b"\x81x\xf9\\"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


def test_case_3():
    bytes_0 = b"d\xcem\xb0\xf3:\x1b\x81ux\xeb+\xcb\xcb\x02\x1b"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


def test_case_4():
    bytes_0 = b"\xb2\x03\xa8\x81\x9a\x9a\x9a\x9a\x9a\x9a\x9a"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    list_1 = [bytes_0, var_0, var_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "YES"
    var_2 = module_0.func(*list_1)
    assert var_2 == "YES"
