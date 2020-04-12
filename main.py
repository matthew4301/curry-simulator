"""objects that ive shoved up my arse"""
import pyglet
from pyglet.sprite import Sprite
from pyglet import media

from button import Button


class Window(pyglet.window.Window):
    """Custom Window class."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.player = media.Player()
        self.music = media.load("resources/curry_music.wav")
        self.player.queue(self.music)

        self.bg_img = pyglet.resource.image("resources/curry.jpg")
        self.bg_img.anchor_x = self.bg_img.width // 2
        self.bg = pyglet.sprite.Sprite(
            self.bg_img,
            self.width//2, 0
        )
        self.bg.scale = self.scale_factor

        self.start_button = Button(
            self.width // 2,
            self.height // 2 - 200,
            self.scale_factor,
            text="start",
            text_size=140
        )

        self.title = pyglet.text.Label(
            "curry simulator 2020",
            font_name="Comic Sans MS",
            font_size=80,
            x=self.width // 2, y=self.height // 2,
            anchor_x="center", anchor_y="center"
        )

    def on_show(self):
        self.player.play()
        return super().on_show()

    def on_draw(self):
        self.clear()
        self.bg.draw()
        self.title.draw()
        self.start_button.draw()
        return super().on_draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if (
            start_button.inButton(x, y) and
            button == pyglet.window.mouse.LEFT
        ):
            print("Clicked!")
        return super().on_mouse_press(x, y, button, modifiers)

    @property
    def scale_factor(self):
        return self.height / self.bg.height


if __name__ == "__main__":
    window = Window(fullscreen=True)
    pyglet.app.run()
