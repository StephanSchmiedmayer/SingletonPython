"""Test singleton.singleton."""

from unittest.mock import Mock

import pytest

from better_singleton import singleton


def test_singleton_general_behavior():
    """Test that all Singleton instances act as one."""

    @singleton
    class Test:
        """Singleton class for testing."""

        def __init__(self):
            self.variable = 0

        def inc(self):
            """Increment `variable`."""
            self.variable += 1

    instance1 = Test()
    assert instance1.variable == 0
    instance2 = Test()
    instance1.inc()
    instance3 = Test()
    assert instance1.variable == 1
    assert instance2.variable == 1
    assert instance3.variable == 1


def test_singleton_init():
    """Test that the Singleton's init function only gets called on first instantiation."""
    mock_init = Mock()

    @singleton
    class Test:
        """Singleton class for testing."""

        def __init__(self):
            mock_init()

    Test()
    Test()
    mock_init.assert_called_once()


def test_singleton_init_with_parameters():
    """Test that the Singleton's init function gets called with the right arguments."""
    mock_init = Mock()

    @singleton
    class Test:
        """Singleton class for testing."""

        def __init__(self, test: str, value: int):
            mock_init(test, value=value)

    Test("test", value=2)

    mock_init.assert_called_once_with("test", value=2)


def test_singleton_new_with_parameters():
    """Test that the Singleton's new function gets called with the right arguments."""
    mock_new = Mock()

    @singleton
    class Test:
        """Singleton class for testing."""

        def __new__(cls, test: str, value: int):
            mock_new(test, value=value)

    Test("test", value=2)

    mock_new.assert_called_once_with("test", value=2)


def test_singleton_without_defined_init():
    """Test that Singleton works without having to define `__init__`."""

    @singleton
    class Test:
        """Singleton class for testing."""

        def __init__(self, variable):
            self.variable = variable

    instance1 = Test(0)
    instance2 = Test(10)
    assert instance2.variable == 0
    instance2.variable = 10
    assert instance1.variable == 10


def test_existing_singleton_variable_raises():
    """Test that defining a singleton class with an existing `_singleton` variable raises."""
    with pytest.raises(TypeError):

        @singleton
        class Test:  # pylint: disable-msg=unused-variable
            """Singleton class for testing."""

            _singleton = 0


def test_singleton_wrapper_transparency():
    """Test that Singleton class retains its type."""

    class Test:
        """Singleton class for testing."""

    Test_Singleton = singleton(Test)

    assert issubclass(Test_Singleton, Test)


def test_singleton_class_variable():
    """Test the Singleton does not change class variable's behavior."""

    @singleton
    class Test:
        test = 1

    instance1 = Test()
    assert instance1.test == 1
    instance2 = Test()
    instance1.test = 2
    assert instance2.test == 2
    assert Test().test == 2


def test_singleton_dir():
    """Test that the singleton does not remove any elements from `dir`."""

    @singleton
    class Test:
        def __init__(self):
            self.variable1 = 1

    class TestReference:
        def __init__(self):
            self.variable1 = 1

    test_dir = dir(Test())
    assert all(
        reference_dir_element in test_dir
        for reference_dir_element in dir(TestReference())
    )


@singleton
class SingletonTest:
    """Singleton class for testing in test_singleton_import"""

    def __init__(self):
        self.variable = 0

    def inc(self):
        """Increment `variable`."""
        self.variable += 1


@singleton
class SingletonTest2:
    """Singleton class for testing in test_singleton_import"""

    def __init__(self):
        self.variable = 0

    def inc(self):
        """Increment `variable`."""
        self.variable += 1
