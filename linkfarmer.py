import time
from random import shuffle, sample
from re import search, findall
from data import Post
from utils.chandata import ChanBoards
from utils.operations import getThreadIdsFromCatalog, getThread, getCommentsFromThreadAsList, removeHTMLFromComment
import db

boards = ['pol',
          'vg',
          'v',
          'b',
          'biz',
          'int',
          'a',
          'tv',
          'vt',
          'trash',
          'mu',
          'fit',
          'r9k',
          'g',
          'x',
          'his',
          'adv',
          'lit',
          'bant',
          'ck',
          'qa',
          'aco',
          'mlp',
          'vrpg',
          'soc',
          'vr',
          's4s'
]

shuffle(boards)

def scrapeBoard(board: str) -> None:

    threadsIdList = getThreadIdsFromCatalog(board)
    if not threadsIdList: exit()
    
    print(f"Beginning {board}, total threads {len(threadsIdList)}")

    for threadIndex, threadId in enumerate(threadsIdList):
        
        delta = 0
        timePast = time.time()  

        thread = getThread(board, threadId)
        
        if thread:    
            for comment in getCommentsFromThreadAsList(thread):
                db.addPost(board,Post(comment))
        
        delta = time.time() - timePast
        print(board, threadIndex, "/", len(threadsIdList), delta)
        
    db.con.commit()


for board in boards:
    scrapeBoard(board)
db.con.close()


