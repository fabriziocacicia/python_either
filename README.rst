.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/python_either.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/python_either
    .. image:: https://readthedocs.org/projects/python_either/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://python_either.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/python_either/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/python_either
    .. image:: https://img.shields.io/pypi/v/python_either.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/python_either/
    .. image:: https://img.shields.io/conda/vn/conda-forge/python_either.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/python_either
    .. image:: https://pepy.tech/badge/python_either/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/python_either
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/python_either

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

=============
python_either
=============


    A simple, flexible Either monad for handling success and failure in Python.


Features
--------

- **Flexible Either Implementation**: Create instances representing success or failure outcomes.
- **Type Safety**: Leverage Python's strong type system with type variables for failure and success types.
- **Intuitive API**: Use methods like `is_failure`, `is_success`, `get_left`, and `get_success` to interact with your values seamlessly.
- **Composable Handling**: Utilize the `fold` method to consolidate your success and failure logic into a single, elegant call.

Installation
------------

Install EitherPy using pip:

.. code-block:: sh

    pip install git+https://github.com/fabriziocacicia/python_either.git@{version}

Usage
_____

Creating an Either Instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from eitherpy import Either, Failure, Success

    result = Success("Operation succeeded")
    if result.is_success():
        print(result.get_success())  # Output: Operation succeeded
    else:
        print(result.get_left())

Handling Failures
~~~~~~~~~~~~~~~~~

.. code-block:: python

    result = Failure("An error occurred")
    if result.is_failure():
        print(result.get_left())  # Output: An error occurred
    else:
        print(result.get_success())

Using Fold
~~~~~~~~~~

.. code-block:: python

    def handle_failure(failure):
        print(f"Failure: {failure}")

    def handle_success(success):
        print(f"Success: {success}")

    result.fold(handle_failure, handle_success)

Contributing
____________

Contributions are welcome! Feel free to open an issue or submit a pull request on GitHub.

License
~~~~~~~

This project is licensed under the MIT License.



.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.6. For details and usage
information on PyScaffold see https://pyscaffold.org/.
