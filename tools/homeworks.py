from tools.time_converter import time_to_milliseconds, milliseconds_to_time

def number_4(connection):
    # название и год выхода альбомов, вышедших в 2018 году;
    sql = "SELECT title, year FROM albums WHERE year=2018"
    result = connection.execute(sql).fetchall()
    print('Альбомы вышедшие в 2018 году:')
    for row in result:
        print(f"[{row[1]}] {row[0]}")

    # название и продолжительность самого длительного трека;
    # Вариант 1
    sql = "SELECT title, duration FROM tracks ORDER BY duration DESC"
    result = connection.execute(sql).fetchone()
    print('\nСамый продолжительный трэк [вариант 1]:')
    print(f"{result[0]}: {milliseconds_to_time(result[1])}")
    # Вариант 2
    slq = "SELECT title, duration FROM tracks WHERE duration=(SELECT MAX(duration) FROM tracks)"
    result = connection.execute(sql).fetchone()
    print('\nСамый продолжительный трэк [вариант 2]:')
    print(f"{result[0]}: {milliseconds_to_time(result[1])}")

    # название треков, продолжительность которых не менее 3,5 минуты;
    track_duration = time_to_milliseconds(minutes=3, seconds=30)
    sql = f"SELECT title, duration FROM tracks WHERE duration >= {track_duration} ORDER BY title"
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
    result = connection.execute(sql).fetchall()
    print('\nНазвание треков, которые содержат слово "мой"/"my":')
    for row in result:
        print(f"[{milliseconds_to_time(row[1])}] {row[0]}")

def number_5(connection):
    # количество исполнителей в каждом жанре (сортировка по количеству);
    sql = "SELECT * FROM " \
          "(SELECT genres.title, COUNT(performers.name) " \
          "FROM PerformerGenre " \
          "INNER JOIN Performers ON Performers.id = PerformerGenre.performer_id " \
          "INNER JOIN Genres ON Genres.id = PerformerGenre.genre_id " \
          "GROUP BY genres.title) AS result " \
          "ORDER BY count DESC, title"

    result = connection.execute(sql)
    print('\nКоличество исполнителей в каждом жанре:')
    for row in result:
        print(f"{row[0]:.<20}{row[1]}")

    # количество треков, вошедших в альбомы 2019-2020 годов;
    # вариант 1
    sql = "SELECT COUNT(tracks.title) " \
          "FROM tracks " \
          "WHERE album_id IN (SELECT id FROM albums WHERE year BETWEEN 2019 AND 2020)"

    result = connection.execute(sql).fetchone()
    print('\nКоличество треков, вошедших в альбомы 2019-2020 годов [вариант 1]:')
    print(f"{result[0]}")

    # вариант 2
    sql = "SELECT COUNT(tracks.title) " \
          "FROM albums " \
          "JOIN tracks ON tracks.album_id = albums.id " \
          "WHERE albums.year BETWEEN 2019 and 2020;"

    result = connection.execute(sql).fetchone()
    print('\nКоличество треков, вошедших в альбомы 2019-2020 годов [вариант 2]:')
    print(f"{result[0]}")

    # количество треков, вошедших в каждый альбом выпущенный 2019-2020 годов;
    # в задании не было, но было интересно реализовать
    sql = "SELECT * FROM " \
          "(SELECT COUNT(tracks.title),  albums.year, albums.title " \
          "FROM tracks " \
          "JOIN albums ON tracks.album_id = albums.id " \
          "WHERE albums.year BETWEEN 2019 AND 2020 " \
          "GROUP BY albums.title, albums.year) AS result " \
          "ORDER BY count"

    result = connection.execute(sql).fetchall()
    print('\nКоличество треков, вошедших в каждый альбом выпущенный в 2019-2020 годах:')
    for row in result:
        print(f"[{row[1]}] {row[2]:.<35}{row[0]}")

    # средняя продолжительность треков по каждому альбому;
    # вариант 1
    sql = "SELECT * FROM (SELECT AVG(tracks.duration),  albums.year, albums.title " \
          "FROM tracks " \
          "JOIN albums ON tracks.album_id = albums.id " \
          "GROUP BY albums.title, albums.year) AS result " \
          "ORDER BY title"

    result = connection.execute(sql).fetchmany(10)
    print('\nСредняя продолжительность треков по каждому альбому [вариант 1]:')
    for row in result:
        print(f"[{milliseconds_to_time(row[0])}] [{row[1]}] {row[2]}")

    # вариант 2
    sql = "SELECT AVG(tracks.duration), albums.year, albums.title " \
          "FROM albums " \
          "JOIN tracks ON tracks.album_id = albums.id " \
          "GROUP BY albums.title, albums.year " \
          "ORDER BY albums.title"
    result = connection.execute(sql).fetchmany(10)
    print('\nСредняя продолжительность треков по каждому альбому [вариант 2]:')
    for row in result:
        print(f"[{milliseconds_to_time(row[0])}] [{row[1]}] {row[2]}")

    # все исполнители, которые не выпустили альбомы в 2020 году;
    sql = "SELECT name " \
          "FROM Performers " \
          "WHERE name NOT IN " \
          "(SELECT DISTINCT Performers.name " \
          "FROM PerformerAlbum " \
          "JOIN Performers ON Performers.id = PerformerAlbum.performer_id " \
          "JOIN Albums ON Albums.id = PerformerAlbum.album_id " \
          "WHERE albums.year = 2020)"

    result = connection.execute(sql).fetchall()
    print('\nВсе исполнители, которые не выпустили альбомы в 2020 году:')
    for row in result:
        print(row[0])

    # названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
    performer_name = 'The XX'

    sql = f"SELECT DISTINCT collections.title " \
          f"FROM collections " \
          f"JOIN trackcollection ON collections.id = trackcollection.collection_id " \
          f"JOIN tracks ON tracks.id = trackcollection.track_id " \
          f"JOIN albums ON albums.id = tracks.album_id " \
          f"JOIN performeralbum ON performeralbum.album_id = albums.id " \
          f"JOIN performers ON performers.id = performeralbum.performer_id " \
          f"WHERE performers.name LIKE '%%{performer_name}%%' " \
          f"ORDER BY collections.title"

    result = connection.execute(sql).fetchall()
    # так как сборники генерируются на лету,
    # то возможен вариант что нужных сборников не будет
    if len(result) > 0:
        print(f'\nНазвания сборников, в которых присутствует {performer_name}')
        for row in result:
            print(row[0])
    else:
        print(f"\nНет сборников, в которых присутствует {performer_name}")

    # название альбомов, в которых присутствуют исполнители более 1 жанра;
    # выведутся все альбомы, так как в моем случае все артисты выступают более чем в одном жанре
    sql = "SELECT albums.title " \
          "FROM albums " \
          "JOIN PerformerAlbum on albums.id = PerformerAlbum.album_id " \
          "JOIN Performers on Performers.id = PerformerAlbum.performer_id " \
          "JOIN PerformerGenre on Performers.id = PerformerGenre.performer_id " \
          "JOIN Genres on Genres.id = PerformerGenre.genre_id " \
          "GROUP BY albums.title " \
          "HAVING COUNT(DISTINCT Genres.title) > 1 " \
          "ORDER BY albums.title"

    result = connection.execute(sql).fetchmany(10)
    print('\nНазвание альбомов, в которых присутствуют исполнители более 1 жанра:')
    for row in result:
        print(row[0])

    # наименование треков, которые не входят в сборники;
    sql = "SELECT tracks.title " \
          "FROM tracks " \
          "LEFT JOIN TrackCollection on tracks.id = TrackCollection.track_id " \
          "WHERE TrackCollection.track_id is NULL;"

    result = connection.execute(sql).fetchmany(10)
    print('\nНаименование треков, которые не входят в сборники:')
    for row in result:
        print(row[0])

    # исполнителя(-ей), написавшего самый короткий по продолжительности трек
    # (теоретически таких треков может быть несколько);
    # так как в БД есть трэки с нулевой длительностью, добавил условие SELECT * FROM tracks WHERE duration <> 0
    sql = "SELECT performers.name, tracks.title, tracks.duration " \
          "FROM tracks " \
          "LEFT JOIN albums on albums.id = tracks.album_id " \
          "LEFT JOIN PerformerAlbum on PerformerAlbum.album_id = albums.id " \
          "LEFT JOIN performers on performers.id = PerformerAlbum.performer_id " \
          "GROUP BY performers.name, tracks.title, tracks.duration " \
          "HAVING tracks.duration = (SELECT MIN(duration) FROM (SELECT * FROM tracks WHERE duration <> 0) temp) " \
          "ORDER BY performers.name"

    result = connection.execute(sql).fetchall()
    print('\nИсполнители, написавшие самый короткий по продолжительности трек:')
    for row in result:
        print(f"{row[0]}::{row[1]}::{milliseconds_to_time(row[2])}")

    # название альбомов, содержащих наименьшее количество треков.
    sql = "SELECT DISTINCT albums.title " \
          "FROM albums " \
          "JOIN tracks ON tracks.album_id = albums.id " \
          "WHERE tracks.album_id in ( " \
          "SELECT album_id " \
          "FROM tracks " \
          "GROUP BY album_id " \
          "HAVING COUNT(id) = ( " \
          "SELECT COUNT(id) " \
          "FROM tracks " \
          "GROUP BY album_id " \
          "ORDER BY count " \
          "limit 1 )) " \
          "ORDER BY albums.title"

    result = connection.execute(sql).fetchall()
    print('\nНазвание альбомов, содержащих наименьшее количество треков:')
    for row in result:
        print(row[0])






