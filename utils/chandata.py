from requests import get
from json import loads
from time import sleep

class ChanBoards:
    def __init__(self):
        self.data = loads(get("https://a.4cdn.org/boards.json").text)
        self.boardNames = [name['board'] for name in self.data["boards"]]
