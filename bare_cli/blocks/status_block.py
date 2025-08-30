from colorama import Fore, Style
from .abstract_block import AbstractBlock
from ..enums import Status


class StatusBlock(AbstractBlock):
    """Return a colorized status bookended in block characters with ample spacing.

    StatusBlocks are always displayed in the left sidebar and right padded. They give a
    quick visual indication of the type of content that is immediately to the right.

    Example: [ ERROR ] .. Main content here
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
        return self._align(".", "<", self.SIDEBAR_WIDTH)
