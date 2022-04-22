from time import time
from tkinter import *
from tkinter import ttk
from tkmainwindow import TkMainwindow

class Mainwindow(TkMainwindow):
    def __init__(self, master :Tk, **kw):
        super().__init__(master, **kw)

        self.item_menu = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.item_menu, label='Item', underline= 0)

        # Add Menu Items
        self.item_menu.add_command(label='Insert Item', command=self.insert_item)
        self.item_menu.add_command(label='Insert Subitem', command=self.insert_subitem)
        self.item_menu.add_separator()
        self.item_menu.add_command(label='Remove Item', command=self.remove_item)
        self.item_menu.add_command(label='Remove All', command=self.remove_all)
        self.item_menu.add_command(label='Modify Item', command=self.modify_item)
        self.item_menu.add_separator()
        self.item_menu.add_command(label='Move Up', command=self.move_up)
        self.item_menu.add_command(label='Move Down', command=self.move_down)




        # column_name : (heading, width, anchor)
        cols = {
            'A' : ('A', 50, CENTER),
            'B' : ('B', 50, E),
            'C' : ('C', 50, W)
        }

        self.tree = ttk.Treeview(self.mainframe, columns=tuple(cols.keys()))
        for k in cols:
            self.tree.heading(k, text=cols[k][0])
            self.tree.column(k, width=cols[k][1], anchor=cols[k][2])
        self.tree.grid(column=0, row=0, sticky=NSEW)

        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.columnconfigure(0, weight=1)

        self.values = [1,10,100]

        master.title('Mainwindow')
        self.master.geometry('600x400')
        self.showmessage('Ready.')

    def insert_item(self):
        self.values = [v + 1 for v in self.values]
        focus_item = self.tree.focus()
        self.showmessage(focus_item)
        if focus_item == '':
            self.tree.insert('', 'end', text=str(time()), values=self.values)    
        else:
            self.tree.insert(self.tree.parent(focus_item), 'end', text=str(time()), values=self.values)    

    def insert_subitem(self):
        self.values = [v + 1 for v in self.values]
        self.tree.insert(self.tree.focus(), 'end', text=str(time()), values=self.values)        

    def remove_item(self):
        self.tree.delete(self.tree.focus())

    def remove_all(self):
        top_items = self.tree.get_children()
        for item in top_items:
            self.tree.delete(item)

    def modify_item(self):
        focus_item = self.tree.focus()
        if focus_item != '':
            self.values = [v + 1 for v in self.values]
            for i, v in enumerate(self.values):
                self.tree.set(focus_item, i, v)



root = Tk()
Mainwindow(root)
root.mainloop()