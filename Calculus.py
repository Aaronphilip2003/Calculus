import sympy as smp
from tkinter import *
x=smp.symbols('x')
# print(smp.limit(smp.sin(x/2)+smp.sin(x),x,smp.pi))
# print(smp.diff(smp.sin(x),x))

#GUI ADJUSTMENTS
root=Tk()
root.geometry("500x500")

#Entry
e1=Entry(root,borderwidth=10, width=50)
e2=Entry(root,borderwidth=10, width=50)
e1.grid(column=0, row=0, columnspan=3, padx=80, pady=10)
e2.grid(column=0, row=1, columnspan=3, padx=80, pady=10)


#Button Functions
def sinx():
    sin=smp.sin(x)
    e1.insert(0,sin)







button_sinx=Button(root,text='sin(x)',padx=15, pady=15, borderwidth=3,command=sinx)
button_sinx.place(x=80,y=120)

root.mainloop()