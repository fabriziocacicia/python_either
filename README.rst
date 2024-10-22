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