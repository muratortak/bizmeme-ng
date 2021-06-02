from requests import get
from time import sleep
from json import loads
# go through every thread

# download everything

def getThreadIdsFromCatalog(board):

    sleep(1)
    ret = []
    try:
        boardCatalogData = loads(get(f"https://a.4cdn.org/{board}/catalog.json").text)
    except:
        return None
    
    for boardCatalogPageData in boardCatalogData:
        for thread in boardCatalogPageData['threads']:
            ret.append(thread['no'])

    return ret

def getThread(board, threadId):

    try:
        sleep(1)
        return loads(get(f"https://a.4cdn.org/{board}/thread/{threadId}.json").text)
    except:
        return None

def getCommentsFromThreadAsList(thread):
    
    ret = []
    data = thread["posts"]  

    for post in data:
        if "com" in post:
            ret.append(post["com"])    
    
    return ret