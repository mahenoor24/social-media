import sqlite3 as sql
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

def create_posts(name,content):
    con=sql.connect(os.path.join(ROOT,'database.db'))
    cur=con.cursor()
    cur.execute('insert into posts(name,content) values(?,?)',(name,content))
    con.commit()
    con.close()
def get_posts():
    con=sql.connect(os.path.join(ROOT,'database.db'))
    cur=con.cursor()
    cur.execute('select * from posts')
    posts=cur.fetchall()
    return posts
def update_post(post_id, name, content):
    con = sql.connect(os.path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('UPDATE posts SET name = ?, content = ? WHERE id = ?', (name, content, post_id))
    con.commit()
    con.close()

def delete_post(post_id):
    con = sql.connect(os.path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('DELETE FROM posts WHERE id = ?', (post_id,))
    con.commit()
    con.close()