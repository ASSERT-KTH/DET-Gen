# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_path_length as module_0
import node as module_1


def test_case_0():
    float_0 = 1734.934
    var_0 = module_0.shortest_path_length(float_0, float_0, float_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "F)iH"
#    module_0.get(str_0, str_0)


def test_case_2():
    str_0 = ""
    var_0 = module_0.get(str_0, str_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 1734.934
#    module_0.insert_or_update(float_0, float_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = 3758.4
    str_0 = "ghwu"
#    module_0.shortest_path_length(float_0, float_0, str_0)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "F)iH"
    var_0 = module_1.Node(successor=str_0, successors=str_0, outgoing_nodes=str_0)
#    module_0.shortest_path_length(var_0, var_0, str_0)


def test_case_6():
    str_0 = "F)-i2"
    node_0 = module_1.Node(successor=str_0, predecessors=str_0, incoming_nodes=str_0)
    var_0 = module_0.shortest_path_length(node_0, node_0, str_0)
    assert var_0 == pytest.approx(1e309, abs=0.01, rel=0.01)


def test_case_7():
    str_0 = "R1"
    list_0 = [str_0]
    var_0 = module_0.insert_or_update(list_0, str_0)


def test_case_8():
    str_0 = "R1"
    list_0 = [str_0]
    var_0 = module_0.get(list_0, str_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
def test_case_9():
    bytes_0 = b"\xa5?"
    list_0 = [bytes_0, bytes_0]
#    module_0.insert_or_update(list_0, list_0)


def test_case_10():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    list_1 = [list_0, list_0, list_0, list_0]
    var_0 = module_0.get(list_1, bool_0)
    assert var_0 is False
    str_0 = "R1"
    list_2 = [str_0]
    var_1 = module_0.get(list_2, str_0)
    assert var_1 == 0
