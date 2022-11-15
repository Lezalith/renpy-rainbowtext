init -10 python:
    class RainbowText(renpy.Displayable):

        # Range of the hue, by default (0.0, 1.0). Same across all RainbowTexts.
        # Can be changed, but skips colors in the missing range. 
        MIN_HUE = 0.0 # Correlates to 0.0
        MAX_HUE = 1.0 # Correlates to 360.0

        # Color of the text is created from HLS - (Hue, Lightness, Saturation).
        # Hue has the range (0.0. 360.0), and both Lightness and Saturation (0.0, 100.0),
        # both of which the code converts to (0.0, 1.0) behind the scenes.
        #
        # interval is the hue value added on every render. Determines speed of the color changes.
        # start is the starting hue, default of None refers to MIN_HUE.
        # l is lightness used when creating the color.
        # s is saturation used when creating the color.
        def __init__(self, text, interval = 0.5, start = None, l = 50.0, s = 100.0, **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(RainbowText, self).__init__(**kwargs)

            # Text displayed.
            self.base_text = text
            # How fast hue gets incremented.
            self.interval = float(interval / 360)

            # Starting hue of the text. Recorded for reset().
            self.hue_starting = (self.MIN_HUE if start is None else float(start / 360))
            # Actual hue of the text.
            self.hue = self.hue_starting

            # Lightness and saturation of the colors.
            self.lightness = float(l / 100)
            self.saturation = float(s / 100)

            # Currently shown child.
            self.child = Null()

            # Whether the color change has been paused.
            self.paused = False 

        # Returns a render containing our Text displayable.
        def render(self, width, height, st, at):

            # Make sure this function runs again asap.
            renpy.redraw(self, 0)

            # Generate a new color and child, unless it's paused.
            if self.paused is False:

                # Set new hue. First add self.interval:
                self.hue = self.hue + self.interval 
                # Before looping it back in case it crossed the maximum.
                self.hue = (self.hue if (self.hue <= self.MAX_HUE) else self.hue - self.MAX_HUE)

                # Generate a new color with current hue and defined lightness and saturation.
                color = Color(hls = (self.hue, self.lightness, self.saturation))

                # New child.
                self.child = Text(self.base_text, color = color)

            # Child render, to get the size of this displayable.
            child_render = renpy.render(self.child, width, height, st, at)
            w, h = child_render.get_size()

            # Create the render we will return, with the gotten size.
            render = renpy.Render(w, h)

            # Place the child into the prepared render.
            render.place(self.child)

            # Return the render.
            return render

        # Default CDD methods:
        def event(self, ev, x, y, st):
            return self.child.event(ev, x, y, st)
        def visit(self):
            return [ self.child ]

        # Simple control methods.
        def pause(self):
            self.paused = True
        def unpause(self):
            self.paused = False
        def reset(self):
            self.hue = self.hue_starting
