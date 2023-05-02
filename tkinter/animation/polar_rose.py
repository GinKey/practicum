import tkinter as tk
import math


class PolarRose(tk.Canvas):
    def __init__(self, root, width=600, height=600, n=2, d=3, size=200):
        super().__init__(root, width=width, height=height, bg='white')
        self.n = n
        self.d = d
        self.size = size

        # Создаем слайдеры для изменения параметров
        n_slider = tk.Scale(from_=1, to=11, orient=tk.HORIZONTAL, label="n", length=150, command=self.set_n)
        n_slider.place(x=290, y=0)
        n_slider.set(n)

        d_slider = tk.Scale(from_=1, to=11, orient=tk.HORIZONTAL, label="d", length=150, command=self.set_d)
        d_slider.pack(anchor="ne")
        d_slider.set(d)

        # Рисуем первую розу
        self.draw_rose()


    def set_n(self, n):
        self.n = int(n)
        self.draw_rose()

    def set_d(self, d):
        self.d = int(d)
        self.draw_rose()

    def draw_rose(self):

        self.delete("all")
        x = self.winfo_width() / 2
        y = self.winfo_height() / 2

        angel = 0

        # Спираль Архимеда
        # r = self.d + self.n * math.radians(angel)

        # Рисовать линией
        r = self.size * math.cos(math.radians(self.n * 0) / self.d)

        x2 = x + r * math.cos(math.radians(0))
        y2 = y - r * math.sin(math.radians(0))
        prev_x, prev_y = x2, y2

        for angel in range(3600):

            # Полярная роза
            r = self.size * math.cos(math.radians((self.n * angel) / self.d))

            # Спираль Архимеда
            # r = self.d + self.n * math.radians(angel)

            # Кривая Лиссажу
            # x2 = x + self.size * math.cos(self.n * math.radians(angel))
            # y2 = y - self.size * math.sin(self.d * math.radians(angel))


            x2 = x + r * math.cos(math.radians(angel))
            y2 = y - r * math.sin(math.radians(angel))



            # Рисовать точками
            # self.create_oval(x2-2, y2-2, x2+2, y2+2, fill='black', width=0)

            # Рисовать линией
            self.create_line(prev_x, prev_y, x2, y2, fill="black")
            prev_x, prev_y = x2, y2


root = tk.Tk()
rose = PolarRose(root)
rose.pack()
root.mainloop()
