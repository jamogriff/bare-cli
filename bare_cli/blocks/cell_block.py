from .abstract_block import AbstractBlock
from colorama import Style

class CellBlock(AbstractBlock):

    def __init__(self, content: str, width: int, *, header: bool = False):
        self.content = " " + content + " "
        self.width = width
        self.block_start = "|"
        self.block_end = "|"
        self.header = header

    def __str__(self) -> str:
        return self.aligned

    @property
    def raw(self) -> str:
        return self.content

    @property
    def colorized(self) -> str:
        if self.header:
            return Style.DIM + self.block_start + Style.RESET_ALL + Style.BRIGHT + self.content + Style.RESET_ALL
        else:
            return Style.DIM + self.block_start + Style.RESET_ALL + self.content + Style.RESET_ALL

    @property
    def aligned(self) -> str:
        return self._align(" ", "<", self.width)

