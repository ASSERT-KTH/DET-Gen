# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2038 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"E\xe7Hs\xf4\x19"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"EH4\xf4\x19"
    module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"9\x01\xbf!9\x0c\x066w>\x80\xb2\x05\xf3m<0~\xe8"
    module_0.func(*bytes_0)
