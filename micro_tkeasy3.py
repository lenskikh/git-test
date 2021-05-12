from tkinter import *

root = Tk()

tab1 = {"New":"1","Save":"2"}
tab2 = {"Edit":"3","Copy":"4"}
name_of_tab ="File"
     
def top_menu(name_of_tab,tab1,tab2):

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)


    menubar.add_cascade(label=name_of_tab, menu=filemenu)

    for name_in_menu in tab1:
        print(name_in_menu)
        filemenu.add_command(label=name_in_menu, 
        command=tab1[name_in_menu])

    root.config(menu=menubar)

top_menu(name_of_tab,tab1,tab2)

root.mainloop()