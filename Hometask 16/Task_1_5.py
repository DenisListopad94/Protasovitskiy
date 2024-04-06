# 1. Подключить готовую базу с актёрами и режиссёрами использую SQLite3.
import sqlite3
from queries import one_movie_director

with sqlite3.connect("D:/Python/cinema.db") as con:
    cur = con.cursor()

    res = cur.execute(one_movie_director)
    data = res.fetchall()

print(data)





