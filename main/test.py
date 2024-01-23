
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


from tkinter import *
import round
import os
import sys
import subprocess
import docker
import base64

# string = "UGVuZ3VpbkZsYWc="
# bin = base64.b64decode(string)
# print(bin.decode('utf-8'))
completed = 1
totalRounds = 10

endMenu = Tk()
endMenu.protocol("WM_DELETE_WINDOW" , closing_menu)

endMenu.title('The Penguins of SWIFT')
w = 500
h = 250
ws = endMenu.winfo_screenwidth()
hs = endMenu.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

endMenu.geometry('%dx%d+%d+%d' % (w, h, x, y))

Progress = Label(endMenu, text=f'Completed rounds: {completed} / {totalRounds}')
Progress.place(relx= 0.5, rely=0.3, anchor='center')
quit = Button(endMenu,
              text='Quit',
              command=lambda: quitGame(menu),
              height=2, width=10
              )
quit.place(relx=0.5,
           rely=0.70,
           anchor='center'
           )

endMenu.mainloop() 

# import base64

# #string to encode
# string = 'pppfoo???'
# #convert string to bytes
# string_encode = string.encode('utf-8')
# #ecode in base 64
# encoded = base64.b64encode(string_encode, altchars=b'-:')
# #display encode data
# print(encoded)
# #decode from base 64
# decoded = base64.b64decode(encoded,  altchars=b'-:')
# #convert from bytes to string and display
# print(decoded.decode('utf-8'))
# #print(string.decode('utf-8'))