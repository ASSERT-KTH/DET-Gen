# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_258 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    bytes_0 = b'\xd5\x18\xcef]z\x9e\x19\x86\x9c"P8'
    var_0 = module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b'\xd5\x18\xcef\xe7z\xbc\x19\x86\x9c"P\x07'
    var_0 = module_0.func(*bytes_0)
    module_1.object(**var_0)
