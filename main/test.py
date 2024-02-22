import docker
import subprocess
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import base64
from PIL import ImageTk, Image
roundsCompleted = 50
numberOfDirectory = 20
endMenu = Tk()
endMenu.title('End of Game')
w = 550
h = 500
ws = endMenu.winfo_screenwidth()
hs = endMenu.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

endMenu.geometry('%dx%d+%d+%d' % (w, h, x, y))
endMenu.configure(bg="#303030")
img = PhotoImage(file="assets/private.png")
img = img.subsample(6)
picture = Label(endMenu, image= img,bg="#303030")
picture.place(relx=0.5, rely=0.25, anchor='center')
Progress = Label(endMenu, text=f'Completed rounds: {roundsCompleted} / {numberOfDirectory}', font=("Monospace",25),bg="#303030",fg="green")
Progress.place(relx= 0.5, rely=0.55, anchor='center')
thank = Label(endMenu, text="Thank you for playing!", font=("Monospace",20),bg="#303030",fg="white")
thank.place(relx= 0.5, rely=0.65, anchor='center')
quit = Button(endMenu,
            text='Quit',
            
            height=2, width=10,
            bg="#ffab40",foreground="white"
            )
quit.place(relx=0.5,
        rely=0.80,
        anchor='center'
        )

endMenu.mainloop() 