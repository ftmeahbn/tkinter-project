from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

from PersonController import PersonController


class PersonUi:
    def clear_text(self):
        self.code.set("")
        self.name.set("")
        self.family.set("")
        self.ability.set("")

    def refresh_table(self):
        for row in self.info_table.get_children():
            self.info_table.delete(row)

        for person in PersonController.find_all():
            self.info_table.insert('', END, values=person)

    def table_select(self,event):
        selected = self.info_table.focus()
        person = self.info_table.item(selected)['values']
        self.code.set(person[0])
        self.name.set(person[1])
        self.family.set(person[2])
        self.ability.set(person[3])

    def save_click(self):
        PersonController.save(self.name_txt.get(), self.family_txt.get(), self.ability_txt.get())
        messagebox.showinfo("Save", "Person Saved")
        self.refresh_table()
        self.clear_text()

    def remove_click(self):
        if messagebox.askyesno("Delete", "Are You Sure?"):
            PersonController.remove(self.code.get())
            messagebox.showinfo("Delete", "Person Removed")
            self.refresh_table()
            self.clear_text()

    def edit_click(self):
        if messagebox.askyesno("Edit", "Are You Sure?"):
            PersonController.edit(self.name.get(), self.family.get(), self.code.get(), self.ability.get())
            messagebox.showinfo("Edit", "Person Edited")
            self.refresh_table()
            self.clear_text()

    def exit_click(self):
        if messagebox.askyesno("Exit", "Are You Sure?"):
            self.window.destroy()

    def search(self,event):
        for row in self.info_table.get_children():
            self.info_table.delete(row)

        for person in PersonController.find_by_family(self.family.get()):
            self.info_table.insert('', END, values=person)

    def __init__(self):
        bg_color = "yellow"
        self.window = Tk()
        self.window.geometry('1000x600')
        self.window.title("Hufflepuff")
        self.window.configure(bg=bg_color)

        # treeview
        self.info_table = ttk.Treeview(self.window, columns=('0', '1', '2','3'), show='headings')

        self.info_table.heading(0, text='ID')
        self.info_table.heading(1, text='Name')
        self.info_table.heading(2, text='Family')
        self.info_table.heading(3, text='ability')

        self.info_table.column(0, width=50)
        self.info_table.column(1, width=150)
        self.info_table.column(2, width=150)
        self.info_table.column(3, width=150)
        

        self.info_table.bind("<ButtonRelease>", self.table_select)
        self.info_table.bind("<KeyRelease>", self.table_select)

        self.info_table.place(x=70, y=150)

        # Labels
        id_lbl = Label(self.window, text='ID', font=("Algerian", 14))
        id_lbl.place(x=20, y=10)
        name_lbl = Label(self.window, text='Name', font=("Algerian", 14))
        name_lbl.place(x=20, y=40)
        family_lbl = Label(self.window, text='Family', font=("Algerian", 14))
        family_lbl.place(x=20, y=70)
        ability_lbl = Label(self.window, text='Ability', font=("Algerian", 14))
        ability_lbl.place(x=20, y=100)
        first_lbl = Label(self.window, text="choose your gender:", font=("Algerian", 14))
        first_lbl.place(x=600 ,y=10)

        self.man = Checkbutton(self.window, text="Man", bg=bg_color)
        self.man.place(x=600 ,y=50)
        self.woman = Checkbutton(self.window, text="Woman", bg=bg_color)
        self.woman.place(x=600 ,y=90)
        
        self.code = IntVar()
        self.name = StringVar()
        self.family = StringVar()
        self.ability = StringVar()

        self.code_txt = Entry(self.window, width=15,textvariable=self.code)
        self.code_txt.place(x=100, y=10)
        self.name_txt = Entry(self.window, width=15,textvariable=self.name)
        self.name_txt.place(x=100, y=40)
        self.family_txt = Entry(self.window, width=15,textvariable=self.family)
        self.family_txt.place(x=100, y=70)
        self.ability_txt = Entry(self.window, width=15,textvariable=self.ability)
        self.ability_txt.place(x=100, y=100)
        self.family_txt.bind("<KeyRelease>", self.search)


        self.save_btn = Button(self.window, text='Save', width=10, command=self.save_click)
        self.save_btn.place(x=70, y=400)
        self.edit_btn = Button(self.window, text='Edit', width=10,command=self.edit_click)
        self.edit_btn.place(x=170, y=400)
        self.remove_btn = Button(self.window, text='Remove', width=10, command=self.remove_click)
        self.remove_btn.place(x=270, y=400)
        self.exit_btn = Button(self.window, text='Exit', width=10,command=self.exit_click)
        self.exit_btn.place(x=370, y=400)

        sec_lbl = Label(self.window, text="choose your age range:", font=("Algerian", 14))
        sec_lbl.place(x=600 ,y=150)

        cmb = ttk.Combobox(self.window)
        cmb['values'] = ["15-17", "18-20", "20-22", "23-25", "26-28"]
        cmb['state'] = 'readonly'
        cmb.current(1)
        cmb.place(x=600 ,y=190)


        self.refresh_table()

        self.window.mainloop()



















        
