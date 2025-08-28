from colorama import Style
from .styled_string import StyledString

class StyledStringFormatter:
    """Formats StyledStrings with consistent padding."""

    STANDARD_RIGHT_PADDING = 8
    OPTION_LEFT_PADDING = 3


    def add_right_padding(self, string: StyledString) -> str:
        return self._format_styled_string(string, '.', '<', self.STANDARD_RIGHT_PADDING)

    def add_left_padding(self, string: StyledString) -> str:
        return self._format_styled_string(string, '', '>', self.OPTION_LEFT_PADDING)

    def _format_styled_string(self, string: StyledString, fill: str, align: str, width: int) -> str:
        """Format a token string by formatting the untokenized first and then replacing."""

        # TODO: need to also pass in message... blah!!
        format_spec = f"{fill}{align}{width}"
        formatted = f"{string.raw:{format_spec}} {Style.RESET_ALL + message}"
        return formatted.replace(string.raw, string.decorated, 1)

