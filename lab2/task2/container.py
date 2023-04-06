import json
import os
import re


class Container:
    _username: str
    _storage: set[str] = set()
    _filename: str

    def __init__(self, username: str):
        self._username = username
        self._filename = f'./data/{username}.json'
        self.load()

def add(self, key):
        self._storage.add(key)