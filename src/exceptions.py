"""Contains all the exceptions used by the package"""
class ConfigValidationTestFailedError(Exception):
    """Exception raised when a test fails"""
    def __init__(self, test: str, failure: dict[str, str | int | list]) -> None:
        self.test = test
        self.failure = failure
    def __str__(self) -> str:
        array = [f"Test failed during configuration validation: {self.test}",
                 "Detailed Error Information:",
                 f"Error Code: {self.failure["error_code"]}",
                 f"Error Message: {self.failure["reason"]}",
                 f"Configuration Path Causing Error: {" / ".join(reversed(self.failure["path"]))}"]

        return "\n".join(array)