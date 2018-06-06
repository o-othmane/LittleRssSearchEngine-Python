#!/usr/bin/env python3 #For Unix
""" #!C:\Python34\python.exe #For Windows"""

"""
@author: Othmane Ouenzar, Soufiane Benhaddou
"""
import cgi, cgitb
import functions, rss
from gensim.models import Word2Vec

print("Content-type: text/html; charset=UTF-8")

cgitb.enable()
form = cgi.FieldStorage()

if 'lang' in form:
    lang = form["lang"].value
else:
    lang = 'en'
    
if lang == 'en':
    title = 'Little RSS Search Engine - En'
    placeholder = 'What are you looking for ?'
    button = 'Search'
    noresult = 'No results for your search'
    en = '<a class = "selected" href="?lang=en">English</a>'
    fr = '<a class = "" href="?lang=fr">French</a>'
else:
    title = 'Little RSS Search Engine - Fr'
    placeholder = 'Que cherchez-vous ?'
    button = 'Chercher'
    noresult = 'Aucun résultat pour votre recherche'
    fr = '<a class = "selected" href="?lang=fr">Français</a>'
    en = '<a class = "" href="?lang=en">Anglais</a>'
    
if('word' in form):
    word = form["word"].value
    if lang == 'en':
        en = '<a class = "selected" href="?word=' + word + '&lang=en">English</a>'
        fr = '<a class = "" href="?word=' + word + '&lang=fr">French</a>'
    else:
        fr = '<a class = "selected" href="?word=' + word + '&lang=fr">Français</a>'
        en = '<a class = "" href="?word=' + word + '&lang=en">Anglais</a>'
    
    model = Word2Vec.load('./rss_models/model_' + lang)
    similatities = functions.getBestSimilarities(model, word, lang, 5)
    results = functions.search(word, lang)
    print('''
          <!DOCTYPE html>
          <html lang="''' + lang + '''">
          <head>
              <title>''' + title + " - " + word + '''</title>
              <link rel="stylesheet" href="../web/styles.css">
          </head>
          <body>
          <div class="logo">
              <img src="../web/images/logo.png" style="border: 0pt none ; width: 300px; height: 300px;">
          </div>
          <form class="searchfield cf">
              <input type="text" name="word" value="''' + word + '''">
              <input type="hidden" name="lang" value="''' + lang + '''">
              <button type="submit">''' + button + '''</button>
          </form> 
          <div class="lang">
              ''' + en + ''' | ''' + fr + '''
          </div>
          <div class="labels">
          ''')
    if similatities:
        for s in similatities:
            print('<a href="?word=' + word + '+' + s + '&lang=' + lang + '"><div class="label">' + s + '</div></a>')
    print('</div>')
        
    if not results:
        print('<div class="result"><p>' + noresult + '</p>')
    else:
        for r in results:
            print('''<a href="''' + r['_source']['url'] + '''">
                <div class="result">
                <p>''' + r['_source']['title'] + '''
                <br><span>''' + r['_source']['desc'] + '''</span></p>
                </div></a>''')
            print('''
                  </body>
                  </html>
                  ''')
        
else:
    rss.fetchRSS(lang, False)
    functions.loadModel(lang)
    print('''
          <!DOCTYPE html>
          <html lang="''' + lang + '''">
          <head>
              <title>''' + title + '''</title>
              <link rel="stylesheet" href="../web/styles.css">
          </head>
          <body>
          <div class="logo">
              <img src="../web/images/logo.png" style="border: 0pt none ; width: 300px; height: 300px;">
          </div>
          <form class="searchfield cf">
              <input type="text" name="word" placeholder="''' + placeholder + '''">
              <input type="hidden" name="lang" value="''' + lang + '''">
              <button type="submit">''' + button + '''</button>
          </form> 
          <div class="lang">
              ''' + en + ''' | ''' + fr + '''
          </div>
          </body>
          </html>
    ''')