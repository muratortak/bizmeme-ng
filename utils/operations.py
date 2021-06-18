from requests import get
from time import sleep
from json import loads
from datetime import datetime

def getThreadIdsFromCatalog(board):

    sleep(1)
    ret = []
    try:
        boardCatalogData = loads(
            get(f"https://a.4cdn.org/{board}/catalog.json").text)
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
        if "com" in post and "time" in post:
            ret.append(post)

    return ret

def removeHTMLFromComment(c):
    comment = c
    comment = comment.replace("<br>", "\n")
    comment = comment.replace("&quot;", "\"")
    comment = comment.replace("&gt;", ">")
    comment = comment.replace("&lt;", "<")
    comment = comment.replace("<wbr>", "")
    comment = comment.replace("<span class=\"quote\">","")
    comment = comment.replace("</span>","")
    comment = comment.replace("&#039;","\'")
    comment = comment.replace("&amp;","&")
    comment = comment.replace("</a>","")
    comment = comment.replace("<a>","")
    comment = comment.replace("\""," ")
    comment = comment.replace(">"," ")
    return comment

def calculateThreadPostRate(board, threadID):
    ''' 
    Take a single thread and calculate the rate posts are made to it
    Return a list of times which are the delays between posts
    '''
    dates = []
    threadPosts = getThread(board, threadID)["posts"]
    for post in threadPosts:
        dates.append(datetime.utcfromtimestamp(post['time']))
    return dates

def getCountryFlagsAndCommentsFromThread(board, threadID):
    
    countryAndComments = []
    threadPosts = getThread(board, threadID)["posts"]
    
    for post in threadPosts:
        if "country" in post and "com" in post:
            countryAndComments.append( (post['country'],post['com']))

    countryAndComments.sort()    
    
    return countryAndComments

def meanPostLengthByCountry(countryAndThreadList):
    postLengths = {}

    for data in countryAndThreadList:
        country = data[0]
        comment = data[1]

        if not (country in postLengths.keys()):
            postLengths[country] = (len(comment),1)
        
        else:
            currentTotalCharacters = postLengths[country][0]
            numberOfPosters = postLengths[country][1]
            postLengths[country] = (currentTotalCharacters+len(comment), numberOfPosters+1)

    ret = []
    for data in postLengths:
        ret.append( (data, int(postLengths[data][0]/postLengths[data][1]) ) )  

    ret.sort(key=lambda x: x[1],reverse=True)
    return ret

