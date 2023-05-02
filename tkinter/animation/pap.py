import random

from tkinter import *
w = 700
h = 700
x_current = 0
y_current = 0
x_prev = 0
y_prev = 0

#     a, b, c, d, e, f = 0, 0, 0, 0.25, 0, -0.4
#     a, b, c, d, e, f = 0.95, 0.005, -0.005, 0.93, -0.002, 0.5
#     a, b, c, d, e, f = 0.035, -0.2, 0.16, 0.04, -0.09, 0.02
#     a, b, c, d, e, f = -0.04, 0.2, 0.16, 0.04, 0.083, 0.12

def paintdot():
    global x_current, y_current, x_prev, y_prev, w, h
    point = random.random()
    if point < 0.01:
        a, b, c, d, e, f = 0, 0, 0, 0.16, 0, 0
    elif point < 0.86:
        a, b, c, d, e, f = 0.85, 0.04, -0.04, 0.85, 0, 1.6
    elif point < 0.93:
        a, b, c, d, e, f = 0.2, -0.26, 0.23, 0.22, 0, 1.6
    else:
        a, b, c, d, e, f = -0.15, 0.28, 0.26, 0.24, 0, 0.44

    x_current = (a * x_prev) + (b * y_prev) + e
    y_current = (c * x_prev) + (d * y_prev) + f
    x_prev = x_current
    y_prev = y_current
    canvas.create_oval(w * (x_current + 3) / 6, h - h * ((y_current + 2) / 14), w * (x_current + 3) / 6, h - h * ((y_current + 2) / 14), width=1, outline='white')
    # canvas.create_oval(50 * (x_current + 7), 50 * (12 - y_current), 50 * (x_current + 7), 50 * (12 - y_current), width=1, outline='white')
    root.after(1, paintdot)


root = Tk()

canvas = Canvas(root, width=w, height=h, bg='black')
canvas.pack()

paintdot()

root.mainloop()