import pyglet
import random
from pyglet.window import key
from pyglet.window import mouse

#设置屏幕大小
game_windom = pyglet.window.Window(1200, 400)
t = 0
label = pyglet.text.Label('Come on Babby', font_name='Time New Roman', font_size=36, x=game_windom.width/2,
                          y=game_windom.height/2, anchor_x='center', anchor_y='center')
#引入背景，头像以及障碍物
image = pyglet.image.load('E:/materials/back.jpg')
image_s = pyglet.image.load('E:/materials/live.gif')
image_fly = pyglet.image.load('E:/materials/fly.jpg')
#产生图像群组
main_batch = pyglet.graphics.Batch()
#设置你的位置
man = pyglet.sprite.Sprite(img=image_s, x=200, y=0)

keys = key.KeyStateHandler()
game_windom.push_handlers(keys)

#生成障碍位置
fly_lives = []
for i in range(10):
    rand_x = random.randrange(0, 1200, 1)
    new_sprite = pyglet.sprite.Sprite(img=image_fly, x=rand_x, y=300)
    new_sprite.scale = 0.1
    fly_lives.append(new_sprite)


def check_bound(self):
    if self.y < 0:
        rand_x = random.randrange(0, 200, 10)
        self.x = self.x+rand_x
        if self.x < 0:
            self.x = 0
        elif self.x > 1200:
            self.x = 1200
        self.y = 400


@game_windom.event
def on_draw():
    game_windom.clear()
    label.draw()
    man.draw()
    for live in fly_lives:
        live.draw()


@game_windom.event
def on_mouse_press(x, y, button):
    if button == mouse.LEFT():
        print('mouse left is passed')
    elif button == mouse.RIGHT:
        print('mouse right is passed')
    print(x)
    print(y)


def update(dt):
    if keys[key.LEFT]:
        man.x -= 10
    if keys[key.RIGHT]:
        man.x += 10
    if keys[key.UP]:
        man.y += 10
    if keys[key.DOWN]:
        man.y -= 10
    if man.y > 400:
        man.y = 400
    if man.y < 0:
        man.y = 0
    if man.x > 1000:
        man.x = 1000
    if man.x < 0 :
        man.x = 0
    for live in fly_lives:
        rand_y = random.randrange(0, 15, 2)
        live.y -= rand_y
        check_bound(live)


pyglet.clock.schedule_interval(update, 1/100.)
pyglet.app.run()
