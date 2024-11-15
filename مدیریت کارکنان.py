from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("مديريت کارکنان کارگاه")
root.geometry("900x300")
root.resizable(False,False)
root.config( bg = "seashell3" )
#=================================================================================================#
data = sqlite3.connect("Database.db")
xdata = data.cursor()
xdata.execute("""CREATE TABLE IF NOT EXISTS Specifications
             (id INTEGER PRIMARY KEY,
             Salary REAL,
             The_Amount_Of_Work_Hours REAL,
             Working_Hours_This_Month INTEGER,
             Last_Name TEXT,
             Date_Of_Employment INTEGER,
             First_Name TEXT,
             ID_Code INTEGER
)
""")
data.commit()
#=================================================================================================#
def Add_worker():
   Work_Page.delete(0, END)
   fname = Entry_Text_6.get()
   lname = Entry_Text_4.get()
   TAOWH = int(Entry_Text_2.get())
   ID = Entry_Text_7.get()
   date = Entry_Text_5.get()
   WHTM = int(Entry_Text_3.get())
   salary = TAOWH * WHTM
   file_name = "Workers.db"
    
   connection = sqlite3.connect(file_name)
   cursor = connection.cursor()

   records = [fname, lname, TAOWH, ID, date, WHTM, salary]

   insert_query = """INSERT INTO Specifications (First_Name, Last_Name, The_Amount_Of_Work_Hours,
   ID_Code, Date_Of_Employment, Working_Hours_This_Month, Salary) VALUES (?, ?, ?, ?, ?, ?, ?)"""
   cursor.execute(insert_query, records)

   Entry_Text_6.delete(0, END)
   Entry_Text_4.delete(0, END)
   Entry_Text_2.delete(0, END)
   Entry_Text_7.delete(0, END)
   Entry_Text_5.delete(0, END)
   Entry_Text_3.delete(0, END)

   connection.commit()
   Work_Page.insert(END, "با موفق ذخيره شد")
   connection.close()
#=================================================================================================#
def Search_worker():
   name = Entry_Text_6.get()
   xdata.execute("SELECT * FROM Specifications WHERE name=?", (name,))
   Specifications = xdata.fetchone()
   if Specifications:
      Entry_Text_1.delete(0, END)
      Entry_Text_1.delete(0, product[1])

      Entry_Text_2.delete(0, END)
      Entry_Text_2.delete(0, product[2])
      
      Entry_Text_3.delete(0, END)
      Entry_Text_3.delete(0, product[3])
      
      Entry_Text_4.delete(0, END)
      Entry_Text_4.delete(0,product[4])
      
      Entry_Text_5.insert(0, END)
      Entry_Text_5.delete(0, product[5])
      
      Entry_Text_6.insert(0, END)
      Entry_Text_6.insert(0, product[6])
      
      Entry_Text_7.delete(0, END)
      Entry_Text_7.insert(0, product[7])
   else:
      messagebox.showwarning("خطا", ". کارگري با اين نشخصات پيدا نشد")
#=================================================================================================#

def view_worker():
   Work_Page.delete(0, END)
   xdata.execute("SELECT * FROM Specifications")
   rows = xdata.fetchall()
   for row in rows:
      Work_page.insert(END, row)

#=================================================================================================#

def delete_worker():
   worker_id = Entry_Text_6.get()
   xdata.execute("DELETE FROM Specifications WHERE id = ?", (worker_id,))
   data.commit()
   messagebox.showinfo("موفقيت", ". کارگر با موفقيت حذف شد")
   view_worker()
#=================================================================================================#
Text_1 = Label( root , text = " حقوق اين ماه " , font = 20 , bg = "seashell3" )
Text_1.place( x = 20 , y = 10 )

Entry_Text_1 = Entry (root , bg = "white", bd = 3, relief = "groove" )
Entry_Text_1.place(width = 110 , height = 50 , x = 5 , y = 35)
#=================================================================================================#
Text_2 = Label( root , text = " مبلغ ساعت کار " , font = 20 , bg = "seashell3" )
Text_2.place( x = 140 , y = 10 )

Entry_Text_2 = Entry (root , bg = "white", bd = 3, relief = "groove" )
Entry_Text_2.place(width = 120 , height = 30 , x = 260 , y = 8)
#=================================================================================================#
Text_3 = Label( root , text = " ساعت کار اين ماه" , font = 20 , bg = "seashell3" )
Text_3.place( x = 135 , y = 52 )

Entry_Text_3 = Entry (root , bg = "white", bd = 3, relief = "groove" )
Entry_Text_3.place(width = 120 , height = 30 , x = 260 , y = 52)
#=================================================================================================#
Text_4 = Label( root , text = "  نام خانودگي کارگر " , font = 20 , bg = "seashell3" )
Text_4.place( x = 440, y = 10 )

Entry_Text_4 = Entry (root , bg = "white", bd = 3, relief = "groove" )
Entry_Text_4.place(width = 120 , height = 30 , x = 560 , y = 8)
#=================================================================================================#
Text_5 = Label( root , text = "  تاريخ استخدام " , font = 20 , bg = "seashell3" )
Text_5.place( x = 450 , y = 52 )

Entry_Text_5 = Entry (root , bg = "white", bd = 3, relief = "groove" )
Entry_Text_5.place(width = 120 , height = 30 , x = 560 , y = 52)
#=================================================================================================#
Text_6 = Label( root , text = " نام کارگر  " , font = 20 , bg = "seashell3" )
Text_6.place( x = 700  , y = 10 )

Entry_Text_6 = Entry (root , bg = "white", bd = 3, relief = "groove" )
Entry_Text_6.place(width = 120 , height = 30 , x =  770 , y = 8)
#=================================================================================================#
Text_7 = Label( root , text = " کد ملي  " , font = 20 , bg = "seashell3" )
Text_7.place( x = 710 , y = 52 )

Entry_Text_7 = Entry (root , bg = "white", bd = 3, relief = "groove" )
Entry_Text_7.place(width = 120 , height = 30 , x = 770 , y = 52)



#=================================================================================================#
btn_1 = Button ( root , text = " مشاهده همه " ,  font = 20 , bg =  "seashell4" , command = view_worker )
btn_1.place(width = 148 ,x = 740 , y = 100)
#=================================================================================================#
btn_2 = Button ( root , text = " جست و جو  " ,  font = 20 , bg =  "seashell4" , command = Search_worker)
btn_2.place(width = 148 , x = 580 , y = 100)
#=================================================================================================#
btn_3 = Button ( root , text = " اضافه کردن " ,  font = 20 , bg =  "seashell4" , command = Add_worker )
btn_3.place(width = 148 , x = 580 , y = 165)
#=================================================================================================#
btn_4 = Button ( root , text = " مرتب کردن " ,  font = 20 , bg =  "seashell4" )
btn_4.place(width = 148 , x = 740 , y = 165)
#=================================================================================================#
btn_5 = Button ( root , text = " خروج  " ,  font = 20 , bg =  "seashell4"  , command = quit)
btn_5.place(width = 148 , x = 580 , y = 230)
#=================================================================================================#
btn_6 = Button ( root , text = "  حذف کردن " ,  font = 20 , bg =  "seashell4" )
btn_6.place(width = 148 , x = 740 , y = 230)
#=================================================================================================#
scroll_1 = Scrollbar (root , bd = 1, relief = "groove" ,width = 20)
scroll_1.place(height = 180 , x = 520, y = 100)

Work_Page = Listbox (root ,yscrollcommand = scroll_1.set, bg = "skyblue" , relief = "flat", width = 50)
Work_Page.place( width = 500 ,height = 180, x = 5 , y = 100)

scroll_1.config(command = Work_Page.yview)
#=================================================================================================#
root.mainloop()
