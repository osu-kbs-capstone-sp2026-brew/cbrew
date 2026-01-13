"""Demo application for cbrew Capstone KBS repository.

This module demonstrates basic Python project structure and testing practices.
"""


def greet(name: str = "World") -> str:
    """Generate a greeting message.

    Args:
        name: The name to greet. Defaults to "World".

    Returns:
        A greeting string.

    Examples:
        >>> greet("Alice")
        'Hello, Alice!'
        >>> greet()
        'Hello, World!'
    """
    if not name:
        name = "World"
    return f"Hello, {name}!"


def add_numbers(a: float, b: float) -> float:
    """Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b

    Examples:
        >>> add_numbers(2, 3)
        5.0
        >>> add_numbers(1.5, 2.5)
        4.0
    """
    return float(a + b)


def main() -> None:
    """Main entry point for the demo application."""
    print("=" * 50)
    print("cbrew - Capstone KBS Demo Repository")
    print("=" * 50)
    print()
    print(greet())
    print(greet("Capstone KBS Team"))
    print()
    print(f"Demo calculation: 2 + 3 = {add_numbers(2, 3)}")
    print()
    print("This demo shows:")
    print("  - Proper Python project structure")
    print("  - Type hints for better code quality")
    print("  - Docstrings for documentation")
    print("  - Functions that can be easily tested")
    print()
    print("Next steps:")
    print("  1. Run tests: uv run pytest")
    print("  2. Check code quality: uv run ruff check .")
    print("  3. Format code: uv run ruff format .")
    print("  4. Type check: uv run pyright")
    print()


if __name__ == "__main__":
    main()
