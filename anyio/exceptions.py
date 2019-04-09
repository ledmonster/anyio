from traceback import format_exception
from typing import Sequence
import trio


class ExceptionGroup(trio.MultiError):
    """Raised when multiple exceptions have been raised in a task group."""
    pass


class CancelledError(Exception):
    """Raised when the enclosing cancel scope has been cancelled."""


class IncompleteRead(Exception):
    """"
    Raised during ``read_exactly()`` if the connection is closed before the requested amount of
    bytes has been read.

    :ivar bytes data: bytes read before the stream was closed
    """

    def __init__(self) -> None:
        super().__init__('The stream was closed before the read operation could be completed')


class DelimiterNotFound(Exception):
    """
    Raised during ``read_until()`` if the maximum number of bytes has been read without the
    delimiter being found.

    :ivar bytes data: bytes read before giving up
    """

    def __init__(self, max_bytes: int) -> None:
        super().__init__('The delimiter was not found among the first {} bytes'.format(max_bytes))


class ClosedResourceError(Exception):
    """Raised when a resource is closed by another task."""


class TLSRequired(Exception):
    """Raised when a TLS related stream method is called before the TLS handshake has been done."""


class ResourceBusyError(Exception):
    """Raised when two tasks are trying to read from or write to the same resource concurrently."""

    def __init__(self, action: str):
        super().__init__('Another task is already {} this resource'.format(action))
