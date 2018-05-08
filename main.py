"""
Created on Thu May  3 22:28:33 2018

@author: Othmane Ouenzar, Soufiane Benhaddou
"""

import rss, argparse, re
from nltk.corpus import stopwords
from elasticsearch import Elasticsearch, helpers
from gensim.models import Word2Vec

# Creating model from Elasticsearch index
def loadModel(ids):
    for i in ids:
        postId = i['_id']
        post = es.get(index = 'rss_' + args.lang, doc_type = 'item-rss', id = postId)
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
    model.save('./rss_models/model_' + args.lang)

# Geting best similarities from W2V model
def getBestSimilarities(model, word, stop, topn=100):
    bs = model.wv
    if word in bs.vocab:
        bs = bs.most_similar(positive = [word], topn = topn)
        for s in bs:
            if (s[0] not in stop) and len(s[0])>2:
                    print(s[0])
    else: print("No proposition for your search")

# Searching for word on Elasticsearch
def search(word):
  result = es.search(index='rss_' + args.lang, doc_type='item-rss', body={"query": {"match": {"title": word.strip()}}})
  if result['hits']['total'] != 0:
      for item in result['hits']['hits']:
        print("Title : ", item['_source']['title'])
        print("Url : ", item['_source']['url'])
  else: print("No result for your search")

# Creating title banner
def banner(text, ch='=', length=78):
    spaced_text = ' %s ' % text
    banner = spaced_text.center(length, ch)
    return banner

if __name__ == "__main__":
    # Displaying banner
    print(banner('Little RSS Search Engine') + "\n")
    
    # Setting arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('word', help='word to search')    
    parser.add_argument('-f', '--fetch', help='fetch rss feeds', action='store_true')
    parser.add_argument('-l', '--lang', default='en',  help='specify language (en | fr) (default:en)')
    parser.add_argument('-np', '--nbrpropos', type=int, default=5, help='number of propositions (default:5)')
    parser.add_argument('-d', '--debug', help='debug', action='store_true')
    args = parser.parse_args()
    
    es = Elasticsearch()

    # If fetch mode, fetch rss feeds and create model
    if args.fetch:
        rss.fetchRSS(args.lang, args.debug)
        sentences=[]
        ids = helpers.scan(es, query={"query":{"match_all": {}}},scroll = '1m', index = 'rss_' + args.lang)
        loadModel(ids)
        
    # Getting W2V model
    model = Word2Vec.load('./rss_models/model_' + args.lang)
    
    # Setting stop words
    if args.lang == 'en':
        stop = set(stopwords.words('english'))
    else:
        stop = set(stopwords.words('french'))
     
# If debug mode, displaying vocabulary dict
if args.debug:
    vocabulary=model.wv.vocab
    print(vocabulary.keys())

# Displaying banner
print("\n")
print(banner('Propositions'))
# Displaying propositions
similatities = getBestSimilarities(model, args.word, stop, args.propositions)
   
# Displaying banner
print("\n")
print(banner('Search results'))
# Displaying search results
search(args.word)