from .abstract_block import AbstractBlock
from colorama import Fore, Style


class CellBlock(AbstractBlock):

    def __init__(self, content: str, width: int, color: str | None = None):
        self.content = " " + content + " "
        self.width = width
        self.block_start = "|"
        self.block_end = "|"
        self.color = color

    def __str__(self) -> str:
        return self.aligned

    @property
    def raw(self) -> str:
        return self.block_start + self.content

    @property
    def colorized(self) -> str:
        if self.color:
            return (
                Style.DIM
                + self.block_start
                + Style.RESET_ALL
                + Style.BRIGHT
                + self.color
                + self.content
                + Fore.RESET
                + Style.RESET_ALL
            )
        else:
            return (
                Style.DIM
                + self.block_start
                + Style.RESET_ALL
                + self.content
                + Style.RESET_ALL
            )

    @property
    def aligned(self) -> str:
        return self._align(" ", "<", self.width)
