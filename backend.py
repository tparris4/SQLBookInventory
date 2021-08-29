import sqlite3


class Database:

    # constructor object
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        # self becomes an attribute of the class, not an object
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year INTEGER, isbn integer)")
        self.conn.commit()
      #  conn.close()

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)",
                         (title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * from book")
        rows = self.cur.fetchall()
        # self.conn.close()
        return rows

    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * from book WHERE title=? OR author=? OR year=? OR isbn=?",
                         (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=? ", (id,))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=? ",
                         (title, author, year, isbn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


#insert("The sea", "John Tablet", 1918, 913123132)
# print(view())
#print(search(author="John Tablet"))
# delete(1)
#update(1, "The earth", "John Smooth", 1917, 999999)
