import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()

cur.execute('''

    CREATE TABLE IF NOT EXISTS chanlinks ( 
        date text,
        board text,
        link text,
        primary key (date, board, link)
    )

''')


def addRow(link, date, board):
    cur.execute(''' INSERT INTO chanlinks (link, date, board) values(?,?,?); ''', (link, date, board))