# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2362 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xf9]\xdf \r\xd0\x80\x92\x85\r\x99\xf5"
    list_0 = [bytes_0, bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b""
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "t1-O\\=Kuzw"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".t.1.-.\\.=.k.z.w"
    int_0 = 1978
    int_1 = 3687
    list_1 = [int_0, int_1]
    module_0.func(*list_1)
