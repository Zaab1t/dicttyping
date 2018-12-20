Getting Started
===============

The bread and butter of ``datatyping`` is the ``validate`` function.

.. autofunction:: datatyping.validate

Examples
--------

The following short examples are meant to clarify. If these are not sufficient,
let me know (or maybe check out the unit tests :).

.. code-block:: python

    >>> validate([int, str], [1, 'a'])
    >>> validate([[int], [str]], [[1, 2, 3], ['a', 'b', 'c'])

    >>> validate([dict], [{'can have': 1}, {'any keys': 2}])
    >>> validate({'a': int, 'b': str}, {'a': 4, 'b': 'c'})
    >>> validate({'a': int}, {'a': 2, 'b': 'oops'})
    KeyError: {'b'}
    >>> validate({'a': int}, {'a': 2, 'b': 'yay'}, strict=False)
