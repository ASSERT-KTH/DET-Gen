# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2094 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x83J\x8c\t\x17\xafE\xabY\x95{\xca\xfc\x1f8\xf3"
    list_0 = [bytes_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
#    module_0.func(*bool_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "=xe{Jb5\x0cQ;=q%"
    dict_0 = {str_0: str_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == ".=.x.{.j.b.5.\x0c.q.;.=.q.%"
#    module_0.func()
