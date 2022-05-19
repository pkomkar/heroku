from os import path
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil







#function
def select_path():
    #allows user to select directory
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    #get user path
    get_link = link_field.get()
    #getselect path
    user_path = path_label.cget("text")
    screen.title("Downloading...")
    #download video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4_video)
    video_clip.close()

    #movie file to selected directory
    shutil.move(mp4_video,user_path)
    screen.title("Download Complet!! Download another file...")

screen = Tk()
title = screen.title("Youtube Download")
canvas = Canvas(screen, width=500,height=500)
canvas.pack()

# image logo
logo_img = PhotoImage(file="hi.png")
#resize
logo_img = logo_img.subsample(3,3)
canvas.create_image(250,80, image = logo_img)

# link
link_field = Entry(screen,width=50)
link_label = Label(screen, text="Enter Download Link:",foreground="red",font=("Arial",10))

#select path for saving file
path_label = Label(screen,text= "Select Path for Download",background="purple",foreground="white",font=("Arial",10))
select_button = Button(screen,text= "Select" ,command = select_path , background="black",foreground="white")
canvas.create_window(250,280,window=path_label)
canvas.create_window(250,330,window=select_button)

#Add widgets to window
canvas.create_window(250,170,window= link_label)
canvas.create_window(250,220,window= link_field)

#button
download_button = Button(screen, text="Download File!!", command=download_file)
#add to canvas
canvas.create_window(250,390,window=download_button)
screen.mainloop()