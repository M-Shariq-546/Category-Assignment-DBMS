import tkinter
from tkinter import messagebox
from tkinter import ttk
import sqlite3 as s3

#Function to Store Data in DBMS
def getDataFromDBMS():
    
    category = main_category_entry.get()
    parent_id = parent_id_entry.get()
    
    
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
    #These Print is Used to print Category and Sub Categories to console
    print("Main Category : ")
    print(res_final_1)
    print("Sub-Categories :")
    print(res_final_2)

    con.commit()

    con.close()


#U.I Code
win = tkinter.Tk()
win.title("Category and Subcategory by M. Shariq Shafiq")

frame = tkinter.Frame(win)
frame.pack()

#Heading
category_info = tkinter.LabelFrame(frame , text="Category and SubCAtegory Info")
category_info.grid(row=0 ,column=0)

#Labels Headings 
main_category_label = tkinter.Label(category_info, text="Enter Category Name : ")
main_category_label.grid(row=0 , column=0)

parent_id_label = tkinter.Label(category_info , text="Enter Parent id : ")
parent_id_label.grid(row=0 , column=2)

#Entry Bars
main_category_entry = tkinter.Entry(category_info)
parent_id_entry = tkinter.Entry(category_info)
main_category_entry.grid(row=1 , column=0)
parent_id_entry.grid(row=1 , column=2)

#Button Clicked to Enter Data
button = tkinter.Button(frame , text="Click To Add Data" , command=getDataFromDBMS)
button.grid(row=3 , column=2 , sticky="news" , padx=15 , pady=15)

win.mainloop()
