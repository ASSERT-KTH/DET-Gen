# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_126 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    module_0.func(*bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xf5I\x9cql\xb7;d]\x8b8\x89.zT8;\xec"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    list_1 = [bytes_0, var_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"a"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    list_1 = [bytes_0, var_0]
    module_0.func(*list_1)
