from tkinter import *
from PIL import ImageTk, Image
import os
# import random
from pygame import mixer
from functools import partial
import tkinter.ttk as ttk

root=Tk()
root.geometry("505x700")
root.maxsize(505,700)
root.title("AJ Player")
root.configure(background="brown")

# photo=PhotoImage(file="dummy/music.png")
# label_1=Label(image=photo)
# label_1.pack(pady=40)

image1 = Image.open('dummy/play.png')
image1 = image1.resize((50,50), Image.ANTIALIAS)
my_img1 = ImageTk.PhotoImage(image1)

image2 = Image.open('dummy/pause.png')
image2 = image2.resize((50,50), Image.ANTIALIAS)
my_img2 = ImageTk.PhotoImage(image2)

image3 = Image.open('dummy/previous.png')
image3 = image3.resize((50,50), Image.ANTIALIAS)
my_img3 = ImageTk.PhotoImage(image3)

image4 = Image.open('dummy/next.png')
image4 = image4.resize((50,50), Image.ANTIALIAS)
my_img4 = ImageTk.PhotoImage(image4)

frame = Frame(root, borderwidth=5, bg="orange",relief=SUNKEN)
length_in_secs=0
def clear_frame():
    for widgets in topframe.winfo_children():
        widgets.destroy()

topframe=Frame(root, borderwidth=3, bg="orange",relief=SUNKEN)
current=""

def start(a):
    global current
    mixer.init()
    mixer.music.load(f"dummy/music/{a}")
    current=a
    mixer.music.set_volume(0.7)
    mixer.music.play()
    clear_frame()
    current_time=mixer.music.get_pos()

    def shift():
        x1, y1, x2, y2 = canvas.bbox("marquee")
        if (x2 < 0 or y1 < 0):  # reset the coordinates
            x1 = canvas.winfo_width()
            y1 = canvas.winfo_height() // 2
            canvas.coords("marquee", x1, y1)
        else:
            canvas.move("marquee", -2, 0)
        canvas.after(1000 // fps, shift)

    canvas = Canvas(topframe, bg='black')
    canvas.pack(fill=X, ipady=15)
    text_var = a
    text = canvas.create_text(0, -2000, text=text_var, font=('Times New Roman', 20, 'bold'), fill='white',
                              tags=("marquee",), anchor='w')
    x1, y1, x2, y2 = canvas.bbox("marquee")
    width = x2 - x1
    height = y2 - y1
    canvas['width'] = width
    canvas['height'] = height
    fps = 40  # Change the fps to make the animation faster/slower
    shift()
    print(a)

def play():
    mixer.music.unpause()

def pause():
    mixer.music.pause()

def previous():
    music_dir = 'D:\\tkinterproject\\dummy\\music'
    songs = os.listdir(music_dir)
    songs.remove("desktop.ini")
    print(current)
    if current in songs:
        x=songs.index(current)
    start(songs[x-1])

def next():
    music_dir = 'D:\\tkinterproject\\dummy\\music'
    songs = os.listdir(music_dir)
    songs.remove("desktop.ini")
    print(current)
    if current in songs:
        x = songs.index(current)
    if x == (len(songs)-1):
        start(songs[0])
    else:
        start(songs[x+1])

# b = Button(frame, text="Start", bg="violet", font=("lucida 15 italic"),borderwidth=5,relief=SUNKEN,command=start).pack(side=TOP,padx=10,ipadx=10, ipady=2,pady=10)

b1 = Button(frame, text="<<", bg="yellow", font=("lucida 15 italic"),image=my_img3,borderwidth=5,relief=SUNKEN,command=previous).pack(side=LEFT,padx=10,ipadx=20, ipady=20)

b2 = Button(frame, text="Play", bg="green", font=("lucida 15 italic"),image=my_img1,borderwidth=5,relief=SUNKEN,command=play).pack(side=LEFT,padx=10,ipadx=20, ipady=20)

b3 = Button(frame, text="Pause", bg="red", font=("lucida 15 italic"),image=my_img2,borderwidth=5,relief=SUNKEN,command=pause).pack(side=LEFT,padx=10,ipadx=20, ipady=20)

b4 = Button(frame, text=">>", bg="yellow", font=("lucida 15 italic"),image=my_img4,borderwidth=5,relief=SUNKEN,command=next).pack(side=LEFT,padx=10,ipadx=20, ipady=20)


topframe.pack(fill=X,padx=5,side=TOP,anchor="nw",pady=10)

frame.pack(fill=X,side=TOP,ipadx=180,ipady=50,padx=5,pady=10)
label1=Label(root,text="Playlist",font=("lucida 18 italic bold"),bg="white",fg="black").pack(anchor="nw",ipadx=5,padx=5,ipady=10)
# frame2=Frame(root, borderwidth=6, bg="blue")
# b4 = Button(frame2, text="Playlist", bg="green", font=("lucida 10 italic")).pack(side=BOTTOM,padx=10,ipadx=10, ipady=10)
# frame2.pack()

wrapper1=LabelFrame(root,relief=SUNKEN,borderwidth=6)
wrapper2=LabelFrame(root)

mycanvas=Canvas(wrapper1)
mycanvas.pack(side=LEFT,fill=BOTH,expand=True)

yscrollbar=ttk.Scrollbar(wrapper1,orient="vertical",command=mycanvas.yview)
yscrollbar.pack(side=RIGHT,fill=Y)

mycanvas.configure(yscrollcommand=yscrollbar.set)

mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

myframe=Frame(mycanvas)
mycanvas.create_window((0,0),window=myframe,anchor="nw")

wrapper1.pack(fill=BOTH,expand=True,padx=5,pady=10)
# wrapper2.pack(fill=BOTH,expand=True,padx=10,pady=10)

music_dir = 'D:\\tkinterproject\\dummy\\music'
songs = os.listdir(music_dir)
songs.remove("desktop.ini")
print(songs)
listbox = Listbox(myframe)
for i in songs:
    button=Button(myframe,text=f"{i}",command=partial(start, i),bg="white")
    button.pack(side=TOP,anchor="nw",padx=2)
root.mainloop()