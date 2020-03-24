from tkinter import *
from tkinter import messagebox

cl=True

def click(buttons):
    global cl
    if buttons["text"]==" " and cl==True:
        buttons["text"]="X"
        buttons["relief"]=SUNKEN
        cl=False
    elif buttons["text"]==" " and cl==False :
        buttons["text"]="O"
        buttons["relief"] = SUNKEN
        cl=True

    elif (button_1['text']=='X' and button_2['text']=='X' and button_3['text']=='X' or
          button_4['text']=='X' and button_5['text']=='X' and button_6['text']=='X' or
          button_7['text']=='X' and button_8['text']=='X' and button_9['text']=='X' or
          button_1['text']=='X' and button_4['text']=='X' and button_7['text']=='X' or
          button_2['text']=='X' and button_5['text']=='X' and button_8['text']=='X' or
          button_3['text']=='X' and button_6['text']=='X' and button_9['text']=='X' or
          button_1['text']=='X' and button_5['text']=='X' and button_9['text']=='X' or
          button_3['text']=='X' and button_5['text']=='X' and button_7['text']=='X' or
          button_1['text']=='X' and button_2['text']=='X' and button_3['text']=='X' ):
            messagebox.showinfo("Game over","PLayer X won")


    elif (button_1['text']=='O' and button_2['text']=='O' and button_3['text']=='O' or
          button_4['text']=='O' and button_5['text']=='O' and button_6['text']=='O' or
          button_7['text']=='O' and button_8['text']=='O' and button_9['text']=='O' or
          button_1['text']=='O' and button_4['text']=='O' and button_7['text']=='O' or
          button_2['text']=='O' and button_5['text']=='O' and button_8['text']=='O' or
          button_3['text']=='O' and button_6['text']=='O' and button_9['text']=='O' or
          button_1['text']=='O' and button_5['text']=='O' and button_9['text']=='O' or
          button_3['text']=='O' and button_5['text']=='O' and button_7['text']=='O' or
          button_1['text']=='O' and button_2['text']=='O' and button_3['text']=='O' ):
            messagebox.showinfo("Game over","PLayer O won")


    else:
            messagebox.showwarning('Warning','None of you can play'  )

root = Tk()
root.title("Tic-Tac-Toe")
root.geometry("426x450")


button_1 = Button(root, text=" ", width=10, height=5,font=("Arial Bold",15),bg="Grey",fg="White",borderwidth=8,command=lambda : click(button_1))
button_1.grid(column=0, row=0)

button_2 = Button(root, text=" ", width=10, height=5,font=("Arial Bold",15),bg="Grey",fg="White",borderwidth=8,command=lambda : click(button_2))
button_2.grid(column=1, row=0)

button_3 = Button(root, text=" ", width=10, height=5,font=("Arial Bold",15),bg="Grey",fg="White",borderwidth=8,command=lambda : click(button_3))
button_3.grid(column=2, row=0)

button_4 = Button(root, text=" ", width=10, height=5,font=("Arial Bold",15),bg="Grey",fg="White",borderwidth=8,command=lambda : click(button_4))
button_4.grid(column=0, row=1)

button_5 = Button(root, text=" ", width=10, height=5,font=("Arial Bold",15),bg="Grey",fg="White",borderwidth=8,command=lambda : click(button_5))
button_5.grid(column=1, row=1)

button_6 = Button(root, text=" ", width=10, height=5,font=("Arial Bold",15),bg="Grey",fg="White",borderwidth=8,command=lambda : click(button_6))
button_6.grid(column=2, row=1)

button_7 = Button(root, text=" ", width=10, height=5,font=("Arial Bold",15),bg="Grey",fg="White",borderwidth=8,command=lambda : click(button_7))
button_7.grid(column=0, row=3)

button_8 = Button(root, text=" ", width=10, height=5,font=("Arial Bold",15),bg="Grey",fg="White",borderwidth=8,command=lambda : click(button_8))
button_8.grid(column=1, row=3)

button_9 = Button(root, text=" ", width=10, height=5,font=("Arial Bold",15),bg="Grey",fg="White",borderwidth=8,command=lambda : click(button_9))
button_9.grid(column=2, row=3)


root.mainloop()
