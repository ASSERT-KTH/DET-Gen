# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_906 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "9]ZvL R>m;;q]9c_A"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".9.].z.v.l. .r.>.m.;.;.q.].9.c._"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "a&jehh"
    bytes_0 = b"k\x846\xc7>\xc5~\xce\xae\xd6\r\xf9\xe6H]\x89+\xf9\x14"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: bytes_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == ".&.j.h.h"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "AUs\r#jHS73lRCt"
    bytes_0 = b"G\x92(I\xf4\xad\x82_*\xf2\xfb\r1k\xa4J\xd0"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: bytes_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == ".s.\r.#.j.h.s.7.3.l.r.c.t"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "$=_yq3< (_\x0bnLY9\\("
    bytes_0 = b"k6\xc7>\xc5~\xce\xae\xd6\r\xf9\xe6H\xfc\x89+\xf9\x14"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: bytes_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == ".$.=._.q.3.<. .(._.\x0b.n.l.9.\\.("
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "P4EdP"
    tuple_0 = (str_0,)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == ".p.4.d.p"
    str_1 = "B'pDxdU.+Zp&AB4ez7"
    dict_0 = {str_1: str_1, str_1: str_1, str_1: str_1, str_1: var_0}
    var_1 = module_0.func(*dict_0)
    assert var_1 == ".b.'.p.d.x.d...+.z.p.&.b.4.z.7"
    var_2 = module_0.func(*var_1)
    assert var_2 == ".."
    var_3 = module_0.func(*var_1)
    assert var_3 == ".."
    var_4 = module_0.func(*var_0)
    assert var_4 == ".."
    var_5 = module_0.func(*dict_0)
    assert var_5 == ".b.'.p.d.x.d...+.z.p.&.b.4.z.7"
    var_6 = module_0.func(*dict_0)
    assert var_6 == ".b.'.p.d.x.d...+.z.p.&.b.4.z.7"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "B'pD dU.+Zqp&AB4e"
    bytes_0 = b"k\x846\xc7>\xc5~\xce\xae\xd6\r\xf9\xe6H]\x89+\xf9\x14"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: bytes_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == ".b.'.p.d. .d...+.z.q.p.&.b.4"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "X^y2u#Dd2"
    bytes_0 = b"k\x846\xc7>\xc5~\xce\xae\xd6\r\xf9\xe6H]\x89+\xf9\x14"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: bytes_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == ".x.^.2.#.d.d.2"
    module_1.object(**dict_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "P4EdP"
    tuple_0 = (str_0,)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == ".p.4.d.p"
    str_1 = "4wIp:o=9Uexi(+d"
    bytes_0 = b"k\x846\xc7>\xc5~\x05\xce\xae\xd6\r\xf9\xe6H]\x89+\xf9\x14"
    dict_0 = {str_1: str_1, str_1: str_1, str_1: str_1, str_1: bytes_0}
    var_1 = module_0.func(*dict_0)
    assert var_1 == ".4.w.p.:.=.9.x.(.+.d"
    module_1.object(**dict_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    str_0 = "E\rzO5L6nxfC1aOx"
    tuple_0 = (str_0,)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == ".\r.z.5.l.6.n.x.f.c.1.x"
    none_type_0 = None
    module_0.func(*none_type_0)