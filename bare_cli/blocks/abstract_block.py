from abc import ABC, abstractmethod
from colorama import Style

class AbstractBlock(ABC):

    BLOCK_START = "[ "
    BLOCK_END = " ] "
    SIDEBAR_WIDTH = 12

    @property
    @abstractmethod
    def raw(self) -> str:
        pass

    @property
    @abstractmethod
    def colorized(self) -> str:
        pass

    @property
    @abstractmethod
    def aligned(self) -> str:
        pass


    def _pad(
        self, fill: str, align: str, width: int
    ) -> str:
        """ANSI color codes will break padding because Python counts their characters as strings.

        So we format the intended label first and then replace it with the colored version.
        """

        format_spec = f"{fill}{align}{width}"
        padded = f"{self.raw:{format_spec}}{Style.RESET_ALL}"
        return padded.replace(self.raw, self.colorized, 1)
