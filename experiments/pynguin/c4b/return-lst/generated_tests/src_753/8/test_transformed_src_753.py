# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_753 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"N\x92\xda}\x9ad\xe8\xaaVA\xb5\x99\xda\x13\x06\x04\xa8'\xc9\xd2"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    bool_0 = False
    list_1 = [list_0, bool_0]
    list_2 = [list_1, list_0]
    list_3 = [list_2, list_2, list_1, list_0]
    var_0 = module_0.func(*list_3)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    list_0 = []
    list_1 = [list_0]
    list_2 = [list_1, list_1, list_1, list_0]
    var_0 = module_0.func(*list_2)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    list_0 = []
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    list_0 = []
    list_1 = [list_0, list_0, list_0, list_0]
    var_0 = module_0.func(*list_1)
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    list_0 = []
    list_1 = [list_0, list_0]
    list_2 = [list_1, list_1, list_1, list_0]
    var_0 = module_0.func(*list_2)
#    module_0.func()