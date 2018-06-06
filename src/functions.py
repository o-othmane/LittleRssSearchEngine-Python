#!/usr/bin/env python3 #For Unix
""" #!C:\Python34\python.exe #For Windows"""

"""
@author: Othmane Ouenzar, Soufiane Benhaddou
"""
import re
from nltk.corpus import stopwords
from elasticsearch import Elasticsearch, helpers
from gensim.models import Word2Vec

es = Elasticsearch()

# Creating model from Elasticsearch index
def loadModel(lang):
    ids = helpers.scan(es, query={"query":{"match_all": {}}},scroll = '1m', index = 'rss_' + lang)
    sentences=[]
    for i in ids:
        postId = i['_id']
        post = es.get(index = 'rss_' + lang, doc_type = 'item-rss', id = postId)
        postsrc=post['_source']
        lines = postsrc['title'] + '\n' + postsrc['desc']
        lines = lines.splitlines()	
        for line in lines:
            line = str(line)
            line = re.sub('[\'\\\[\]/{}.,]+', ' ', line)
            if len(line) > 3:
                line = line.lower()
                line = line.split()
                sentences.append(line[2:])    
    model = Word2Vec(sentences, min_count = 2, window=4, iter = 30, sg = 1)
    model.save('./rss_models/model_' + lang)

# Geting best similarities from W2V model
def getBestSimilarities(model, word, lang, topn=100):
    # Setting stop words
    if lang == 'en':
        stop = set(stopwords.words('english'))
    else:
        stop = set(stopwords.words('french'))
       
    similarities=[]
    bs = model.wv
    if word in bs.vocab:
        bs = bs.most_similar(positive = [word], topn = topn)
        for s in bs:
            if (s[0] not in stop) and len(s[0])>2:
                    similarities.append(s[0])
    return similarities

# Searching for word on Elasticsearch
def search(word, lang):
    results=[]
    result = es.search(index='rss_' + lang, doc_type='item-rss', body={"query": {"match": {"title": word.strip()}}})
    if result['hits']['total'] != 0:
        for item in result['hits']['hits']:
            results.append(item)      
    return results