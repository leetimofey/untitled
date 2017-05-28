import sqlite3


# Стандартный класс для БД
class UsersDB:
    name = 'pullAndBear.db'  # Надо чтобы имя было такое, она может сама создаться если ее нет

    _db_connection = None
    _db_cur = None

    def __init__(self):
        self._db_connection = sqlite3.connect(self.name)
        self._db_cur = self._db_connection.cursor()

    def query(self, query):  # Обычный запрос, чтобы что-нить вставить в БД
        self._db_cur.execute(query)
        self._db_connection.commit()
        return

    def fetch(self, query):  # Вытащить что-нить из БД
        return self._db_cur.execute(query).fetchall()

    def save(self):
        self._db_connection.commit()

    def __del__(self):
        self._db_connection.close()


def createUsersTable():  # Создать таблицу в БД
    a = UsersDB()
    a.query(
        'CREATE TABLE users(uid INTEGER NOT NULL, first_name TEXT, last_name TEXT, sex INTEGER, bday INTEGER, city INTEGER, country INTEGER, home_town INTEGER, university_ids TEXT, schools_ids TEXT, followers INTEGER, relation INTEGER, groups_ids TEXT, date_creation INTEGER);'
    )


def createLinksTable():  # Создать таблицу с autoincrement/ Названия столбцов через запятую
    a = UsersDB()
    a.query(
        'CREATE TABLE links(id INTEGER NOT NULL PRIMARY KEY autoincrement UNIQUE, destination TEXT, isDeleted INTEGER);'
    )
    return


def addVisit(link_id, vk_id, fromWhere):  # Добавить инфу в таблицу
    a = UsersDB()
    a.query(
        'INSERT INTO visits(vk_id, link_id, fromWhere) values (%d,%d,\'%s\')' % (vk_id, link_id, fromWhere)
    )
    return

# visits - название таблицы/ (vk_id, link_id, fromWhere) - в какие столбцы надо добавить инфу
# values (%d,%d,\'%s\')' % (vk_id, link_id, fromWhere) - какие значения вставить, они пришли в аргумент ф-