# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2269 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "Zb"
    none_type_0 = None
    str_1 = "|[bC\x0b).5J"
    dict_0 = {str_0: none_type_0, str_1: none_type_0, str_1: none_type_0}
    object_0 = module_0.func(*dict_0)
    assert object_0 == ".z.b"
    list_0 = [object_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "...z...b"
#    module_0.func()
