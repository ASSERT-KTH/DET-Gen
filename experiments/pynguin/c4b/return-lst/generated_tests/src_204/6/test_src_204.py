# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_204 as module_0


def test_case_0():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)


def test_case_1():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x98\xeb\xbc\xb8\x0f&\x12%\xe0\xfb\xc6\xe5\x14\xc1\xf2Ms2X\x9b"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b'\xc7"\x08\xba\xfd\x9b\x89\xdb\xd0Q\x81v\x04'
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xd1\x85\xd3E;\xa8+o\xfeX'\xcd%\xe2\xec\x04\x89"
    var_0 = module_0.func(*bytes_0)
    module_0.func()
