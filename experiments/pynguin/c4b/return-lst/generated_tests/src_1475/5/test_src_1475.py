# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1475 as module_0


def test_case_0():
    bytes_0 = b"\x1fM\x1e\x85\xb7\x03\xc8k\xa5\x164q\r\x0b\xa4\xb4\xaa"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.func(*none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x1fM\x1e\x85\xb7\x03\xc8\x164q\r\x0b\xb4\xaa"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
    module_0.func()
