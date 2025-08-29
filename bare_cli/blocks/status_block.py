from colorama import Fore, Style
from .abstract_block import AbstractBlock
from ..enums.status import Status


class StatusBlock(AbstractBlock):
    """Represents a string before and after adding ANSI values.

    Blocks are the core visual identity of BareCLI and are the only components that contain color.
    Return a colorized string bookended in block characters.

    Example: [ INFO ]
    """

    def __init__(self, status: Status, color: str):
        self.content = status.value
        self.color = color
        self.block_start = self.BLOCK_START + " "
        self.block_end = " " + self.BLOCK_END + " "

    def __str__(self) -> str:
        return self.aligned

    @property
    def raw(self) -> str:
        return self.block_start + self.content + self.block_end

    @property
    def colorized(self) -> str:
        return (
            Style.DIM
            + self.block_start
            + Style.RESET_ALL
            + Style.BRIGHT
            + self.color
            + self.content
            + Fore.RESET
            + Style.RESET_ALL
            + Style.DIM
            + self.block_end
        )

    @property
    def aligned(self) -> str:
        return self._pad(".", "<", self.SIDEBAR_WIDTH)
