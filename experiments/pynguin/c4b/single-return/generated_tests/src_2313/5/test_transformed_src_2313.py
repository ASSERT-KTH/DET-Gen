# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2313 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x1a@\x99\xdb\xa2i"
    list_0 = [bytes_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "w<\nB|0!phaJ9U)D0\x0c>>"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".w.<.\n.b.|.0.!.p.h.j.9.).d.0.\x0c.>.>"
    object_0 = module_1.object()
    list_1 = [object_0, object_0]
#    module_0.func(*list_1)