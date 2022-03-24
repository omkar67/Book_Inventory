import sqlite3

class Database:

    def __init__(self):
        self.connection_var=sqlite3.connect("books_database.db")
        self.Cursor_var=self.connection_var.cursor()
        self.Cursor_var.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.connection_var.commit()
        

    def view_db(self):
        
        self.Cursor_var.execute("SELECT * FROM book ")
        rows=self.Cursor_var.fetchall()
        return rows

    def search_db(self,title,author,year,isbn):
       
        self.Cursor_var.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? or isbn=? ",(title,author,year,isbn,))
        rows=self.Cursor_var.fetchall()
        self.connection_var.commit()
        return rows


    def add_db(self,title,author,year,isbn):
       
        self.Cursor_var.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
        self.connection_var.commit()

    def update_db(self,title,author,year,isbn,id):
               
        self.Cursor_var.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id,))
        self.connection_var.commit()
        

    def delete_db(self,id):
        self.Cursor_var.execute("DELETE FROM book WHERE id=?",(id,))
        self.connection_var.commit()

    def __del__(self):
        self.connection_var.close()

'''  
add_db("R P N Singh","Politics of Opportunism",1996,456)
add_db("oliver twist",'Charles Dickens',1945,7964)

'''






