import sys


class Node(object):

    def __init__(self, name):
        self.name = name
        self.minDistance = sys.maxsize
