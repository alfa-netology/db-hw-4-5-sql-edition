import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
from datetime import timedelta
import random
import json

from data import source


def milliseconds_to_time(duration):
    # преобразование в часы, минуты и секунды
    seconds = int((duration/1000) % 60)
    minutes = int((duration / (1000 * 60)) % 60)
    hours = int((duration / (1000 * 60 * 60)) % 24)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def time_to_milliseconds(hours=0, minutes=0, seconds=0):
    # преобразование в милисекунды
    delta = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    return int(delta.total_seconds()) * 1000


# подключение к бд
with open('data/connection_settings') as file:
    connection_settings = file.readline()

dbase = connection_settings
engine = sqlalchemy.create_engine(dbase)
connection = engine.connect()

queries = source.queries

# удалем таблицы если он существуют
connection.execute(queries.get('drop_tables'))
# создем таблицы
connection.execute(queries.get('create_tables'))
# исходные данные об исполнителях
with open('data/performers_data.json', encoding='utf-8') as file:
    performers_data = json.load(file)

album_id = 0
track_id = 0
genres_id = 0
genres = {}

for performer_id, (performer_name, performer_data) in enumerate(performers_data.items()):
    # наполняем отношение Performers
    sql = f"INSERT INTO Performers VALUES ({performer_id}, '{performer_name}')"
    connection.execute(sql)

    # наполняем отношения Genres & PerformerGenre
    for genre in performer_data.get('genres'):
        if genre not in genres:
            sql = f"INSERT INTO Genres VALUES ({genres_id}, '{genre}')"
            connection.execute(sql)
            genres[genre] = genres_id
            genres_id += 1

        sql = f"SELECT id FROM genres WHERE title='{genre}'"
        genre_id = connection.execute(sql).fetchone()[0]

        sql = f"INSERT INTO PerformerGenre VALUES ({performer_id}, {genre_id})"
        connection.execute(sql)

    # наполняем отношения Albums & PerformerAlbum
    for album in performer_data.get('albums'):
        album_title = album.get('title').replace("'", "''")
        album_year = album.get('year')
        if album_year != '0':
            sql = f"INSERT INTO albums VALUES ({album_id}, '{album_title}', {album_year})"
            connection.execute(sql)

            sql = f"INSERT INTO PerformerAlbum VALUES ({performer_id}, {album_id})"
            connection.execute(sql)

            # наполняем отношение Tracks
            for track in album.get('tracks'):
                track_title = track.get('title').replace("'", "''")
                track_duration = int(track.get('duration'))
                sql = f"INSERT INTO tracks VALUES ({track_id}, '{track_title}', {track_duration}, {album_id})"
                connection.execute(sql)
                track_id += 1
            album_id += 1

# максимальный track_id (для генерации колекций)
sql = f"SELECT * FROM tracks ORDER BY id DESC"
track_max_id = connection.execute(sql).fetchone()[0]

# наполняем отношение Collections & TrackCollection
for collection_id in range(11):
    collection_year = random.randrange(2015, 2022, 1)
    collection_title = f"Collection #{collection_id}"
    sql = f"INSERT INTO collections VALUES ({collection_id}, '{collection_title}', {collection_year})"
    connection.execute(sql)

    for i in range(random.randrange(10, 15, 1)):
        track_id = random.sample(range(0, track_max_id), 1)[0]
        sql = f"INSERT INTO TrackCollection VALUES ({track_id}, {collection_id})"
        try:
            connection.execute(sql)
        except SQLAlchemyError as e:
            pass

# название и год выхода альбомов, вышедших в 2018 году;
sql = "SELECT title, year FROM albums WHERE year=2018"
result = connection.execute(sql).fetchall()
print('Альбомы вышедшие в 2018 году:')
for row in result:
    print(f"{row[0]:.<45}{row[1]}")

# название и продолжительность самого длительного трека;
sql = "SELECT title, duration FROM tracks ORDER BY duration DESC"
result = connection.execute(sql).fetchone()
print('\nСамый продолжительный трэк:')
print(f"{result[0]}: {milliseconds_to_time(result[1])}")

# название треков, продолжительность которых не менее 3,5 минуты;
track_duration = time_to_milliseconds(minutes=3, seconds=30)
sql = f"SELECT title, duration FROM tracks WHERE duration >= {track_duration} ORDER BY title"
result = connection.execute(sql).fetchall()
print('\nТрэки продолжительностью не менее 3,5 минут:')
for row in result:
    print(f"[{milliseconds_to_time(row[1])}] {row[0]}")

# названия сборников, вышедших в период с 2018 по 2020 год включительно;
sql = "SELECT title, year FROM collections WHERE year BETWEEN 2018 and 2020"
result = connection.execute(sql).fetchall()
print('\nСборники вышедшие с 2018 по 2020 годы:')
for row in result:
    print(row[1], row[0])

# исполнители, чье имя состоит из 1 слова;
sql = "SELECT name FROM performers WHERE name NOT LIKE '%% %%'"
result = connection.execute(sql).fetchall()
print('\nИсполнители чьё имя состоит из одного слова:')
for row in result:
    print(row[0])

# название треков, которые содержат слово "мой"/"my".
sql = "SELECT title, duration FROM tracks WHERE title ~* '( my |мой )' or title ~* '(^my |^мой )';"
result = connection.execute(sql).fetchall()
print('\nНазвание треков, которые содержат слово "мой"/"my":')
for row in result:
    print(f"[{milliseconds_to_time(row[1])}] {row[0]}")
