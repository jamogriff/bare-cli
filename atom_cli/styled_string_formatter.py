from colorama import Style
from .styled_string import StyledString

class StyledStringFormatter:
    """Formats StyledStrings with consistent padding."""

    STANDARD_RIGHT_PADDING = 12
    OPTION_LEFT_PADDING = 8

    def add_right_padding(self, sidebar: StyledString, main_content: str) -> str:
        return self._format_styled_string(sidebar, main_content, '.', '<', self.STANDARD_RIGHT_PADDING)

    def add_left_padding(self, sidebar: StyledString, main_content: str) -> str:
        return self._format_styled_string(sidebar, main_content, '', '>', self.OPTION_LEFT_PADDING)

    def format_block_element(self, line: StyledString, block_type: str) -> str:
        left_padding = len(block_type) + 3
        return self._format_bare_string(line, '', '>', left_padding)

    def _format_styled_string(self, sidebar: StyledString, main_content: str, fill: str, align: str, width: int) -> str:
        """Format a token string by formatting the untokenized first and then replacing."""

        # TODO: need to also pass in message... blah!!
        format_spec = f"{fill}{align}{width}"
        formatted = f"{sidebar.raw:{format_spec}} {Style.RESET_ALL + main_content}"
        return formatted.replace(sidebar.raw, sidebar.decorated, 1)

