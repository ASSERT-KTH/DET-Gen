# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_path_lengths as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    module_0.shortest_path_lengths(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.shortest_path_lengths(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    set_0 = set()
    bool_0 = False
    var_0 = module_0.shortest_path_lengths(bool_0, set_0)
    list_0 = []
    module_0.shortest_path_lengths(list_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    set_0 = set()
    bool_0 = True
    var_0 = module_0.shortest_path_lengths(bool_0, set_0)
    list_0 = []
    module_0.shortest_path_lengths(list_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 65
    set_0 = set()
    var_0 = module_0.shortest_path_lengths(int_0, set_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "collections.defaultdict"
    )
    assert len(var_0) == 4225
    module_0.shortest_path_lengths(int_0, int_0)
