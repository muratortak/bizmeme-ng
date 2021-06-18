from data import Post
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
    

cur.execute('''

    CREATE TABLE IF NOT EXISTS PostData ( 
        board text,
        no text,
        sticky text,
        closed text,
        now text,
        name text,
        sub text,
        com text,
        filename text,
        ext text,
        w text,
        h text,
        tn_w text,
        tn_h text,
        tim text,
        time text,
        md5 text,
        filesize text,
        resto text,
        capcode text,
        semantic_url text,
        trip text,
        id text,
        country text,
        country_name text,
        board_flag text,
        flag_name text,
        filedelete text,
        spoiler text,
        custom_spoiler text,
        replies text,
        bumplimit text,
        since4pass text,
        unique_ips text,
        archived text,
        archived_on text,
        primary key (board, no)
    )

''')

def addPost(boardName: str, data: Post) -> None:
    try:
        cur.execute(''' 
        INSERT INTO PostData 
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?); ''', 
        (
            boardName, 
            data.no,
            data.sticky,
            data.closed,
            data.now,
            data.name,
            data.sub,
            data.com,
            data.filename,
            data.ext,
            data.w,
            data.h,
            data.tn_w,
            data.tn_h,
            data.tim,
            data.time,
            data.md5,
            data.filesize,
            data.resto,
            data.capcode,
            data.semantic_url,
            data.trip,
            data.id,
            data.country,
            data.country_name,
            data.board_flag,
            data.flag_name,
            data.filedeleted,
            data.spoiler,
            data.custom_spoiler,
            data.replies,
            data.bumplimit,
            data.since4pass,
            data.unique_ips,
            data.archived,
            data.archived_on
        ))
    except:
        print("Error on insert")
    



















