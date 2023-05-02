import tkinter

def calculate(value):
    global f
    if 'error' in f:
        f = value
    elif value == "C":
        f = '0'
    elif value == "=":
        try:
            f = str(eval(f))
        except:
            f = 'error'
    else:
        if f == "0":
            f = ''
        f += value
    lable_text.configure(text=f)

def create_buttons():
    buttons = ['1', '2', '3', '-', '4', '5', '6', '+', '7', '8', '9', '=']
    x = 10
    y = 50
    for button in buttons:
        command = lambda x=button: calculate(x)
        new_button = tkinter.Button(text=button, font=('Arial', 20), command=command)
        new_button.place(x=x, y=y, width=60, height=60)
        x += 65
        if x >= 213:
            x = 10
            y += 70
    new_button = tkinter.Button(text='0', font=('Arial', 20), command=lambda x='0': calculate(x))
    new_button.place(x=x, y=y, width=120, height=60)
    x += 130
    new_button = tkinter.Button(text='C', font=('Arial', 20), command=lambda x='C': calculate(x))
    new_button.place(x=x, y=y, width=120, height=60)


if __name__ == '__main__':
    root = tkinter.Tk()
    root.geometry('270x330')
    root.resizable(False, False)
    root.title("Калькулятор")
    f = "0"
    lable_text = tkinter.Label(text=f, font=('Arial', 20))
    lable_text.place(x=10, y=10)
    create_buttons()
    root.mainloop()