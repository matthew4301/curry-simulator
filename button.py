"""Button class."""

import pyglet


class Button(pyglet.sprite.Sprite):
    """Button class."""

    def __init__(self, x, y, scale, text="Button", text_size=30):
        """Creates a button sprite and a text label inside of it.

        Arguments:
            x {int} -- the x pos of the button
            y {int} -- the y pos of the button
            scale {float} -- the scale of the button and label

        Keyword Arguments:
            text {str} -- the text to be displayed on the button (default: {"Button"})
            text_size {int} -- the size of the text to be displayed (default: {30})
        """
        image = pyglet.image.load("resources/button.png")
        image.anchor_x, image.anchor_y = image.width//2, image.height//2
        super().__init__(image, x=x, y=y)
        self.scale = scale

        self.label = pyglet.text.Label(
            text,
            font_name="Comic Sans MS",
            font_size=text_size*scale,
            x=self.x + 20*scale - self.width // 2, y=self.y + 20*scale,
            width=self.width - 20*scale,
            multiline=True,
            anchor_y="center"
        )

    def draw(self):
        """Draws the button."""
        super().draw()
        self.label.draw()

    def inButton(self, x, y):
        """Checks if a given x and y value is inside the borders of the button.

        Arguments:
            x {int} -- X value of check
            y {int} -- Y value of check

        Returns:
            boolean -- Are the coordinates within the button's borders
        """
        return (
            self.x < x and
            x < self.x+self.width*self.scale and
            self.y < y and
            y < self.y+self.height*self.scale
        )
