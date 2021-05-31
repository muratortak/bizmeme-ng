import json
import requests
import time

def display(thread):
    
    if "sub" in thread:
        print(thread['sub'])
        print("")
    if "com" in thread:
        comment = thread['com']
        comment = comment.replace("<br>", "\n")
        comment = comment.replace("&quot;", "\"")
        comment = comment.replace("&gt;", ">")
        comment = comment.replace("&lt;", "<")
        comment = comment.replace("<wbr>", "")
        comment = comment.replace("<span class=\"quote\">","")
        comment = comment.replace("</span>","")
        comment = comment.replace("&#039;","\'")
        
        print(comment)
    print("-"*80)

def monitor():

    biz = "biz"
    seen = []
    threads = []

    while True:
        boardCatalog = json.loads(requests.get(f"https://a.4cdn.org/{biz}/catalog.json").text)
        time.sleep(1)

        for v in boardCatalog:
            for i in v['threads']:
                threads.append(i)

        threads.sort(key=lambda x: x['no'])
        threads.reverse()

        if not(threads[0]['no'] in seen):
            seen.append(threads[0]['no'])
            display(threads[0])


monitor()