"""Singleton definition."""

import functools


def singleton(wrapped_class):
    """Make the decorated class a Singleton.

    Ensures that at most only one instance of the class exists at any point in time.
    `__init__` and `__new__` of the original class get called only once: the first time
    an instance is created. This instance will from then on be the singleton instance.
    Every following call to the constructor of the wrapped class returns the singleton instance.

    The wrapped class cannot have a class variable called `_singleton` as that stores
    the singleton instance. This will throw an error before execution begins.

    Not thread safe during first initialization.

    Raises:
        TypeError: The wrapped class defines a class variable `_singleton`.

    Returns:
        The original class behaving as a singleton.
    """
    if getattr(wrapped_class, "_singleton", None) is not None:
        raise TypeError("Singleton class cannot define an attribute `_singleton`")

    class SingletonWrapper(wrapped_class):
        """Singleton wrapper class."""

        def __init__(self, *args, **kwargs):
            pass

        def __new__(cls, *args, **kwargs):
            if (
                singleton_instance := getattr(wrapped_class, "_singleton", None)
            ) is not None:
                return singleton_instance

            singleton_instance = wrapped_class(*args, **kwargs)
            wrapped_class._singleton = singleton_instance
            return singleton_instance

    functools.update_wrapper(SingletonWrapper, wrapped_class, updated=())

    return SingletonWrapper
