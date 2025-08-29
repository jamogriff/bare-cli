from colorama import Fore, Style
from .block import Block


class BlockFactory:
    """Houses low-level ANSI styling to create Block instances."""

    BLOCK_START = "[ "
    BLOCK_END = " ] "
    CHILD_BLOCK_END = "| "

    def make(self, colorama_color: str, value: str) -> Block:
        """Return a colorized string bookended in block characters.

        Example: [ INFO ]
        """

        string = self.BLOCK_START + value + self.BLOCK_END
        ansi_string = (
            Style.DIM
            + self.BLOCK_START
            + Style.RESET_ALL
            + Style.BRIGHT
            + colorama_color
            + value
            + Fore.RESET
            + Style.RESET_ALL
            + Style.DIM
            + self.BLOCK_END
        )

        return Block(string, ansi_string)

    def make_child(self, parent_type: str) -> Block:
        """Return a nested block element that has empty content but matches the parent block's length.

        Example:
            [ INPUT ]
                    | < Child block
        """

        parent_block_width = (
            len(self.BLOCK_START) + len(parent_type) + len(self.BLOCK_END)
        )
        string = f"{self.CHILD_BLOCK_END:>{parent_block_width}}"
        ansi_string = Style.DIM + string

        return Block(string, ansi_string)
