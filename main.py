'''objects that ive shoved up my arse'''
import pyglet
from pyglet.sprite import Sprite
from pyglet import media

from button import Button

player = media.Player()
source = media.load('curry_music.wav')
player.queue(source)

window = pyglet.window.Window(fullscreen = True);

image = pyglet.resource.image('curry.jpg')
SCALE_FACTOR = window.height / image.height
image.anchor_x = image.width // 2
curry_sprite = Sprite(
    image,
    x=window.width//2, y=0
)
curry_sprite.scale = SCALE_FACTOR

start_button = Button(
    window.width // 2,
    window.height // 2 - 200,
    SCALE_FACTOR*1.5,
    text="start",
    text_size=140
)

label = pyglet.text.Label(
    'curry simulator 2020',
    font_name='Comic Sans MS',
    font_size=80,
    x=window.width // 2, y = window.height // 2,
    anchor_x="center", anchor_y="center"
)

@window.event
def on_show():
    player.play()

@window.event
def on_draw():
    window.clear()
    curry_sprite.draw()
    label.draw()
    start_button.draw()

@window.event
def on_mouse_press(x, y, mb, modifiers):
    if (start_button.inButton(x, y) and
        mb == pyglet.window.mouse.LEFT):
        print("Clicked!")

pyglet.app.run()