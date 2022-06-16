from tkinter import *

window = Tk()

window.title('CALCULATOR')
window.geometry('320x550')
window.configure(bg='#4c6954')
window.resizable(0,0)

val=""
vals=0
operator=""

def clicked(item):
    global val
    val=val+str(item)
    data.set(val)
def clicked_clear():
    global val
    val = ""
    data.set(val)
def clicked_del():
    global val
    val =val[:-1]
    data.set(val)
def clicked_divide():
    global val
    global vls
    global operator
    if val.find("-") >= 0 or val.find("+") >= 0 or val.find("*") >= 0 or val.find("/") >= 0 or val.find("%"):
       clicked_equals()
    vls = float(val)
    operator = "/"

    val = val + "/"
    data.set(val)
def clicked_mult():
    global val
    global vls
    global operator
    if val.find("-") >= 0 or val.find("+") >= 0 or val.find("*") >= 0 or val.find("/") >= 0 or val.find("%"):
         clicked_equals()
    vls = float(val)
    operator = "*"
    val = val + "*"
    data.set(val)
def clicked_minus():
    global val
    global vls
    global operator
    if val.find("-") >= 0 or val.find("+") >= 0 or val.find("*") >= 0 or val.find("/") >= 0 or val.find("%"):
       clicked_equals()
    vls = float(val)
    operator = "-"
    val = val + "-"
    data.set(val)
def clicked_mod():
    global val
    global vls
    global operator
    if val.find("-") >= 0 or val.find("+") >= 0 or val.find("*") >= 0 or val.find("/") >= 0 or val.find("%"):
       clicked_equals()
    vls = float(val)
    operator = "%"
    val = val + "%"
    data.set(val)

def clicked_plus():
    global val
    global vls
    global operator
    if val.find("-") >= 0 or val.find("+") >= 0 or val.find("*") >= 0 or val.find("/") >= 0 or val.find("%"):
       clicked_equals()
    vls = float(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def clicked_equals():
    global val
    global vals
    global operator

    if operator == "+":
        result= str(eval(val))
        data.set(result)
        val = str(result)
    elif operator == "-":
        result= str(eval(val))
        data.set(result)
        val = str(result)
    elif operator == "*":
        result = str(eval(val))
        data.set(result)
        val = str(result)
    elif operator == "%":
        result = str(eval(val))
        data.set(result)
        val = str(result)
    elif operator == "/":
        try:
            total = str(eval(val))
        except:
            ZeroDivisionError
        val = "Sorry, Division By Zero Is Not Possible!!!"
        data.set(val)
        data.set(total)
        val = str(total)



item=StringVar()
data = StringVar()
lbl = Label(window, wraplength=300, justify=RIGHT,text="",textvariable=data, anchor=SE, font=("Verdana", 20), height=3, bg="white", fg="black")
lbl.pack(expand=True, fill="both")


btns_frame = Frame(window, width=200, height=250, bg="grey")
btns_frame.pack()

btn_clr = Button(btns_frame, text="clear", width=10, height=5, command=lambda :clicked_clear())
btn_clr.grid(row=1, column=0, columnspan=2, sticky="WE")
btn_divide = Button(btns_frame, text="/", width=10, height=5,command=lambda :clicked_divide())
btn_divide.grid(row=1, column=2)
btn_mult = Button(btns_frame, text="*", width=10, height=5,command=lambda :clicked_mult())
btn_mult.grid(row=1, column=3)

button7 = Button(btns_frame, text="7", width=10, height=5, command=lambda: clicked(7))
button7.grid(row=2, column=0)
button8 = Button(btns_frame, text="8", width=10, height=5, command=lambda: clicked(8))
button8.grid(row=2, column=1)
button9 = Button(btns_frame, text="9", width=10, height=5, command=lambda: clicked(9))
button9.grid(row=2, column=2)
button_minus = Button(btns_frame, text="-", width=10, height=5, command=lambda :clicked_minus())
button_minus.grid(row=2, column=3)

button4 = Button(btns_frame, text="4", width=10, height=5, command=lambda: clicked(4))
button4.grid(row=3, column=0)
button5 = Button(btns_frame, text="5", width=10, height=5, command=lambda: clicked(5))
button5.grid(row=3, column=1)
button6 = Button(btns_frame, text="6", width=10, height=5, command=lambda: clicked(6))
button6.grid(row=3, column=2)
button_mod = Button(btns_frame, text="%", width=10, height=5,command=lambda :clicked_mod())
button_mod.grid(row=3, column=3)

button1 = Button(btns_frame, text="1", width=10, height=5, command=lambda: clicked(1))
button1.grid(row=4, column=0)
button2 = Button(btns_frame, text="2", width=10, height=5, command=lambda: clicked(2))
button2.grid(row=4, column=1)
button3 = Button(btns_frame, text="3", width=10, height=5, command=lambda: clicked(3))
button3.grid(row=4, column=2)
button_plus = Button(btns_frame, text="+", width=10, height=5,command=lambda: clicked_plus())
button_plus.grid(row=4, column=3)

button_dot = Button(btns_frame, text=".", width=10, height=5, command=lambda: clicked("."))
button_dot.grid(row=5, column=0)
button0 = Button(btns_frame, text="0", width=10, height=5, command=lambda: clicked(0))
button0.grid(row=5, column=1)
button_del = Button(btns_frame, text="del", width=10, height=5,command=lambda :clicked_del())
button_del.grid(row=5, column=2)
button_equals = Button(btns_frame, text="=", width=10, height=5, command=lambda :clicked_equals())
button_equals.grid(row=5, column=3)

window.mainloop()
