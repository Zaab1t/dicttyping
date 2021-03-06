Structure Generation
====================

It can be tedious to type out a structure. Luckily `datatyping` comes with a
useful submodule for that called `printer`.

.. code-block:: python

    >>> from datatyping.printer import pprint
    >>> import requests
    >>> r = requests.get('http://httpbin.org/anything')
    >>> pprint(r.json())
    {   
        'args': dict,
        'data': str,
        'files': dict,
        'form': dict,
        'headers': {   
            'Accept': str,
            'Accept-Encoding': str,
            'Connection': str,
            'Host': str,
            'User-Agent': str,
        },
        'json': NoneType,
        'method': str,
        'origin': str,
        'url': str,
    }

Printer module
--------------

.. automodule:: datatyping.printer

.. autofunction:: datatyping.printer.pprint

.. autofunction:: datatyping.printer.pformat
