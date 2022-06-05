from data_accessing import msg_flag #when msg_flag is True then print out extracted message

import tkinter as tk
from tkinter import *



wind = tk.Tk()


def done():
    wind.destroy()


Button(
        wind,
        text="EXIT",
        fg='white',
        bg='black',
        padx=19,
        pady=19,
        command=done,
    ).pack()




if( msg_flag==True ):
    from data_accessing import extracted_message
    wind.title("EXTRACTED MESSAGE UNCOVERED (see below)")
    greeting = tk.Label( text='EXTRACTED MESSAGE:\n'+extracted_message )
    greeting.pack()
    wind.geometry('600x400')
    wind['bg'] = '#26dddd'
    wind.mainloop()
else:
    wind.title("ALL FINISHED EMBEDDING MESSAGE")
    greeting = tk.Label(text='Secret message/data has been embedded in your chosen image')
    greeting.pack()
    wind.geometry('600x400')
    wind['bg'] = '#26dddd'
    wind.mainloop()

