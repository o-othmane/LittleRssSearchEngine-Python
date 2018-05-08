"""
Created on Thu May  3 22:28:33 2018

@author: Othmane Ouenzar, Soufiane Benhaddou
"""
import feedparser, hashlib
from elasticsearch import Elasticsearch

# Getting RSS urls from file
def getUrls(lang, debug):
    if lang == 'en':
        file = open("lists/list_en.url.txt","r")
    else:
        file = open("lists/list_fr.url.txt","r")
    
    urls = []
    for line in file:
        urls.append(line)
    file.close()
    if debug:
        print("\n==========\nFetched urls :\n")
        print(urls)
        print("\n==========\n")
    return urls

# Fetching RSS feeds
def fetchRSS(lang, debug):
    urls = getUrls(lang, debug)
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    for url in urls:
        d = feedparser.parse(url, handlers = [])
        count = 1
        if debug: print("\n==========\nFetched posts for '" + url + ":\n")
        for post in d.entries:
            l = post.title + '\n' + post.description + '\n'
            h = hashlib.sha224(l.encode('utf-8')).hexdigest()
            if not es.exists(index='rss_' + lang, doc_type='item-rss', id=h):
                if debug: print("Title : " + post.title + "\n")
                es.index(index='rss_' + lang, doc_type='item-rss', id=count, body={'title':post.title, 'desc':post.description, 'url':url})
                count += 1
        if debug: print("\n==========\n")