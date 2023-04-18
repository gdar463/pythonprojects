from manim import *  # type: ignore

class Bitmap(Scene):
    def construct(self):
        realbg = Rectangle(width=14.5, height=8, color="#808080", fill_color="#808080", fill_opacity=1).center() # type: ignore
        self.add(realbg)
        bg = Rectangle(width=8, height=7, color=WHITE, fill_color=WHITE, fill_opacity=1).center() # type: ignore
        dots = Group()
        for x in range(-4, 4):
            for y in range(-3, 4):
                dots.add(Dot(np.array([x + 0.5, y, 0]), color=RED, fill_opacity=0))
        f = open("image.txt", "r")
        file = f.read().splitlines()
        f.close()
        rectangles = Group()
        for x in range(len(file)):
            xlist = file[x].split(" ")
            for y in range(len(xlist)):
                if xlist[y] == "1":
                    rectangles.add(Rectangle(width=1, height=1, color=BLACK, fill_color=BLACK, fill_opacity=1).move_to(np.array([x - 3, y - 3.5, 0]))) # type: ignore
        lines = Group()
        for x in range(-4, 5):
            lines.add(Line(np.array([x, 3.5, 0]), np.array([x, -3.5, 0]), color=RED))
        for y in range(-4, 4):
            lines.add(Line(np.array([-4, y + 0.5, 0]), np.array([4, y + 0.5, 0]), color=RED))
        image = Group(bg, dots, rectangles.rotate_about_origin(-PI/2)).scale(0.8).shift(RIGHT * 3.5)
        squares = Group(Square(side_length=0.0001, color=RED, fill_color=RED, fill_opacity=1).move_to(np.array([-4, 3.5, 0])), Square(side_length=0.0001, color=RED, fill_color=RED, fill_opacity=1).move_to(np.array([-4, -3.5, 0])), Square(side_length=0.0001, color=RED, fill_color=RED, fill_opacity=1).move_to(np.array([4, 3.5, 0])), Square(side_length=0.0001, color=RED, fill_color=RED, fill_opacity=1).move_to(np.array([4, -3.5, 0])))
        self.add(image)
        self.wait(1.5)
        t0 = Text("Questa è un'immagine\n   di dimensioni 8x7", font_size = 30).shift(UP * 2.5, LEFT * 3.4)
        t1 = Text("   Rappresenta una D \n con spessore di 2 punti", font_size = 30).shift(LEFT * 3.4)
        t2 = Text("Ma come viene transformata\n        in un file bitmap?", font_size = 30).shift(DOWN * 2.5, LEFT * 3.4)
        self.play(Write(t0))
        self.wait(2)
        self.play(FadeTransform(t0, t1))
        self.wait(2)
        self.play(FadeTransform(t1, t2))
        self.wait(2)
        self.play(Unwrite(t2))
        t0 = Text("Ecco la sequenza:", font_size = 30)
        t1 = Text("1) Discretizzazione", font_size = 30)
        t2 = Text("2) Quantizzazione", font_size = 30)
        sequence = VGroup(t0, t1, t2).arrange(DOWN, aligned_edge = LEFT).shift(LEFT * 3.4) # type: ignore
        self.play(Write(sequence), lag_ratio = 0.5)
        self.wait(2.5)
        self.play(Unwrite(t0), Unwrite(t2))
        t1.generate_target()
        t1.target.scale(1.4).shift(UP * 3.3) # type: ignore
        self.play(MoveToTarget(t1))
        self.wait(1)
        # image.generate_target()
        # image.target.shift(LEFT * 7) # type: ignore
        # self.play(MoveToTarget(image))
        t3 = Text(" In questo passaggio\n bisogna dividere l'immagine\n in una griglia di dimensioni che vogliamo\n (in questo caso sempre 8x7)", font_size = 24)
        t4 = Text("Poi si puo' passare alla quantizzazione", font_size = 24)
        sequence = VGroup(t3, t4).arrange(DOWN, aligned_edge = LEFT).shift(LEFT * 3.4) # type: ignore
        self.play(Write(t3))
        self.wait(2)
        self.play(FadeIn(lines.scale(0.8).shift(RIGHT * 3.5)), FadeIn(squares.scale(0.8).shift(RIGHT * 3.5)))
        image.add(lines, squares)
        self.wait(1)
        self.play(Write(t4))
        self.wait(2)
        t2 = Text("2) Quantizzazione", font_size = 30).scale(1.4)
        t2.move_to(t1)
        self.play(Unwrite(t3), Unwrite(t4))
        self.wait(0.5)
        self.play(FadeTransform(t1, t2))
        self.wait(1)
        t3 = Text("In questo passaggio\nbisogna considerare ogni pixel\ne assegnargli un valore\nche rappresenti la sua intensità", font_size = 24)
        t4 = Text("In questo caso\ni valori sono 0 o 1", font_size = 24)
        t5 = Text("Di conseguenza\nsi può rappresentare una seconda immagine\ncomposta solo da 0 o 1", font_size = 24)
        sequence = VGroup(t3, t4, t5).arrange(DOWN, aligned_edge = LEFT).shift(UP * 0.5, LEFT * 3.2) # type: ignore
        self.play(Write(t3))
        self.wait(2)
        pixel = rectangles[0].copy()
        pixel.generate_target()
        pixel.target.scale(1.25).shift(DOWN * 5.5, LEFT * 6) # type: ignore
        self.play(MoveToTarget(pixel))
        self.wait(1)
        num = Text("1", font_size = 30, color = BLACK).scale(1.25).shift(DOWN * 3, LEFT * 2.5).set_y(pixel.get_y()) # type: ignore
        newpixel = pixel.copy()
        numbg = Square(side_length = 1, color = WHITE, fill_color = WHITE, fill_opacity = 1).shift(DOWN * 3, LEFT * 2.5).set_y(pixel.get_y())
        self.play(Write(t4))
        self.wait(2)
        self.play(FadeIn(numbg))
        self.play(FadeTransform(newpixel, num))
        self.wait(1)
        self.play(Write(t5))
        image.generate_target()
        image.target.scale(0.5).center().shift(UP * 1.5, RIGHT * 3.5) # type: ignore
        self.play(MoveToTarget(image))
        self.wait(0.5)
        pixels = VGroup(*[Text(str(file[x]).replace(" ", "     "), font_size = 16, color = BLACK) for x in range(len(file))]).arrange(DOWN, aligned_edge = LEFT) # type: ignore
        pixelsbg = Rectangle(width=8, height=7, color=WHITE, fill_color=WHITE, fill_opacity=1).scale(0.8).scale(0.5) # type: ignore
        newimage = Group(pixelsbg, pixels)
        images = Group(image, newimage).arrange(DOWN, aligned_edge = LEFT).shift(RIGHT * 3.5) # type: ignore
        self.play(FadeIn(newimage))
        self.wait(5)