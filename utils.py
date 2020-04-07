import os
import json

from config import FILENAME


def get_codes():
    if not os.path.exists(FILENAME):
        # first creation
        with open(FILENAME, 'w'):
            return {}
    with open(FILENAME) as f:
        data = json.load(f)
    return data
