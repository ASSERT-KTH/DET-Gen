# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2202 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)


def test_case_2():
    bytes_0 = b",\xd8\x8eIj\xba\xb8\xcd\x02\xd7{\x02"
    var_0 = module_0.func(*bytes_0)


def test_case_3():
    bytes_0 = b"\x13I 8n\xac\x86\xc9\xd3j\xaek\x7f\xbb\xb5\x96#"
    var_0 = module_0.func(*bytes_0)


def test_case_4():
    bytes_0 = b"\x14\xd3\xe9\xad\xbe\x88\xe4I\xbb\xa7I\xca\x8a\xb5qh"
    var_0 = module_0.func(*bytes_0)
