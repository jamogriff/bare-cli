from .abstract_block import AbstractBlock
from colorama import Style

class BorderBlock(AbstractBlock):

    def __init__(self, width: int):
        self.width = width
        self.block_start = "+"
        self.block_end = "+"

    def __str__(self) -> str:
        return self.aligned

    @property
    def raw(self) -> str:
        return self.block_start

    @property
    def colorized(self) -> str:
        return Style.DIM + self.block_start

    @property
    def aligned(self) -> str:
        return self._align("-", "<", self.width)

