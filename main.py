import time
import requests
import json
import sqlite3


boards = {
    "biz":"https://a.4cdn.org/biz/archive.json",
} 

def chanGet(url): 
    time.sleep(1)
    try:
        t = requests.get(url).text
        t = json.loads(t)
    except:
        return None
    return t

def getArchive(board): 
    return chanGet(board)

def getThreads(board):

    boardArchive = getArchive(f"https://a.4cdn.org/{board}/archive.json")
    threads = []

    for i, thread in enumerate(boardArchive):
        print(f" {i} / {len(boardArchive)} ")
        print(f"https://a.4cdn.org/{board}/thread/{thread}.json")

        try:
            threadData = chanGet(f"https://a.4cdn.org/{board}/thread/{thread}.json")
            
            if len(threadData['posts']) < 10:
                if 'sub' in threadData:
                    print(threadData['sub'])
                print(threadData['com'])
            
            threads.append(threadData)
        except:
            pass
    return threads
    
getThreads("biz")