import tkinter
from tkinter import messagebox
from tkinter import ttk
import sqlite3 as s3


def MainCategory():
    con = s3.connect('category.db' , timeout=10)
    cur = con.cursor()
    
    res2 = '''select * from category
        where parent_id is "null"'''
    
    res4 = cur.execute(res2)

    res_final_1 = cur.fetchall()

    #These Print is Used to print Category and Sub Categories to console
    print("Main Category : ")
    print(res_final_1)
    label3.configure(text=f"Main Categories : {res_final_1} \n")
    
    con.commit()

    con.close()




def SubCategory():
    con = s3.connect('category.db' , timeout=10)
    cur = con.cursor()

    res3 = '''select * from category
        where parent_id between 1 and 100 '''

    res5 = cur.execute(res3)


    res_final_2 = cur.fetchall()
    #SubCategories
    print("Sub-Categories :")
    print(res_final_2)

    label4.configure(text=f"Sub Categories :\n {res_final_2} \n")


    con.commit()

    con.close()


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
        where parent_id between 1 and 100 '''

    res4 = cur.execute(res2)

    res_final_1 = cur.fetchall()

    res5 = cur.execute(res3)


    res_final_2 = cur.fetchall()
    #These Print is Used to print Category and Sub Categories to console
    print("Main Category : ")
    print(res_final_1 , end="\n")
    print("Sub-Categories :")
    print(res_final_2 ,end="\n")
 
    con.commit()

    con.close()


#U.I Code
win = tkinter.Tk()
win.title("Category and Subcategory by M. Shariq Shafiq")
win.configure(bg='Black')
win.geometry("920x550")


frame = tkinter.Frame(win , bg='Black')
frame.pack(fill='both')

#Heading
category_info = tkinter.LabelFrame(frame , text="Category and Sub-Category Info" , font=("Courier 20 bold"))
category_info.configure(bg='Black' , fg='white')
category_info.grid(row=0 ,column=0 )

#Labels Headings 
main_category_label = tkinter.Label(category_info, text="Enter Category Name : " , font=("Courier 15 bold"))
main_category_label.configure(bg='Black' , fg='white')
main_category_label.grid(row=0 , column=0)

parent_id_label = tkinter.Label(category_info , text="Enter Parent id : " , font=("Courier 17 bold"))
parent_id_label.configure(bg='Black' , fg='white')
parent_id_label.grid(row=1 , column=0)

#Entry Bars
main_category_entry = tkinter.Entry(category_info)
parent_id_entry = tkinter.Entry(category_info)
main_category_entry.grid(row=0 , column=1)
main_category_entry.configure(bg='white' , fg='black')
parent_id_entry.grid(row=1 , column=1)
parent_id_entry.configure(bg='white' , fg='black')

#Button Clicked to Enter Data
button1 = tkinter.Button(frame , text="Get Main Categories" , command=MainCategory)
button1.configure(bg='green' , fg='aqua')
button1.grid(row=3 , column=0 , sticky="news" , padx=5 , pady=5)

button2 = tkinter.Button(frame , text="Get Sub-Categories" , command=SubCategory)
button2.configure(bg='green' , fg='aqua')
button2.grid(row=3 , column=1 , sticky="news" , padx=5 , pady=5)

button3 = tkinter.Button(frame , text="Click To Add Data" , command=getDataFromDBMS)
button3.configure(bg='orange' , fg='black')
button3.grid(row=3 , column=2 , sticky="news" , padx=5 , pady=5)

label2=tkinter.Label(win, text="The Data Will be displayed here : ", font=("Courier 15 bold"))
label2.configure(bg='black',fg='cyan')
label2.pack()
frame.rowconfigure((0,1,2) , weight = 1)
frame.columnconfigure((0,1) , weight = 1)


label3=tkinter.Label(win, text="", font=("Courier 15 bold"))
label3.configure(bg='black',fg='White')
label3.pack()
frame.rowconfigure((0,1,2) , weight = 1)
frame.columnconfigure((0,1) , weight = 1)

label4=tkinter.Label(win, text="", font=("Courier 15 bold"))
label4.configure(bg='black',fg='White')
label4.pack()
frame.rowconfigure((0,1,3) , weight = 1)
frame.columnconfigure((0,1) , weight = 1)

label5=tkinter.Label(win, text="", font=("Courier 15 bold"))
label5.configure(bg='black',fg='White')
label5.pack()
frame.rowconfigure((0,1,4) , weight = 1)
frame.columnconfigure((0,1) , weight = 1)


win.mainloop()
