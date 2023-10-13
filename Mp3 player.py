from tkinter import *
from tkinter import filedialog
import pygame.mixer as mixer
import os
import time
from PIL import ImageTk, Image
from tkinter import ttk
root=Tk()
bg =  ImageTk.PhotoImage(Image.open("E:\Images\wallpaper_453744858.jpg"))
root.geometry('800x500')
root.title('Hari mp3 player')
mixer.init()

def load(listbox):
    os.chdir(filedialog.askdirectory(title='open'))
    for i in os.listdir():
        listbox.insert(END,i)

        
def playsong(song_name:StringVar,song_list:Listbox,status:StringVar):
    song_name.set(song_list.get(ACTIVE))
    mixer.music.load(song_list.get(ACTIVE))
    mixer.music.play()
    status.set('Song Playing')

def stopsong(status:StringVar):
    mixer.music.stop()
    status.set('Song Stopped')

def pausesong(status:StringVar):
    mixer.music.pause()
    status.set('Song Paused')

def resumesong(status:StringVar):
    mixer.music.unpause()
    status.set('Song Resumed')

my_canvas = Canvas(root,width=500,height=300)
my_canvas.pack(fill='both',expand=True)
my_canvas.create_image(0,0,image=bg,anchor='nw')
my_canvas.create_text(40,0,text='Current song',font=('Helvetica',8),fill='white')

listbox_frame = LabelFrame(root, text='Playlist', bg='blue')
listbox_frame.place(x=1200, y=0 )

current_song = StringVar(root, value='<Not selected>')
song_status = StringVar(root, value='<Not Available>')

playlist = Listbox(listbox_frame, font=('Helvetica', 11), selectbackground='red')
scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=BOTH)
playlist.config(width=36,height=43)
scroll_bar.config(command=playlist.yview)
playlist.pack(fill=BOTH, padx=10, pady=0)

Label(my_canvas, text='CURRENTLY PLAYING:', bg='violet', font=('Times', 10, 'bold')).place(x=5, y=20)
song_lbl = Label(my_canvas, textvariable=current_song, bg='Gold', font=("Times", 44), width=25)
song_lbl.place(x=250, y=250)

pause_btn = Button(my_canvas, text='Pause',fg='black', bg='yellow',font=("Georgia", 13), width=7,command=lambda: pausesong(song_status))
pause_btn.place(x=100, y=600)

stop_btn = Button(my_canvas, text='Stop',fg='white', bg='blue', font=("Georgia", 13), width=7, command=lambda: stopsong(song_status))
stop_btn.place(x=300, y=600)

play_btn= Button(my_canvas, text='Play',fg='white', bg='black', font=("Georgia", 13), width=7,command=lambda: playsong(current_song, playlist, song_status))
play_btn.place(x=500, y=600)

resume_btn= Button(my_canvas, text='Resume',fg='white', bg='black', font=("Georgia", 13), width=7, command=lambda: resumesong(song_status))
resume_btn.place(x=700, y=600)

load_btn = Button(my_canvas, text='Load Directory', bg='violet', font=("Georgia", 13), width=35,command=lambda: load(playlist))
load_btn.place(x=20, y=100)


root.update()
root=mainloop()

