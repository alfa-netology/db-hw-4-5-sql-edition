from tools import connection
from data import queries
from tools import insert_data
from tools import homeworks

connection = connection.create()
queries = queries.data

# удалем отношения если они существуют
connection.execute(queries.get('drop_tables'))
# создем отношения
connection.execute(queries.get('create_tables'))
# наполняем отношения данными
insert_data.insert(connection)
# домашнее задание #4
homeworks.number_4(connection)
# домашнее задание #5
homeworks.number_5(connection)
