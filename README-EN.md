# Little RSS Search Engine

Un moteur de recherche qui analyse les flux RSS à partir de la liste des URL  .TXT, indexe le contenu des pages en utilisant Elasticsearch et utilise word2vec pour la classification des résultats.

## Getting Started

### Prerequisites

Python >= 3.0 with modules nltk, feedparser and elasticsearch:

```
pip install nltk feedparser elasticsearch
```

### Setup
Clone the repo

```
git clone https://github.com/o-othmane/LittleRssSearchEngine-Python
```

Move into the directory

```
cd LittleRssSearchEngine-Python
```

First run the script with --fetch argument to fetch RSS feeds and create index in ElasticSearch.

```
python main.py -f -l fr test
```

## Usage



Sggest using -h to get help on the most current version.

```
usage: main.py [-h] [-f] [-l LANG] [-p PROPOSITIONS] [-d] word

positional arguments:
word            word to search

optional arguments:
-h,             --help                   show this help message and exit
-f,             --fetch                  fetch rss feeds
-l LANG,        --lang LANG              specify language (en | fr) (default:en)
-np NBRPROPOS,  --nbrpropos NBRPROPOS    number of propositions (default:5)
-d,             --debug                  debug
```

## Example use
```
python main.py -l fr -p 3 trump

========================== Little RSS Search Engine ==========================

================================ Propositions ================================
donald
accord
nucleaire

=============================== Search results ===============================
Title :  Trump dans l'oeil du cyclone Stormy Daniels
Url :  http://www.lepoint.fr/24h-infos/rss.xml

Title :  Sur les biocarburants, Trump tiraillé entre agriculteurs et raffineurs
Url :  http://www.lepoint.fr/24h-infos/rss.xml

Title :  Singapour devrait accueillir mi-juin le sommet Kim-Trump
Url :  http://www.lepoint.fr/24h-infos/rss.xml

Title :  Nucléaire iranien: Rohani met en garde Trump avant sa décision
Url :  http://www.lepoint.fr/24h-infos/rss.xml

Title :  Nucléaire iranien: Rohani met en garde Trump avant sa décision
Url :  http://www.lepoint.fr/24h-infos/rss.xml

Title :  Nobel: le mystère de la nomination falsifiée de Trump restera entier
Url :  http://www.lepoint.fr/24h-infos/rss.xml
```

## Web interfaces

Launch server

```
python httpServer
```

You can then access search engine on 

```
http://localhost:8000/src/search.py
```

You can get rest by calling

```
http://localhost:8000/src/rest.py
```

## Authors

**[Othmane Ouenzar](https://github.com/o-othmane)**

**[Soufiane Benhaddou](https://github.com/soufianemarly)**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

