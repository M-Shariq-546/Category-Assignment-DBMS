from tkinter import *
import tkinter as ttk
import sqlite3 as s3

win = Tk()
win.title("Category and Subcategory by M. Shariq Shafiq")

category = str(input("Enter Category name : "))

parent_id = int(input("Enter Parent id : "))



create_table ='''create table categories (
                    id INTEGER PRIMARY KEY auto incremented,
                    c_name varchar,
                    parent_id INTEGER,
                    FOREIGN KEY (parent_id) REFERENCES categories(id) )'''

con = s3.connect('categories.db' , timeout=10)
cur = con.cursor()

data = [(category , parent_id)]

sql = '''insert into categories (category , parent_id) values(? , ?)'''

#res = cur.execute(create_table) 

res1 = cur.executemany(sql , data)

res3 = '''select * from categories
    where parent_id is 2'''

res4 = cur.execute(res3)

#print(res4)
res_final = cur.fetchall()

print(res_final)

con.commit()

con.close()
