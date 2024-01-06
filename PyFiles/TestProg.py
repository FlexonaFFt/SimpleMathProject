from manim import *

class CylinderExample(Scene):
    def construct(self):
        # Создание цилиндра
        cylinder = Cylinder(radius=1, height=2, fill_color='#6c584c', stroke_color=ORANGE, stroke_width=4)

        # Добавление цилиндра на сцену
        self.play(Create(cylinder))

        # Добавление подписей
        radius_label = MathTex("r", color=ORANGE).next_to(cylinder, DOWN)
        height_label = MathTex("h", color=ORANGE).shift(2*UP)
        self.play(Write(radius_label), Write(height_label))

        self.wait(1)
