from colorama import Fore, Style
from .abstract_block import AbstractBlock

class MiscBlock(AbstractBlock):
    """Represents a string before and after adding ANSI values.

    Blocks are the core visual identity of BareCLI and are the only components that contain color.
    """

    def __init__(self, content: str, color: str, *, add_spacing: bool = False):
        self.content = content
        self.color = color

        if add_spacing:
            self.block_start = self.BLOCK_START + " "
            self.block_end = " " + self.BLOCK_END + " "
        else:
            self.block_start = self.BLOCK_START
            self.block_end = self.BLOCK_END

    def __str__(self) -> str:
        return self.colorized

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
            + Style.RESET_ALL
        )

    @property
    def aligned(self) -> str:
        pass




