"""
manim -pql windmill.py Windmill
"""

from manim import *
import math

class Windmill(Scene):
    def construct(self):
        bg = ImageMobject("background.jpg")
        self.add(bg)
        self.bring_to_back(bg)

        #ax = Axes(x_length=10, y_length=10)
        #self.add(ax)

        windmill = VGroup()
        center = windmill.get_center()

        whee = Circle(radius=3.1, arc_center=center)
        whee.set_fill(PINK, opacity=0.1)
        windmill.add(whee)
        
        for i in range(3):
            angle = i*2*PI/3
            bar = Line((0, 0, 0), (math.cos(angle+PI/6)*3, math.sin(angle+PI/6)*3, 0))
            bar.set_fill(BLACK)
            windmill.add(bar)
            leaf = Sector(arc_center=center, outer_radius=3, inner_radius=0.5, angle=PI/6, start_angle=angle+PI/12)
            leaf.set_fill(YELLOW, opacity=1.0)
            windmill.add(leaf)

        dot = Dot()
        dot.set_fill(BLACK)
        windmill.add(dot)

        windmill.move_to(LEFT)

        self.play(Rotate(windmill), run_time=5, rate_func=rush_into)
        for i in range(10):
            self.play(Rotate(windmill), run_time=1, rate_func=linear)
