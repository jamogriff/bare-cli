from dataclasses import dataclass

@dataclass
class Block:
    """Represents a string before and after adding ANSI values.

    Blocks are the core visual identity of BareCLI and are the only components that contain color.
    """

    raw: str
    colorized: str
