import tkinter as tk
import time
import numpy as np
from PIL import Image,ImageTk

np.random.seed(1)
photo_image = ImageTk.PhotoImage
unit = 100
height = 5
width = 5

#创建一个class继承tk.TK
class Env(tk.Tk):
    def __init__(self):
        super(Env,self).__init__()
        self.action_space = ['u','d','r','l']
#action数目
        self.n_actions = len(self.action_space)
        self.title('Monte carlo')
#几何形状
        self.geometry('{0}x{1}'.format(height*unit, width*unit))
        self.shapes = self.load_images()
        self.canvas = self._build_canvas()
        self.texts = []

    def _build_canvas(self):
#创建画布，背景为白色，高，宽
        canvas = tk.Canvas(self, bg='white', height = height*unit, width = width*unit)
#绘制方格线条
        for c in range(0, width*unit, unit):
            x0, y0, x1, y1 = c, 0, c, height*unit
            canvas.create_line(x0, y0, x1, y1)
        for r in range(0, height*unit, unit):
            x0, y0, x1, y1 = 0, r, height*unit, r
            canvas.create_line(x0, y0, x1, y1)
#给定形状，三角形是炸弹，圆形是宝藏
        self.square = canvas.create_image(50, 50, image=self.shapes[0])
        self.triangle1 = canvas.create_image(250, 150, image=self.shapes[1])
        self.triangle2 = canvas.create_image(150, 250, image=self.shapes[1])
        self.circle = canvas.create_image(250, 250, image=self.shapes[2])
        canvas.pack()
        return canvas

#给定形状
    def load_images(self):
        square = photo_image(Image.open('E:/materials/square.jpg').resize((65, 65)))
        triangle = photo_image(Image.open('E:/materials/triangle.jpg').resize((65, 65)))
        circle = photo_image(Image.open('E:/materials/circle.jpg').resize((65, 65)))
        return square, triangle, circle

    @staticmethod
    def coord_to_states(coords):
        x = int((coords[0]-50)/100)
        y = int((coords[1]-50)/100)
        return [x,y]

#重置游戏
    def reset(self):
        self.update()
        time.sleep(0.5)
        x, y = self.canvas.coords(self.square)
        self.canvas.move(self.square,unit/2-x, unit/2-y)
        return self.coord_to_states(self.canvas.coords(self.square))

    def step(self, action):
        state = self.canvas.coords(self.square)
#基准动作
        base_action = np.array([0, 0])
        self.render()
#上u
        if action == 0:
            if state[1] > unit:
                base_action[1] -= unit
#下d
        elif action == 1:
            if state[1] < (height-1)*unit:
                base_action[1] += unit
#右r
        elif action == 2:
            if state[0] < (width-1)*unit:
                base_action[0] += unit
#左l
        elif action == 3:
            if state[0] > unit:
                base_action[0] -= unit
#移动到base_action的位置
        self.canvas.move(self.square, base_action[0], base_action[1])
        self.canvas.tag_raise(self.square)
#取得下一个state
        next_state = self.canvas.coords(self.square)
#奖励机制，如果是圆圈，宝藏+100，如果是炸弹-100
        if next_state == self.canvas.coords(self.circle):
            reward = 100
            done = True
        elif next_state in [self.canvas.coords(self.triangle1),self.canvas.coords(self.triangle2)]:
            reward = -100
            done = True
        else:
            reward = 0
            done = False
        next_state = self.coord_to_states(next_state)

        return next_state, reward, done

    def render(self):
        time.sleep(0.5)
        self.update()
