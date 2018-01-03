"""
A program that stores the book information:
Title, Author
Year, ISBN

User can:
view all records
search an entry
add entry
update entry
delete 
close
https://www.udemy.com/the-python-mega-course/learn/v4/t/lecture/4775396?start=0
"""

from tkinter import *
import sqlite3
import numpy as np
import itertools as it
#import app5_frontend

def create():
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTs books \
		(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
	conn.commit()
	conn.close()

def insert(title, author, year, isbn):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO books VALUES (NULL, ?,?,?,?)", (title, author, year, isbn))
	conn.commit()
	conn.close()

def update(id, title, author, year, isbn):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", \
		(title, author, year, isbn, id))
	conn.commit()
	conn.close()

def delete(id):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("DELETE FROM books WHERE id=?", (id,))
	conn.commit()
	conn.close()

def search(title='', author='', year='', isbn=''):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", \
		(title,author,year, isbn))
	selected_rows=cur.fetchall()
	#conn.commit()
	conn.close()
	return selected_rows

def view_table():
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM books")
	rows=cur.fetchall()
	#conn.commit()
	conn.close()
	return rows


create()
# insert('The Earch', 'John Smith', 1980, 908223214)
# insert('The Sun', 'Joe 3th', 1976, 908223214)
# update(112,'The Moon', 'Brian 4th', 1917, 908223214 )
# print(view_table())
# for i in it.chain(range(0, 110), range(120, 150)):
# #for i in range(0,112):#np.arange(40,100):#range(30):
# 	delete(i)
# print(view_table())
# print('\n search result: \n' , search(year='1980'))
#print('test running of backend.py in importing')
#print('\nTable: \n', view_table())
#print('\n search result: \n' , search(author='John Smith'))
#print('test')