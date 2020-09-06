import json

from fu import *


def rjd(fn):
    """
    rjd :   Read JSON as Dictionary
    """
    with open(fn) as fp:
        return json.load(fp)


def rjs(fn):
    """
    rjs :   Read JSON as String
    """
    with open(fn) as fp:
        return json.loads(fp.read())


if __name__ == "__main__":
    print(rjd("C:\\utils\\fu\\rough.json"))
    print(rjs("C:\\utils\\fu\\rough.json"))
