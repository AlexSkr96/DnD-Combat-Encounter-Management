class InsuficcientAPException(Exception):
    def __init__(self, message: str|None = None):
        self.message = message if message else "Not enough AP, action won't be performed!"

    # def __str__(self):
    #     return self.message


class GearSlotOccupiedException(Exception):
    def __init__(self, message: str|None = None):
        self.message = message if message else "Gear slot is already occupied!"
