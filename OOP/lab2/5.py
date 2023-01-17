def only_english(string: str):
    return ''.join([s for s in string if 122 >= ord(s) >= 97 or 90 >= ord(s) >= 65])