# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2267 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "}2/*"
    list_0 = [str_0]
    none_type_0 = None
    var_0 = module_0.func(*list_0)
    assert var_0 == "}2/*"
    object_0 = module_1.object()
#    module_0.func(*none_type_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x02\n \xfe\xc1\x8dJ\xc3\xc9\xecy\xaf\xc6\x83"
    list_0 = [bytes_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "\t@:Q*r6EM|Wf0#"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "\t@:Q*r6EM|Wf0#"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "}2/*"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "}2/*"
    var_1 = module_0.func(*var_0)
    assert var_1 == "}"
    var_2 = module_0.func(*var_0)
    assert var_2 == "}"
    var_3 = module_0.func(*var_1)
    assert var_3 == "}"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "Q}2/*"
    var_0 = module_0.func(*str_0)
    assert var_0 == "q"
    var_1 = module_0.func(*var_0)
    assert var_1 == "Q"
    list_0 = [str_0]
    var_2 = module_0.func(*list_0)
    assert var_2 == "q}2/*"
#    module_0.func()
