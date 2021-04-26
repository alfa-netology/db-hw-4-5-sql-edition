import json
from sqlalchemy.exc import SQLAlchemyError
import random

def insert(connection):
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
            # рандом рандомом, но он бывает повторяется, подстрахуемся
            try:
                connection.execute(sql)
            except SQLAlchemyError as e:
                print(e)
                print("Упс! Что-то пошло не так, но ничего страшного. "
                      "Мы с этим справимся.\n")
