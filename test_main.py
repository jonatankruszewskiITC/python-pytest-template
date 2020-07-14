from file import sum_numbers
from pytest import mark
from pytest import raises


@mark.parametrize(
    'args, result, assertion', [
        ((1, 2, 3, 4, 5, 6), 21, "General Case"),
        ((-5, 0), -5, "Negative Number"),
    ]
)
def test_params(args, result, assertion):
    assert sum_numbers(*args) == result, assertion


@mark.parametrize(
    'args, result, assertion', [
        (("hello", 4, 5), raises(TypeError), 'String not being parsed')
    ]
)
def test_exception(args, result, assertion):
    with raises(TypeError):
        assert sum_numbers(*args) == result, assertion

