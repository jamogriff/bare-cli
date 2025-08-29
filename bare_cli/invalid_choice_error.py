class InvalidChoiceError(Exception):

    def __init__(self, message: str = "User provided invalid choice input."):
        self.message = message
        super().__init__(f"{message}")
