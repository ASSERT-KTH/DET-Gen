# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_460 as module_0


def test_case_0():
    bytes_0 = b"|\xe0\x16\xc4\x8ffS\x8c\x89|\xd9Y\x85\xed"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()