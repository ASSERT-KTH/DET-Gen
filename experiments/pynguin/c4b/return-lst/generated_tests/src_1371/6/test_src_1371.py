# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1371 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b",e\x80\x95\xe5\x9d\xde\xd2?v\x83\xdf\xe9\x95\x06l\xaa\xcf0\xe8"
    list_0 = [bytes_0]
    module_0.func(*list_0)
