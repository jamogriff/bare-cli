from colorama import Fore
from .enums.accent_color import AccentColor

class ColorMapper:
    """Maps an AccentColor enum to a corresponding Colorama Fore color."""

    def from_accent_color(self, accent: AccentColor) -> str:
        match accent:
            case AccentColor.CYAN:
                return Fore.CYAN
            case AccentColor.MAGENTA:
                return Fore.MAGENTA
            case AccentColor.BLUE:
                return Fore.BLUE
            case AccentColor.YELLOW:
                return Fore.YELLOW
            case _:
                # Default to yellow if no match
                return Fore.YELLOW
