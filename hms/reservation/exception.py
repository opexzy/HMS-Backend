# Exception classes
class QuantityOutOfRange(Exception):
    """ The quantity out of availanle range exception"""
    def __init__(self, message="", code=None, params=None):
        if not message:
            message = "Quantity out of avaliable range"
        super().__init__(message, code, params)