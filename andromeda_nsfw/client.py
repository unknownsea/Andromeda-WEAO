# andromeda_nsfw/client.py
from .enums import NsfwTypes

class Client:
    def __init__(self):
        pass

    def get_supported(self, enum = NsfwTypes):
        filtered_supported = []
        for name, value in vars(enum).items():
            if not name.startswith("__"):  # Exclude special/magic attributes
                filtered_supported.append(value)

        return filtered_supported
