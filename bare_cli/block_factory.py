from colorama import Fore, Style
from .block import Block


class BlockFactory:
    """Houses low-level ANSI styling to create Block instances."""

    def __init__(self, *, block_start: str, block_end: str, child_block_end: str):
        self._block_start = block_start
        self._block_end = block_end
        self._child_block_end = child_block_end

    def make(self, colorama_color: str, value: str) -> Block:
        """Return a colorized string bookended in block characters.

        Example: [ INFO ]
        """

        string = self._block_start + value + self._block_end
        ansi_string = (
            Style.DIM
            + self._block_start
            + Style.RESET_ALL
            + Style.BRIGHT
            + colorama_color
            + value
            + Fore.RESET
            + Style.RESET_ALL
            + Style.DIM
            + self._block_end
        )

        return Block(string, ansi_string)

    def make_child(self, parent_type: str) -> Block:
        """Return a nested block element that has empty content but matches the parent block's length.

        Example:
            [ INPUT ]
                    | < Child block
        """

        parent_block_width = (
            len(self._block_start) + len(parent_type) + len(self._block_end)
        )
        string = f"{self._child_block_end:>{parent_block_width}}"
        ansi_string = Style.DIM + string

        return Block(string, ansi_string)
