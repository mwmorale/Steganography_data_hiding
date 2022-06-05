import tkinter as tk
from tkinter import *

theds = []
end_name = ''

embed = [False]
extract = [False]





wind = tk.Tk()
wind.title("EMBED OR EXTRACT MESSAGE FROM IMAGE")

greeting_text1 = '\nHello! You have two options here...\n\n1. Embed a secret message within the image \nOR\n2.'
greeting_text2 = ' Extract the most recent secret message within image\n'
greeting_text_final = greeting_text1 + greeting_text2

greeting = tk.Label( text=greeting_text_final )
greeting.pack()
wind.geometry('500x400')
wind['bg'] = '#26dddd'



def do_destroy():
    wind.destroy()



def choose_embed():
    embed[0] = True
    do_destroy()



def choose_extract():
    extract[0] = True
    do_destroy()





Button(
    wind,
    text="EMBED MESSAGE",
    padx=15,
    pady=5,
    command=choose_embed
    ).pack()

Button(
    wind,
    text="EXTRACT MESSAGE",
    padx=10,
    pady=5,
    command=choose_extract
    ).pack()

Button(
    wind,
    text="CANCEL",
    bg='white',
    fg='black',
    padx=0,
    pady=5,
    command=do_destroy
    ).pack()




wind.mainloop()



