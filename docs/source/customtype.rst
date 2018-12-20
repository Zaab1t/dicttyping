Defining Custom Types
=====================

Sometimes, a more specific constraint is required. Such constraints can be imposed by
passing a callable instead of the type as the type mask.

Make sure that the callable follows the exception conventions for the library:

* A ``TypeError`` is raised when an object does not match the constraint.
* A ``ValueError`` is raised when the dimensions of the data don't make sense for the type
  mask

Example
-------

The following example defines a "custom type", that can only be positive
integers.

.. code-block:: python

    from datatyping import validate
    def positive_int(i):
        if i < 1:
            raise TypeError('%d is not positive' % i)

    validate([positive_int], [1, 2, 3, 4])
    validate([positive_int], [1, 2, 3, -4])
    TypeError: -4 is not positive


datatyping.customtype
---------------------

.. autofunction:: datatyping.customtype
