from random import shuffle, sample
from re import search, findall
from utils.chandata import ChanBoards
from utils.operations import getThreadIdsFromCatalog, getThread, getCommentsFromThreadAsList, removeHTMLFromComment
import db

boards = ChanBoards().boardNames

for board in boards:

    threadsIdList = getThreadIdsFromCatalog(board)
    
    if not threadsIdList: exit()
    
    print(f"Beginning {board}, total threads {len(threadsIdList)}")
    
    commentList = []
    for threadId in threadsIdList:

        thread = getThread(board, threadId)
        
        if thread:
            
            print("o",end="",flush=True)
            
            for c in getCommentsFromThreadAsList(thread):
                
                comment = removeHTMLFromComment(c[0])
                matches = findall(r'(https?://\S+)', comment)
                
                if len(matches) > 0:
                    
                    for link in matches:
                        try:
                            db.addRow(link,c[1],board)
                        except:
                            print("u",end="",flush=True)
        else:
            pass
            print("x",end="",flush=True)
    
        db.con.commit()
    print()

db.con.close()
