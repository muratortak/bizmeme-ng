from re import search, findall
from utils.chandata import ChanBoards
from utils.operations import getThreadIdsFromCatalog, getThread, getCommentsFromThreadAsList, removeHTMLFromComment

board = "biz"

threadsIdList = getThreadIdsFromCatalog(board)
if not threadsIdList:
    exit()

commentList = []
for counter, threadId in enumerate(threadsIdList):

    thread = getThread(board, threadId)
    if thread:
        for c in getCommentsFromThreadAsList(thread):
            comment = removeHTMLFromComment(c)
            t = findall(r'(https?://\S+)', comment)
            if len(t) > 0:
                for link in t:
                    print(link)
    else:
        pass