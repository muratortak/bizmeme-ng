from html import unscape
from re import search, findall
from utils.chandata import ChanBoards
from utils.operations import getThreadIdsFromCatalog, getThread, getCommentsFromThreadAsList

board = "biz"

threadsIdList = getThreadIdsFromCatalog(board)
if threadsIdList == None:
    exit()

commentList = []
for counter, threadId in enumerate(threadsIdList):

    thread = getThread(board, threadId)
    if thread != None:
        for comment in getCommentsFromThreadAsList(thread):
            comment = html.unescape(comment)

            t = findall(r'(https?://\S+)', comment)
            if len(t) > 0:
                for link in t:
                    print(link)
    else:
        pass
