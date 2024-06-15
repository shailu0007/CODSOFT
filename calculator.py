from tkinter import *

def click(event=None):
    global scvalue
    text = event.widget.cget("text")
    if text == "C":
       scvalue.set("")
       screen.update()
    elif text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                value = "ERROR"
            
        scvalue.set(value)
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("320x700")
root.title("CODSOFT- calculator")

scvalue = StringVar()
scvalue.set("")
#entry() function use for creating text field
#pack() function use for adding component to main screen
screen = Entry(root,textvariable=scvalue,font=("lucida",40,"bold"))
screen.pack(fill=X,ipadx=8,pady=10,padx=10)

f1 = Frame(root,bg="grey")
b = Button(f1,text="9",width=2,height=1,font=("lucida",40,"bold"))
b.pack(side=LEFT,padx=2,pady=1)
b.bind("<Button-1>",click)

b1 = Button(f1,text="8",width=2,height=1,font=("lucida",40,"bold"))
b1.pack(side=LEFT,padx=2,pady=1)
b1.bind("<Button-1>",click)

b2 = Button(f1,text="7",width=2,height=1,font=("lucida",40,"bold"))
b2.pack(side=LEFT,padx=2,pady=1)
b2.bind("<Button-1>",click)

f1.pack()

f1 = Frame(root,bg="grey")
b = Button(f1,text="6",width=2,height=1,font=("lucida",40,"bold"))
b.pack(side=LEFT,padx=2,pady=1)
b.bind("<Button-1>",click)

b1 = Button(f1,text="5",width=2,height=1,font=("lucida",40,"bold"))
b1.pack(side=LEFT,padx=2,pady=1)
b1.bind("<Button-1>",click)

b2 = Button(f1,text="4",width=2,height=1,font=("lucida",40,"bold"))
b2.pack(side=LEFT,padx=2,pady=1)
b2.bind("<Button-1>",click)

f1.pack()

f1 = Frame(root,bg="grey")
b = Button(f1,text="3",width=2,height=1,font=("lucida",40,"bold"))
b.pack(side=LEFT,padx=2,pady=1)
b.bind("<Button-1>",click)

b1 = Button(f1,text="2",width=2,height=1,font=("lucida",40,"bold"))
b1.pack(side=LEFT,padx=2,pady=1)
b1.bind("<Button-1>",click)

b2 = Button(f1,text="1",width=2,height=1,font=("lucida",40,"bold"))
b2.pack(side=LEFT,padx=2,pady=1)
b2.bind("<Button-1>",click)

f1.pack()

f1 = Frame(root,bg="grey")
b = Button(f1,text="0",width=2,height=1,font=("lucida",40,"bold"))
b.pack(side=LEFT,padx=2,pady=1)
b.bind("<Button-1>",click)

b1 = Button(f1,text="C",width=2,height=1,font=("lucida",40,"bold"))
b1.pack(side=LEFT,padx=2,pady=1)
b1.bind("<Button-1>",click)

b2 = Button(f1,text="=",width=2,height=1,font=("lucida",40,"bold"))
b2.pack(side=LEFT,padx=2,pady=1)
b2.bind("<Button-1>",click)

f1.pack()

f1 = Frame(root,bg="grey")
b = Button(f1,text="+",width=2,height=1,font=("lucida",40,"bold"))
b.pack(side=LEFT,padx=2,pady=1)
b.bind("<Button-1>",click)

b1 = Button(f1,text="-",width=2,height=1,font=("lucida",40,"bold"))
b1.pack(side=LEFT,padx=2,pady=1)
b1.bind("<Button-1>",click)

b2 = Button(f1,text="*",width=2,height=1,font=("lucida",40,"bold"))
b2.pack(side=LEFT,padx=2,pady=1)
b2.bind("<Button-1>",click)

f1.pack()

f1 = Frame(root,bg="grey")
b = Button(f1,text="/",width=2,height=1,font=("lucida",40,"bold"))
b.pack(side=LEFT,padx=2,pady=1)
b.bind("<Button-1>",click)

b1 = Button(f1,text="%",width=2,height=1,font=("lucida",40,"bold"))
b1.pack(side=LEFT,padx=2,pady=1)
b1.bind("<Button-1>",click)

b2 = Button(f1,text="",width=2,height=1,font=("lucida",40,"bold"))
b2.pack(side=LEFT,padx=2,pady=1)
b2.bind("<Button-1>",click)

f1.pack()



root.mainloop()
