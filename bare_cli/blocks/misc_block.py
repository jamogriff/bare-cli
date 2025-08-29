from colorama import Fore, Style
from .abstract_block import AbstractBlock

class MiscBlock(AbstractBlock):
    """Represents a string before and after adding ANSI values.

    Blocks are the core visual identity of BareCLI and are the only components that contain color.
    """

    def __init__(self, content: str, color: str):
        self.content = content
        self.color = color

    def __str__(self) -> str:
        return self.colorized

    @property
    def raw(self) -> str:
        return self.BLOCK_START + self.content + self.BLOCK_END

    @property
    def colorized(self) -> str:
        return (
            Style.DIM
            + self.BLOCK_START
            + Style.RESET_ALL
            + Style.BRIGHT
            + self.color
            + self.content
            + Fore.RESET
            + Style.RESET_ALL
            + Style.DIM
            + self.BLOCK_END
            + Style.RESET_ALL
        )

    @property
    def aligned(self) -> str:
        pass




