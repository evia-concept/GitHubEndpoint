from collaborators.messages.error_messages import (
    null_argument_exception,
    not_allowed_argument_exception,
)


class Validator:
    @staticmethod
    def check_valid_name(name):

        if (name == None) or (name == ""):
            raise ValueError(null_argument_exception)

        if any(element in name for element in ["/", "\\"]):
            raise ValueError(not_allowed_argument_exception)
