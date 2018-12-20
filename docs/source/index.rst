datatyping
==========

``datatyping`` is a Python library that can verify whether data matches the expected type format.

This makes it useful for stuff that is currently hard in Python such
as documenting incoming data or testing outgoing data.

.. code-block:: python

    >>> import datatyping
    >>> structure = {'status_code': int, 'content': [str]}
    >>> data = {'status_code': 400, 'content': ['Gouda', 'Cheddar']}
    >>> datatyping.validate(structure, data)

This approach ensures early failure in a specific spot if data is malformed or
has changed format unexpectedly. This results in a more explicit codebase that
is easier to maintain.

For more, check out Jeff Knupp's `"How Python Makes Working With Data More
Difficult in the Long Run"
<https://jeffknupp.com/blog/2016/11/13/how-python-makes-working-with-data-more-difficult-in-the-long-run/>`_
which has inspired this library.

Installation
------------

.. code-block:: bash

    $ pip install datatyping

Contents
--------

:ref:`genindex`, :ref:`search`

.. toctree::
   :maxdepth: 2

   validate.rst
   customtype.rst
   printer.rst
