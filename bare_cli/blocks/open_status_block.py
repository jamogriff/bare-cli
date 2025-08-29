from colorama import Fore, Style
from .abstract_block import AbstractBlock
from .status_block import StatusBlock

class OpenStatusBlock(AbstractBlock):
    """Return a nested block element that has empty content but matches the parent block's length.

    Example:
        [ INPUT ]
                | < Child block
    """

    CHILD_BLOCK_END = "› "

    def __init__(self, parent: StatusBlock):
        self.parent_block_width = len(parent.raw)

    def __str__(self) -> str:
        return self.aligned

    @property
    def raw(self) -> str:
        return f"{self.CHILD_BLOCK_END:>{self.parent_block_width}}"

    @property
    def colorized(self) -> str:
        return Style.DIM + self.raw

    @property
    def aligned(self) -> str:
        return self._pad("", "<", self.SIDEBAR_WIDTH)




