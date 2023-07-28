from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from PersonUI import PersonUi
from Person2UI import Person2Ui
from Person3UI import Person3Ui
from Person4UI import Person4Ui


def gry_click():
    Gryffindor  = Person2Ui()

def huff_click():
    Hufflepuff  = PersonUi()
    
def raw_click():
    Ravenclaw  = Person3Ui()

def sly_click():
    Slytherin  = Person4Ui()


    
bg_color = "white"
gry_color = "tomato"
huff_color = "yellow"
rav_color = "royalblue"
sly_color = "limegreen"


window = Tk()
window.title("hogwarts school")
window.geometry("800x550")
window.configure(bg=bg_color)


photo = ImageTk.PhotoImage(Image.open("logo.jpg"))
window.iconphoto(False, photo)

img = ImageTk.PhotoImage(Image.open("Doc2-1.png"))
lbl = Button(window, image=img,bg=bg_color).place(x=250, y=10)

first_lbl = Label(window, text="hogwarts School of Witchcraft and Wizardry is a fictional British ", font=("Algerian", 16)).place(x=20, y=270)
sec_lbl = Label(window, text="boarding school of magic for students aged eleven to eighteen ", font=("Algerian", 16)).place(x=40, y=300)


Button(window, text="Gryffindor", font=("Algerian", 16), bg=gry_color, command=gry_click).place(x=40, y=400)
Button(window, text="Hufflepuff", font=("Algerian", 16), bg=huff_color, command=huff_click).place(x=240, y=400)
Button(window, text="Ravenclaw", font=("Algerian", 16), bg=rav_color, command=raw_click).place(x=440, y=400)
Button(window, text="Slytherin", font=("Algerian", 16),bg=sly_color, command=sly_click).place(x=640, y=400)

window.mainloop()























