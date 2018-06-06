#!/usr/bin/env python3 #For Unix
""" #!C:\Python34\python.exe #For Windows"""

"""
@author: Othmane Ouenzar, Soufiane Benhaddou
"""
import cgi, cgitb
import functions, rss
from gensim.models import Word2Vec

cgitb.enable()
form = cgi.FieldStorage()

print("Content-type:application/json; charset=UTF-8")
print("Access-Control-Allow-Origin: *\r\n\r\n")

if 'lang' in form:
    lang = form["lang"].value
else:
    lang = 'en'
    
rss.fetchRSS(lang, False)
functions.loadModel(lang)

if('word' in form):
    word = form["word"].value

    model = Word2Vec.load('./rss_models/model_' + lang)
    similatities = functions.getBestSimilarities(model, word, lang, 5)
    results = functions.search(word, lang)
    
    if not similatities:
        print('{{"similatities":[]},')
    else:
        print('{{"similatities":[')
        i = 0
        for s in similatities:
            print('"' + s + '"')
            if i != len(s)-1:
                print(',')
            i += 1
        print(']},')
        
    if not results:
        print('{"results":[]}}')
    else:
        print('{"results":[')
        i = 0
        for r in results:
            print('\n{"title":"' + r['_source']['title'] + '",\n"url":"' + r['_source']['url'] + '",\n"description":' + r['_source']['desc'] + '}')
            if i != len(s)-1:
                print(',')
            i += 1
        print(']}}')