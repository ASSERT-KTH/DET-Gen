# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_391 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    str_0 = 'u.)i{"R,2|V\x0c6\t '
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = 'u.)i{"R,2|V\x0c3\t '
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "uR)i{&R,2|V\x0c36\t "
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 3
#    module_0.func()
