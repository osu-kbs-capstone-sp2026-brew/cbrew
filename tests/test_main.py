"""Tests for main module."""

from main import add_numbers, greet


class TestGreet:
    """Tests for the greet function."""

    def test_greet_with_name(self):
        """Test greeting with a specific name."""
        assert greet("Alice") == "Hello, Alice!"

    def test_greet_default(self):
        """Test greeting with default name."""
        assert greet() == "Hello, World!"

    def test_greet_empty_string(self):
        """Test greeting with empty string defaults to World."""
        assert greet("") == "Hello, World!"

    def test_greet_with_special_characters(self):
        """Test greeting with special characters."""
        assert greet("Dr. Smith") == "Hello, Dr. Smith!"


class TestAddNumbers:
    """Tests for the add_numbers function."""

    def test_add_positive_integers(self):
        """Test adding positive integers."""
        assert add_numbers(2, 3) == 5.0

    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        assert add_numbers(-5, -3) == -8.0

    def test_add_mixed_signs(self):
        """Test adding numbers with different signs."""
        assert add_numbers(10, -3) == 7.0

    def test_add_floats(self):
        """Test adding floating point numbers."""
        assert add_numbers(1.5, 2.5) == 4.0

    def test_add_zero(self):
        """Test adding with zero."""
        assert add_numbers(5, 0) == 5.0
        assert add_numbers(0, 0) == 0.0
