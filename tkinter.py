from Tkinter import *
import crawler_index_querying
from PIL import ImageTk,Image

def loadEntry  () :
    e=crawler_index_querying.searcher('searchindex.db')
    s=e.query(nameVar.get())
    T.delete("1.0",END)
    
    for i in s:
      T.insert(END,i)
      T.insert(END,"\n")
    

def makeWindow () :
    global nameVar, select,T
    win = Tk()
    win.title("Varun's Personal Search Engine for Programming Languages")
    im = Image.open('t1.png')
    im=im.resize((700,150),Image.ANTIALIAS)
    tkimage = ImageTk.PhotoImage(im)
    myvar=Label(win,image = tkimage)
    myvar.image=tkimage
    myvar.pack()

    frame1 = Frame(win)
    l=Label(win,text="WELCOME TO MY SEARCH ENGINE",font=("comic sans ms", 20),fg="black")
    l.pack()
    Label(frame1, text="Query",font=("comic sans ms", 16)).grid(row=0, column=0, sticky=W)
    nameVar = StringVar()
    name = Entry(frame1, textvariable=nameVar,bd=5,width=50)
    name.grid(row=0, column=1, sticky=W)
    frame1.pack(expand=True)

    frame2 = Frame(win)       
    frame2.pack()
    b1 = Button(frame2,text=" Search ",command=loadEntry,font=("comic sans ms", 12))
    b1.pack(side=LEFT)

    frame3= Frame(win)
    T = Text(win, height=30, width=100, bd=5,spacing1=2)
    T.pack()
    T.delete("1.0",END)
    frame3.pack()
  

win = makeWindow()
mainloop()
