from colorama import Fore, Style
from .abstract_block import AbstractBlock
from ..status import Status

class OpenStatusBlock(AbstractBlock):
    """Return a nested block element that has empty content but matches the parent block's length.

    Example:
        [ INPUT ]
                | < Child block
    """

    CHILD_BLOCK_END = "| "

    def __init__(self, status: Status, color: str):
        self.parent_block_width =(
            len(self.BLOCK_START) + len(status.value) + len(self.BLOCK_END)
        )
        self.color = color

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
        return self._pad(".", "<", self.SIDEBAR_WIDTH)




