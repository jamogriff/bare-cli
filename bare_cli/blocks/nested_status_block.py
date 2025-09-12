from colorama import Style
from .abstract_block import AbstractBlock
from .status_block import StatusBlock


class NestedStatusBlock(AbstractBlock):
    """Return a nested block element that pads to the parent StatusBlock's length.

    Like StatusBlocks, these are always displayed in the left sidebar; however, these are used
    to keep the vertical log nature of BareCLI clean by not spamming the same status on every line.

    Example:
        [ INPUT ]
                |  < Child block
                |  < Child block
                |  < Child block
        [ INPUT ]
    """

    CHILD_BLOCK_END = "| "

    def __init__(self, parent: StatusBlock, *, no_fill: bool = False):
        self.parent_block_width = len(parent.raw)
        self.no_fill = no_fill

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
        if self.no_fill:
            char = ""
        else:
            char = "›"

        return self._align(char, "<", self.SIDEBAR_WIDTH)

