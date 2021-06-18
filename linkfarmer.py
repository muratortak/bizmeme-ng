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
          'sp',
          'trash',
          'co',
          'mu',
          'tg',
          'fit',
          'r9k',
          'g',
          'x',
          'his',
          'adv',
          'lit',
          'bant',
          'ck',
          'o',
          'qa',
          'aco',
          'mlp',
          'vrpg',
          'soc',
          'm',
          'vr',
          's4s'
]
shuffle(boards)
posts = []
for board in boards:

    threadsIdList = getThreadIdsFromCatalog(board)
    
    if not threadsIdList: exit()
    
    print(f"Beginning {board}, total threads {len(threadsIdList)}")
    
    commentList = []
    for threadId in threadsIdList:
        thread = getThread(board, threadId)
        if thread:     
            print("o",end="",flush=True)
            for comment in getCommentsFromThreadAsList(thread):
                db.addPost(board,Post(comment))
        else:
            pass
            print("x",end="",flush=True)
        db.con.commit()
    print()

db.con.close()
