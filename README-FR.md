<p align="center">
<img src="https://github.com/o-othmane/LittleRssSearchEngine-Python/blob/master/web/images/Header.jpg" width="100%"/>
</p>

# Little RSS Search Engine

Un moteur de recherche qui analyse les flux RSS à partir de la liste des URL  .TXT, indexe le contenu des pages en utilisant Elasticsearch et utilise word2vec pour la classification des résultats.

## Commencer

### Préalables

Python >= 3.0 avec les modules nltk, feedparser et elasticsearch:

```
pip install nltk feedparser elasticsearch
```

### Installer
Cloner le repo

```
git clone https://github.com/o-othmane/LittleRssSearchEngine-Python
```

Déplacer vers le répertoire

```
cd LittleRssSearchEngine-Python
```

Commencez par exécuter le script avec --fetch argument pour récupérer les flux RSS et créer un index dans ElasticSearch.

```
python main.py -f -l fr test
```

## Utilisation

Suggére d'utiliser -h pour obtenir de l'aide sur la version la plus récente.

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

## Example d'utilisation
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

## Interfaces web 

Lancer le serveur

```
python httpServer
```

Vous pouvez ensuite accéder au moteur de recherche sur l'adresse 

```
http://localhost:8000/src/search.py
```

Vous pouvez acceder à REST par 

```
GET http://localhost:8000/src/rest.py?lang=fr&word=trump
```

## Captures d'écran
<p align="center">
<img src="https://github.com/o-othmane/LittleRssSearchEngine-Python/blob/master/web/images/Screenshot1.png" width="40%"/>
<img src="https://github.com/o-othmane/LittleRssSearchEngine-Python/blob/master/web/images/Screenshot2.png" width="40%"/>
<img src="https://github.com/o-othmane/LittleRssSearchEngine-Python/blob/master/web/images/Screenshot3.png" width="40%"/>
<img src="https://github.com/o-othmane/LittleRssSearchEngine-Python/blob/master/web/images/Screenshot4.png" width="40%"/>
</p>

## Auteurs

**[Othmane Ouenzar](https://github.com/o-othmane)**

**[Soufiane Benhaddou](https://github.com/soufianemarly)**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

