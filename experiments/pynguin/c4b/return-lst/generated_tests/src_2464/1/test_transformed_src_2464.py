# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2464 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1615
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"!\xd2/\xd9U\x80u\x1e"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\n\x81L\xa4\xfc\xb2\xc9L"
    var_0 = module_0.func(*bytes_0)
#    module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 1
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_1.object()
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"<\xa8\xc0\x9f"
    var_0 = module_0.func(*bytes_0)
#    module_1.object(**var_0)
