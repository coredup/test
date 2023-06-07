from tkinter import *
from tkinter import ttk

root = Tk()
root.title("ycla.coding")
root.geometry('300x200')

#Определим данные для отображения 
students = [("Андрей"),17, "andrew228@gmail.com"]



#Определим столбцы
columns = ("name","age","email")


tree = ttk.Treeview(columns=columns, show="")
tree.pack(fill=BOTH, expand=1)

#Определим заголовки 
tree.heading("name", text="Имя")
tree.heading("name", text="Имя")
tree.heading("name", text="Имя")


#Добавляем данные
for student in students:
    tree.insert("",END, values=student)
root.mainloop()    