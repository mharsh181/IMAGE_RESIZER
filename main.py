from PIL import Image, ImageTk
import PIL.Image
from resizeimage import resizeimage
from tkinter import *
from tkinter import filedialog



#making windows
root=Tk()
root.geometry('320x500')
root.title('IMAGE RESIZER')
root.config(bg='gold')

#sest image on bg
canvas=Canvas(root,bg='gold')
canvas.pack()
img=PhotoImage(file='download.png')
canvas.create_image(45, 0, anchor=NW, image=img)
#defina label for app name
Label(root, text='IMAGE RESIZER', font='Verdana 20 bold', fg='black', bg='gold').pack()
Label(root, text='BY HARSH MISHRA', font='Verdana 10 bold', fg='black', bg='gold').pack()

#variable for asl image width and height
width=IntVar()
height=IntVar()

#define label and entry box for ask image size
Label(root, text='Size', font='Verdana 10 bold', fg='black', bg='gold').place(x=10, y=410)
Label(root, text='X', font='Verdana 10 bold', fg='black', bg='gold').place(x=166, y=410)
Label(root, text='Width', font='Verdana 10 bold', fg='black', bg='gold').place(x=70, y=390)
Label(root, text='Height', font='Verdana 10 bold', fg='black', bg='gold').place(x=195, y=390)

#Entry box

Entry(root, textvariable=width, font='Verdana 10 bold', fg='black', bg='gold',borderwidth=3, width=9).place(x=70, y=410)
Entry(root, textvariable=height, font='Verdana 10 bold', fg='black', bg='gold',borderwidth=3, width=9).place(x=190, y=410)


#function for select file for browser
def ChooseFile():
    global filename
    #browser file
    filename=filedialog.askopenfilename(initialdir="/",title="Select a file", filetype=(('JPG File','*.jpg*'),('All Files', '*.*')))
    #change label contents
    label_file_explorer.configure(text='File:'+filename)

#function for convert image
def StartConvert():
    WSize = width.get()
    HSize = height.get()
    with open(str(filename), 'r+b') as f:
        with PIL.Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [WSize, HSize])
            cover.save('1.jpeg', image.format)

    Label(root, text='IMAGE CONVERT SUCCESSFULLY', font='Verdana 10 bold', fg='black', bg='gold').place(x=57, y=500)


#label for file explore
label_file_explorer=Label(root, text="File", font='Verdana 10 bold', fg='black', bg='gold',width=50, height=4)
label_file_explorer.pack()
#design button for call to function
Button(root, text='Choose File', font='Verdana 10 bold', fg='black', bg='gold', command=ChooseFile).place(x=40, y=460)
Button(root, text='Start', font='Verdana 10 bold', fg='black', bg='gold', command=StartConvert).place(x=180, y=460)


root.mainloop()