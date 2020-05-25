import pyglet
from pyglet.window import key
from pyglet.window import FPSDisplay
from pyglet import media
from random import randint, choice

in_menu = True
not_menu = False

window = pyglet.window.Window(caption="Curry Simulator 2020", width = 1367, height = 768, fullscreen = False)
window.set_location(400, 100)
image = pyglet.resource.image('resources/curry.jpg')
icon = pyglet.image.load('resources/icon.png')
window.set_icon(icon)
fps_display = FPSDisplay(window)
fps_display.label.font_size = 50
label = pyglet.text.Label(
    "curry simulator 2020",
    font_name="Comic Sans MS",
    font_size=80,
    x=window.width // 2, y=700,
    anchor_x="center", anchor_y="center"
)
label3 = pyglet.text.Label(
    "eat all the curry quickly",
    font_name="Comic Sans MS",
    font_size=80,
    x=window.width // 2, y=window.width // 2,
    anchor_x="center", anchor_y="center"
)
label2 = pyglet.text.Label(
    "press enter to start",
    font_name="Comic Sans MS",
    font_size=40,
    x=window.width // 2, y=100,
    anchor_x="center", anchor_y="center"
)


music = pyglet.resource.media('resources/music.mp3')
music.play()

@window.event
def on_draw():
    window.clear()
    fps_display.draw()
    if in_menu:
        label.draw()
        label2.draw()
        image.blit(350, 150)

@window.event
def on_key_press(button, modifiers):
    global in_menu
    if button == key.ENTER and in_menu:
        in_menu = False
        not_menu = True
        window.clear()
        label3.draw()

pyglet.app.run()