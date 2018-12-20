import string

import pytest
from hypothesis import given, assume
from hypothesis.strategies import lists, integers, text, one_of, composite, \
    fixed_dictionaries

from datatyping.datatyping import validate


# Custom checker definitions

def positive_int(i):
    if i < 1:
        raise TypeError('%d is negative' % i)


def title(s):
    if s != s.title():
        raise TypeError('%s is not a title' % s)


def two_item_list(lst):
    if len(lst) != 2:
        raise TypeError('list contains %d items, not 2' % len(lst))


# Tests

@given(num=integers(min_value=1))
def test_simple_pos_int(num):
    assert validate(positive_int, num) is None


@given(words=text(alphabet=string.ascii_lowercase + ' ').map(str.title))
def test_simple_title(words):
    assert validate(title, words) is None


@given(lst=lists(integers(), min_size=2, max_size=2))
def test_simple_ti_list(lst):
    assert validate(two_item_list, lst) is None


@given(num=integers(max_value=-1))
def test_simple_pos_int_error(num):
    with pytest.raises(TypeError):
        validate(positive_int, num)


@given(words=text(alphabet=string.ascii_lowercase + ' '))
def test_simple_title_error(words):
    assume(len(words) > 0)
    assume(not words.isspace())
    with pytest.raises(TypeError):
        validate(title, words)


@given(lst=one_of(lists(integers(), max_size=1),
                  lists(integers(), min_size=3)))
def test_simple_ti_list_error(lst):
    with pytest.raises(TypeError):
        validate(two_item_list, lst)


@given(data=lists(fixed_dictionaries(
    {
        'id': integers(min_value=1),
        'name': text(alphabet=string.ascii_lowercase + ' ').map(str.title)
    }
)))
def test_nested(data):
    type_mask = [
        {'id': positive_int, 'name': title}
    ]

    assert validate(type_mask, data) is None


@given(data=lists(fixed_dictionaries(
    {
        'id': integers(max_value=-1),
        'name': text(alphabet=string.ascii_lowercase + ' ').map(str.title)
    }
)))
def test_nested_error(data):
    assume(len(data) != 0)
    type_mask = [
        {'id': positive_int, 'name': title}
    ]

    with pytest.raises(TypeError):
        validate(type_mask, data)


@composite
def deeply_nested_list(draw):
    return [
        draw(lists(integers(), min_size=2, max_size=2)),
        [
            draw(integers(min_value=1)),
            draw(lists(integers(), min_size=2, max_size=2))
        ],
        [
            draw(text(alphabet=string.ascii_lowercase + ' ').map(str.title))
        ]
    ]


@given(data=deeply_nested_list())
def test_deep_nesting(data):
    type_mask = [two_item_list, [positive_int, two_item_list], [title]]
    assert validate(type_mask, data) is None
