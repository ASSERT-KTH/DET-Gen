# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_490 as module_0


def test_case_0():
    bytes_0 = b"$\xc8\xea`{\xfd\x1b\xc8\x7fL\xb7\x1a"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = "Th0d9Am9>OX%\"Y'z"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


def test_case_3():
    str_0 = '$#"h0eI9Y0(G%6#%llio'
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"


def test_case_4():
    str_0 = '$#"h0eI9Y0(G%6#%lloL'
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
