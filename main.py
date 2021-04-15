from data import queries
from tools.time_converter import time_to_milliseconds, milliseconds_to_time
from tools import connection
from tools import insert_data

connection = connection.create()
queries = queries.data

# удалем отношения если он существуют
connection.execute(queries.get('drop_tables'))
# создем отношения
connection.execute(queries.get('create_tables'))
# наполняем отношения данными
insert_data.insert(connection)


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
# result = connection.execute(sql).fetchall()
result = connection.execute(sql).fetchmany(10)
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
# result = connection.execute(sql).fetchall()
result = connection.execute(sql).fetchmany(10)
print('\nНазвание треков, которые содержат слово "мой"/"my":')
for row in result:
    print(f"[{milliseconds_to_time(row[1])}] {row[0]}")
