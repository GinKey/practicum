import math
from tkinter import *

root = Tk()
w = 600
h = 600
r_ball = 200
r = 200
x_center = w//2
y_center = h//2
root.geometry(f'{w}x{h}+{x_center}+{y_center}')
root.title("Главное меню")
c = Canvas(root, width=w, height=h, bg='white')
c.pack()
ball = c.create_oval(x_center-r_ball, y_center+r_ball, x_center+r_ball, y_center-r_ball, fill='blue')


angle = 5
x1 = x_center + r * math.cos(angle)
y1 = y_center + r * math.sin(angle)
ball1 = c.create_oval(x1 - 10, y1 + 10, x1 + 10, y1 - 10, fill='black')
def moveBall():
    global x1, y1, angle
    angle += math.radians(0.5)
    x2 = x_center + r * math.cos(angle)
    y2 = y_center + r * math.sin(angle)
    c.move(ball1, x2 - x1, y2 - y1)
    x1, y1 = x2, y2
    root.after(10, moveBall)

moveBall()

root.mainloop()
