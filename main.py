#!/usr/bin/env python3 #For Unix
""" #!C:\Python34\python.exe #For Windows"""

"""
@author: Othmane Ouenzar, Soufiane Benhaddou
"""
import argparse
from src import rss, functions
from gensim.models import Word2Vec

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

    # If fetch mode, fetch rss feeds and create model
    if args.fetch:
        rss.fetchRSS(args.lang, args.debug)
        functions.loadModel(args.lang)
        
    # Getting W2V model
    model = Word2Vec.load('./rss_models/model_' + args.lang)
     
# If debug mode, displaying vocabulary dict
if args.debug:
    vocabulary=model.wv.vocab
    print(vocabulary.keys())

# Displaying banner
print("\n")
print(banner('Related words'))
# Displaying propositions
similatities = functions.getBestSimilarities(model, args.word, args.lang, args.nbrpropos)
if not similatities:
    print("No propositions for your search")
else:
    print(similatities)
 
# Displaying banner
print("\n")
print(banner('Search results'))
# Displaying search results
results = functions.search(args.word, args.lang)
if not results:
    print("No results for your search")
else:
    for result in results:
        print("Title : ", result['_source']['title'])
        print("Url : ", result['_source']['url'])