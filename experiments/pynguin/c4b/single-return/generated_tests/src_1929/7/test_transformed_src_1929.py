# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1929 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0]
#    module_0.func(*list_0)


def test_case_1():
    str_0 = "I9{/F,7LO4"
    set_0 = {str_0, str_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 8


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


def test_case_3():
    str_0 = "v17\x0cm]81y6]5eoN"
    set_0 = {str_0, str_0, str_0, str_0, str_0, str_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 5


def test_case_4():
    str_0 = "d7W\x0csyq\x0cC6oc"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 8


def test_case_5():
    str_0 = "_8g"
    set_0 = {str_0, str_0, str_0, str_0, str_0, str_0, str_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 5


def test_case_6():
    str_0 = "a2MVG."
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5


#@pytest.mark.xfail(strict=True)
def test_case_7():
    bytes_0 = b":E_\xa5"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == 8
    str_0 = "a82MVG."
    list_0 = [str_0, str_0, str_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == 3
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_8():
    bytes_0 = b":\xe9_\xa5"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == 8
    str_0 = "a1VG."
    list_0 = [str_0, str_0, str_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == 3
#    module_1.object(*var_0)


def test_case_9():
    str_0 = "h3g7eOLy"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5


#@pytest.mark.xfail(strict=True)
def test_case_10():
    bytes_0 = b"\t3W\xa2\xc5\xd4k-\x17\xd6\x1e\x90"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 8
    str_0 = "h1(7ey"
    list_1 = [str_0, bytes_0, str_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == 8
    var_2 = module_0.func(*list_1)
    assert var_2 == 3
#    module_1.object(**var_0)


#@pytest.mark.xfail(strict=True)
def test_case_11():
    bytes_0 = b"\t3W\xa2\xc5\xd4k-\x17\xd6\x1e\x90"
    var_0 = module_1.object()
    str_0 = "h8eS"
    list_0 = [str_0, bytes_0, str_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == 3
#    module_0.func(*var_0)
