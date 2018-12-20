__all__ = ["validate", "customtype"]
__author__ = "Carl Bordum Hansen"
__license__ = "MIT"


import collections.abc
import reprlib
import warnings


# Open questions:
#     how should sets be handled?
#     should we handle collections.abc.MappingView?


def _make_typeerror(structure, actual_data):
    if isinstance(structure, type):
        classname = structure.__name__
    else:
        classname = structure.__class__.__name__

    error_msg = '%s is of type %s, expected type %s' % (
        reprlib.repr(actual_data),
        actual_data.__class__.__name__,
        classname
    )
    return TypeError(error_msg)


def _make_valueerror(structure, actual_data):
    error_msg = '%s has the wrong length. Expected %d, got %d.' % (
        reprlib.repr(actual_data),
        len(structure),
        len(actual_data),
    )
    return ValueError(error_msg)


def customtype(check_function):
    """Decorate a function, so it can be used for type checking.

    Now deprecated, any function or callable can be used for type checking as long
    as it raises the proper exceptions.

    Example
    -------
        >>> @customtype
        ... def two_item_list(lst):
        ...     if len(lst) != 2:
        ...         raise TypeError('length %d!!!' % len(lst))
        ...
        >>> validate([two_item_list], [[1, 2], [3, 4]])
        >>> validate([two_item_list], [[1, 2], [3, 4, 5]])
        TypeError: length 3!!!

    Note
    ----
        Sets the `check_function.__datatyping_validate` attribute.

    Parameters
    ----------
    check_function : function
        Function that should be used to type check.

    """
    warnings.warn('The @customtype decorator is no longer needed', DeprecationWarning)
    check_function.__datatyping_validate = True
    return check_function


def validate(structure, data, *, strict=True):
    """Verify that values in a dataset are of correct types.

    Example
    -------
        >>> validate([str], ['a', 'b', 'c'])
        >>> validate(
        ...     {'id': int, 'lucky_numbers': [int]},
        ...     {'id': 700, 'lucky_numbers': [1, 3, 7, 13]}
        ... )
        >>> validate([int], [1, 2, 3, 4.5])
        TypeError: 4.5 is of type float, expected type int.

    Parameters
    ----------
    structure : type or collection of types
        The data structure that `data` should follow.
        It can also be a function or callable that takes a value and raises exceptions
        if the check fails. It is highly recommended to follow the exception conventions
        for this library.
    data : anything
        The data you want type checked.
    strict : bool
        Dicts in `data` must have the **exact** keys specified in
        `structure`. No more.

    Raises
    ------
    TypeError
        If an elements in `data` has wrong type.
    ValueError
        If the length of `structure` doesn't make sense for validating
        `data`.
    KeyError
        If a dict in `data` misses a key or `strict` is True and a dict
        has keys not in `structure`.

    """
    if isinstance(structure, collections.abc.Sequence) and not isinstance(data, str):
        if not isinstance(data, type(structure)):
            raise _make_typeerror(structure, data)

        if len(structure) == 1:  # All items should be of the same type
            for item in data:
                validate(structure[0], item, strict=strict)
        elif len(structure) != len(data):
            raise _make_valueerror(structure, data)
        else:
            for type_, item in zip(structure, data):
                validate(type_, item, strict=strict)
    elif isinstance(structure, collections.abc.Mapping):
        if not isinstance(data, type(structure)):
            raise _make_typeerror(structure, data)

        if strict and len(structure) != len(data):
            raise KeyError(reprlib.repr(set(structure.keys()) ^ set(data.keys())))
        for key, type_ in structure.items():
            item = data[key]  # or KeyError :)
            validate(type_, item, strict=strict)
    elif isinstance(structure, type):
        if not isinstance(data, structure):
            raise _make_typeerror(structure, data)
    elif callable(structure):
        structure(data)
    else:
        raise TypeError(
            'The given type mask %s is neither a structure nor a callable' % structure
        )
