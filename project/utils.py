import os
import json

ACTIVATION_CODE_FILENAME = 'codes.json'


def get_activation_codes():
    """reads code file to"""
    if not os.path.exists(ACTIVATION_CODE_FILENAME):
        # first creation
        with open(ACTIVATION_CODE_FILENAME, 'w'):
            return {}
    with open(ACTIVATION_CODE_FILENAME) as f:
        data = json.load(f)
    return data


def delete_activation_code_file():
    """called from tests"""
    if os.path.exists(ACTIVATION_CODE_FILENAME):
        os.remove(ACTIVATION_CODE_FILENAME)
