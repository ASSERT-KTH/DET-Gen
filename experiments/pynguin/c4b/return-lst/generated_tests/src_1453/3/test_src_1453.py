# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1453 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xeaD\xd6\x94CB{;\xf2\xb3s\x14"
    var_0 = module_0.func(*bytes_0)
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xd6\xd0\xbfl\xf8\x12\xed,\x9a\xcao\x8b\x9b\x19["
    var_0 = module_0.func(*bytes_0)
    bytes_1 = b"\xeaD\xd6\x94CB{;\xf2\xb3s\x14"
    var_1 = module_0.func(*bytes_1)
    module_0.func(*var_1)
