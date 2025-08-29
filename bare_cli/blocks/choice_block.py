from colorama import Fore, Style
from .abstract_block import AbstractBlock

class ChoiceBlock(AbstractBlock):
    """Represents a string before and after adding ANSI values.

    Blocks are the core visual identity of BareCLI and are the only components that contain color.
    """

    WIDTH = 8

    def __init__(self, choice: int, color: str):
        self.content = str(choice)
        self.color = color

    def __str__(self) -> str:
        return self.aligned

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
        )

    @property
    def aligned(self) -> str:
        return self._pad("", ">", self.WIDTH)




