from tkinter import *
import tkinter as ttk
import sqlite3 as s3

win = Tk()
win.title("Category and Subcategory by M. Shariq Shafiq")


category = str(input("Enter Category name : "))
#category = Label(win, text = "Enter Category name : ")
#category.pack()
parent_id = str(input("Enter Parent id : "))
#parent_id = Label(win, text = "Enter Parent id : ")
#parent_id.pack()


create_table ='''CREATE TABLE IF NOT EXISTS category
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 category_name TEXT,
                 parent_id INTEGER,
                 FOREIGN KEY (parent_id) REFERENCES category(id))'''

con = s3.connect('category.db' , timeout=10)
cur = con.cursor()

data = [(category , parent_id)]

sql = '''insert into category (category_name , parent_id) values(? , ?)'''

res = cur.execute(create_table) 

res1 = cur.executemany(sql , data)

res2 = '''select * from category
    where parent_id is "null"'''

res3 = '''select * from category
    where parent_id is 1'''


res4 = cur.execute(res2)

res_final_1 = cur.fetchall()

res5 = cur.execute(res3)


res_final_2 = cur.fetchall()
print("Main Category : ")
print(res_final_1)
print("Sub-Categories :")
print(res_final_2)

con.commit()

con.close()
