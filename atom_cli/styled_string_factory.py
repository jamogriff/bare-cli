from colorama import Fore, Style
from .styled_string import StyledString

class StyledStringFactory:
    """House low-level ANSI styling to create instances of StyledStrings."""

    def make_bracket(self, colorama_color: str, value: str) -> StyledString:
        string = StyledString(value)
        string.decorated = Style.DIM + "[ " + Style.RESET_ALL + Style.BRIGHT + colorama_color + value + Fore.RESET + Style.RESET_ALL + Style.DIM + " ] "

        return string

    def make_open_bracket(self, colorama_color: str, value: str) -> StyledString:
        string = StyledString(value)
        string.decorated = Style.DIM + "| " + Style.RESET_ALL + colorama_color + value + Fore.RESET + Style.DIM
 
        return string

