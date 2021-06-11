
# Display new threads as they're created

import json
import requests
import time
from utils.operations import removeHTMLFromComment

def display(thread):

    if "sub" in thread:
        print(thread['sub'])
        print("")
    if "com" in thread:
        comment = removeHTMLFromComment(thread['com'])
        print(comment)
    print("-"*80)


def monitor():

    biz = "biz"
    seen = []
    threads = []

    while True:
        boardCatalogDataText = requests.get(
            f"https://a.4cdn.org/{biz}/catalog.json").text
        boardCatalogJson = json.loads(boardCatalogDataText)
        time.sleep(1)

        for boardPageJson in boardCatalogJson:
            for boardThreadLink in boardPageJson['threads']:
                threads.append(boardThreadLink)

        threads.sort(key=lambda x: x['no'], reverse=True)

        if not(threads[0]['no'] in seen):
            seen.append(threads[0]['no'])
            display(threads[0])


monitor()

