__author__ = "Fabrizio Cacicia"
__copyright__ = "Fabrizio Cacicia"
__license__ = "MIT"

from typing import Generic, TypeVar, Union, Callable, Any

# Type variables for failure and success types
F = TypeVar('F')
S = TypeVar('S')


class Either(Generic[F, S]):
    """
    A generic class representing an Either type which can be either a success or a failure.

    Attributes:
        value -- The actual value of the Either instance.
        _is_success -- Boolean flag indicating if the instance is a success.
    """

    def __init__(self, value: Union[F, S], is_success: bool):
        self.value = value
        self._is_success = is_success

    def is_failure(self) -> bool:
        """
        Checks if the instance represents a failure.

        Returns:
            bool: True if it's a failure, False otherwise.
        """
        return not self._is_success

    def is_success(self) -> bool:
        """
        Checks if the instance represents a success.

        Returns:
            bool: True if it's a success, False otherwise.
        """
        return self._is_success

    def get_failure(self) -> F:
        """
        Retrieves the failure value if the instance is a failure.

        Returns:
            F: The failure value.

        Raises:
            ValueError: If the instance is not a failure.
        """
        if self.is_failure():
            return self.value
        raise ValueError("Not a failure value")

    def get_success(self) -> S:
        """
        Retrieves the success value if the instance is a success.

        Returns:
            S: The success value.

        Raises:
            ValueError: If the instance is not a success.
        """
        if self.is_success():
            return self.value
        raise ValueError("Not a success value")

    def fold(self, on_failure: Callable[[F], Any], on_success: Callable[[S], Any]) -> Any:
        """
        Applies the given functions based on the state of the Either instance.

        Args:
            on_failure: Function to apply if the instance is a failure.
            on_success: Function to apply if the instance is a success.

        Returns:
            Any: The result of the applied function.
        """
        if self.is_failure():
            return on_failure(self.value)
        else:
            return on_success(self.value)

    def __eq__(self, other: Any) -> bool:
        """
        Checks equality between this Either instance and another.

        Args:
            other (Any): The object to compare with this instance.

        Returns:
            bool: True if the objects are considered equal, False otherwise.
        """
        if isinstance(other, Either):
            return self.value == other.value and self._is_success == other._is_success
        return False


# Helper functions for creating Either instances
def Failure(value: F) -> Either[F, S]:
    """
    Creates an Either instance representing a failure.

    Args:
        value: The failure value.

    Returns:
        Either[F, S]: An Either instance representing a failure.
    """
    return Either(value, is_success=False)


def Success(value: S) -> Either[F, S]:
    """
    Creates an Either instance representing a success.

    Args:
        value: The success value.

    Returns:
        Either[F, S]: An Either instance representing a success.
    """
    return Either(value, is_success=True)
