# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_783 as module_0


def test_case_0():
    bytes_0 = b"\xef\x90\x03!\xd7@\xcf"
    var_0 = module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    bytes_0 = b"6\xe6\xd7\xcf"
    var_0 = module_0.func(*bytes_0)
