# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import next_permutation as module_0


def test_case_0():
    bytes_0 = b"#\xbb\xe5\x01\xae\xb0\x18H\xc0\xf3\x8e\xabi\xbfL\x9a\xeb\xb1\x7f"
    var_0 = module_0.next_permutation(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    tuple_0 = (bool_0,)
    var_0 = module_0.next_permutation(tuple_0)
    module_0.next_permutation(var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -431
    module_0.next_permutation(int_0)