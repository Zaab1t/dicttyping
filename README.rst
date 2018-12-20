datatyping
==========

.. image:: https://travis-ci.org/carlbordum/datatyping.svg?branch=master
    :target: https://travis-ci.org/carlbordum/datatyping

.. image:: https://readthedocs.org/projects/datatyping/badge/?version=latest
    :target: http://datatyping.readthedocs.io


``datatyping`` is a pure Python library with no dependencies that you can use to
verify whether elements in a data structure have the expected types. Great for
incoming JSON.

.. code-block:: python

    import datatyping
    datatyping.validate([int], [1, 2, 3])

Check out the `documentation <http://datatyping.readthedocs.io>`_ for more usage examples.

Installation
------------

.. code-block:: bash

    $ pip install datatyping

Develop with me :)
------------------

Fork the repository first. Then use the following lines to setup:

.. code-block:: bash

    $ git clone https://github.com/YOUR_USERNAME/datatyping
    $ cd datatyping
    $ virtualenv venv
    $ . venv/bin/activate
    $ python setup.py develop

Run tests:

.. code-block:: bash

    $ pip install pytest hypothesis
    $ python -m pytest

Build documentation:

.. code-block:: bash

    $ make -C docs/ html


Notes
-----
* Inspired by `"How Python Makes Working With Data More Difficult in the Long Run" <https://jeffknupp.com/blog/2016/11/13/how-python-makes-working-with-data-more-difficult-in-the-long-run/>`_.
* Any and all contributions are welcome.
* Please open an issue if you think we can help.
* Suggest anything you want to see support for!
