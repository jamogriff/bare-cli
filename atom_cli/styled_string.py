
class StyledString:
    """Represents a string before and after adding ANSI values."""

    def __init__(self, value: str):
        self.raw = value
        self.decorated = None
