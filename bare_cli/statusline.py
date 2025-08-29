from enum import Enum

class StatusLine(Enum):
    """Each line in BareCLI is prefixed with a status in the sidebar (e.g. INFO, OK, SUCCESS)."""

    INFO = "INFO"
    SUCCESS = "OK"
    ERROR = "ERROR"
    WARNING = "WARNING"
    INPUT = "INPUT"

