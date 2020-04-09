import os
import json

FILENAME = 'codes.json'


def get_codes():
    if not os.path.exists(FILENAME):
        # first creation
        with open(FILENAME, 'w'):
            return {}
    with open(FILENAME) as f:
        data = json.load(f)
    return data


def delete_code_file():
    """called from tests"""
    if os.path.exists(FILENAME):
        os.remove(FILENAME)
