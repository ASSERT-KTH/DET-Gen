# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1495 as module_0


def test_case_0():
    bytes_0 = b"\xcd"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    bytes_0 = b"%e\xad\xf4\x1d\xb3\xee\x10=>*0"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"]\xef"
    bytes_1 = b"V\nG\xdc\x01"
    set_0 = {bytes_1, bytes_1, bytes_0}
    var_0 = module_0.func(*set_0)
    module_0.func()
