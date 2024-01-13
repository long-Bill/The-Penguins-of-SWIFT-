
# import tkinter


# def helloWord(root):
    
#     print('hello world')
#     root.destroy()


# menu = tkinter.Tk()
# menu.title('The Penguins of SWIFT')
# w = 500
# h = 500
# ws = menu.winfo_screenwidth()
# hs = menu.winfo_screenheight()

# x = (ws/2) - (w/2)
# y = (hs/2) - (h/2)

# menu.geometry('%dx%d+%d+%d' % (w, h, x, y))
# start = tkinter.Button(menu, text = 'Start!', command=lambda: helloWord(menu), height=2, width=10)
# start.place(relx=0.5, rely=0.55, anchor='center')

# quit = tkinter.Button(menu, text = 'Quit', command=menu.destroy,height=2,width=10)
# quit.place(relx=0.5, rely=0.70, anchor='center')

# menu.mainloop()






import os
import sys
import subprocess
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

from tkinter import * 
import round

firstround = round.round0(0,script_directory)
#firstround.createImage()

menu = Tk()
menu.title('The Penguins of SWIFT')
w = 500
h = 500
ws = menu.winfo_screenwidth()
hs = menu.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

menu.geometry('%dx%d+%d+%d' % (w, h, x, y))
start = Button(menu, text = 'Check', command=lambda: firstround.checkSolution(), height=2, width=10)
start.place(relx=0.5, rely=0.55, anchor='center')
menu.after(2000,firstround.createImage())
menu.mainloop()


###### GIT CANNOT SEE THIS######







