import requests
from bs4 import BeautifulSoup
import sqlite3


class DB:
    path = ''

    _db_connection = None
    _db_cur = None

    def __init__(self, path):
        self.path = path
        self._db_connection = sqlite3.connect(self.path)
        self._db_cur = self._db_connection.cursor()

    def query(self, query):
        return self._db_cur.execute(query)

    def fetch(self, query):
        return self._db_cur.execute(query).fetchall()

    def save(self):
        self._db_connection.commit()

    def __del__(self):
        self._db_connection.close()


class Actor:
    href = ""
    name = ""
    film = ""

    def __init__(self, href, name, film):
        self.href = href
        self.name = name
        self.film = film


url = "https://www.kinopoisk.ru/film/522/"

act = []
html = requests.get(url).text
soup = BeautifulSoup(html, "html5lib")

filmname = soup.find("h1", {'class': 'moviename-big'}).text
actors = soup.findAll("li", {'itemprop': "actors"})
for actor in actors:
    # print(actor)
    href = actor.find("a")
    if href is not None:
        act.append(Actor(href.get("href"), actor.text, filmname))

del act[-1]

# -----------------------------------------------------

db = DB("C:\\Users\\atyunyatkin\\Downloads\\db_tab1 (1).sqlite")

for a in act:
    db.query("INSERT INTO Actor VALUES (0, '%s', '%s', '%s');") % (a.href, a.name, a.film)
    db.save()

print(db.fetch("SELECT * FROM Actors"))