from colorama import Fore, Style
from .styled_string import StyledString

class StyledStringFactory:
    """House low-level ANSI styling to create instances of StyledStrings."""

    BLOCK_START = "[ "
    BLOCK_END = " ] "
    CHILD_BLOCK_END = "| "

    def make_bracket(self, colorama_color: str, value: str) -> StyledString:
        block = self.BLOCK_START + value + self.BLOCK_END
        string = StyledString(block)
        string.decorated = Style.DIM + self.BLOCK_START + Style.RESET_ALL + Style.BRIGHT + colorama_color + value + Fore.RESET + Style.RESET_ALL + Style.DIM + self.BLOCK_END

        return string

    def make_open_bracket(self, status_type: str) -> StyledString:
        total_width = len(self.BLOCK_START) + len(status_type) + len(self.BLOCK_END)
        block = f"{self.CHILD_BLOCK_END:>{total_width}}"

        string = StyledString(block)
        string.decorated = Style.DIM + block 
 
        return string

