from playwright.sync_api import expect as playwright_expect
from typing import Any
import functools


def _wrap_method(method):
    """
    Wrapper for expect methods, converts exceptions to AssertionError.

    In the future, decorators for reporting system can be added here.
    """

    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        except Exception as e:
            # Convert any playwright error to AssertionError
            if not isinstance(e, AssertionError):
                raise AssertionError(str(e)) from e
            raise

    return wrapper


class _ExpectWrapper:
    """
    Proxy for playwright expect with automatic wrapping of all methods.

    Uses __getattr__ to automatically proxy all playwright expect methods
    with conversion of exceptions to AssertionError.
    Custom methods can be added directly to this class.
    """

    def __init__(self, playwright_expect_obj):
        # Use object.__setattr__ to avoid recursion with __getattr__
        object.__setattr__(self, "_playwright_expect", playwright_expect_obj)

    def to_be_staleness(self, **kwargs):
        """
        Custom method to check element staleness.
        Verifies that the element is no longer attached to the DOM (detached).

        Args:
            **kwargs: Parameters to pass to playwright expect (timeout, etc.)

        Raises:
            AssertionError: If the element is still attached to the DOM
        """
        try:
            # Try to check that the element is attached
            # If the element is stale/detached, this will raise an exception
            self._playwright_expect.to_be_attached(**kwargs)
            # If the element is attached, it's NOT stale - raise AssertionError
            raise AssertionError("Element is not stale (still attached to DOM)")
        except Exception as e:
            # Check if the error is related to detached/stale element
            error_msg = str(e).lower()
            if (
                "detached" in error_msg
                or "stale" in error_msg
                or "target closed" in error_msg
            ):
                # Element is indeed stale - this is expected behavior
                return
            # If it's another error, convert to AssertionError
            raise AssertionError(f"Element staleness check failed: {e}") from e

    def __getattr__(self, name):
        """
        Automatically proxies all playwright expect methods.

        Called only when the attribute is not found in the _ExpectWrapper class,
        so custom methods (e.g., to_be_staleness) have priority.
        """
        attr = getattr(self._playwright_expect, name)

        # If it's a method, wrap it to convert exceptions
        if callable(attr):
            return _wrap_method(attr)

        # If it's a property/chain (e.g., not_to), return a wrapped object
        if hasattr(attr, "__self__"):
            return _ExpectWrapper(attr)

        return attr


def expect(actual: Any):
    """
    Wrapper over playwright expect with conversion of exceptions to AssertionError.

    Automatically supports all playwright expect methods.
    To add custom methods, use the _ExpectWrapper class.

    Args:
        actual: Locator, page, or other object to check

    Returns:
        _ExpectWrapper: Proxy object for performing checks

    Example:
        from utils.custom_expect import expect

        expect(page.locator("button")).to_be_visible()
        expect(page.locator("input")).to_have_value("test")
        expect(page.locator(".removed")).to_be_staleness()
    """
    return _ExpectWrapper(playwright_expect(actual))
