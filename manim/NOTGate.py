from manim import *  # type: ignore

bits = [[0, -2.5, 0], [0, 2.5, 0]]

class NOTGate(Scene):
    def construct(self):
        t0 = Table(
            [["1", "0"],
            ["0", "1"]],
            col_labels=[Text("Input 1").set_color(BLUE), Text("Output").set_color(ORANGE)]  # type: ignore
        )
        
        gate = Text("NOT Gate")
        g = Group(gate, t0).arrange_in_grid(2,1,row_heights=[2.25,2.25]).shift(LEFT * 3.5).scale(0.7)

        triangle = Triangle().set_color(WHITE).scale(1.2).center().set_stroke(width=10) # type: ignore
        circle = Circle(1).set_color(WHITE).scale(0.15) # type: ignore
        not_gate = Group(triangle, circle).arrange_in_grid(2,1, row_heights=[-2.8,0])

        dot0, dot1, dot2, dot3 = Dot([0, -1.06, 0]), Dot(bits[0]), Dot([0, 1.1, 0]), Dot(bits[1])  # type: ignore
        g0 = Group(dot1, dot3)
        l0, l1 = Line(dot1.get_center(), dot0.get_center()), Line(dot2.get_center(), dot3.get_center())
        g1 = Group(l0, l1)
        g2 = Group(g0, g1, not_gate).shift(RIGHT * 3)
        
        text0, text1 = Text("I").move_to(dot1).shift(DOWN * 0.5), Text("O").move_to(dot3).shift(UP * 0.5)
        g4 = Group(text0, text1)
        g3 = Group(g, g2, g4)
        self.add(g3)

        a0 = Arrow(start=RIGHT, end=LEFT, color=WHITE).shift(DOWN * 0.3, LEFT * 0.1)
        a0.generate_target()
        self.play(FadeIn(a0))

        dots = [Dot(bits[i]).set_color(GOLD) for i in range(2)]  # type: ignore
        self.play(MoveAlongPath(dots[0], l0), rate_func=linear)
        self.play(FadeOut(dots[0]))
        a0.target.shift(DOWN * 0.9)  # type: ignore
        self.play(MoveToTarget(a0))
        self.wait(0.6)
        self.play(MoveAlongPath(dots[1], l1))
        self.play(FadeOut(dots[1]))
        self.wait(1)
