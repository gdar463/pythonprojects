from manim import *  # type: ignore

bits = [[-0.5, -2.5, 0], [0.5, -2.5, 0], [0, 2.5, 0]]

class ANDGate(Scene):
    def construct(self):
        t0 = Table(
            [["1", "1", "1"],
            ["1", "0", "0"],
            ["0", "1", "0"],
            ["0", "0", "0"],],
            col_labels=[Text("Input 1").set_color(BLUE), Text("Input 2").set_color(BLUE), Text("Output").set_color(ORANGE)]  # type: ignore
        )
        
        gate = Text("AND Gate")
        g = Group(gate, t0).arrange_in_grid(2,1,row_heights=[3.5,3.5]).shift(LEFT * 4).scale(0.5)

        arc_conf = {"stroke_width": 7}
        a, b, c = [-1, 0, 0], [1, 0, 0], [0, np.sqrt(3), 0]
        dots = [Dot(a, 0.035), Dot(b, 0.035), Dot(c, 0.04)]
        arc0, arc1 = ArcBetweenPoints(b, c, radius=2, **arc_conf), ArcBetweenPoints(c, a, radius=2, **arc_conf)
        line = Line(dots[0].get_center(), dots[1].get_center()).set_stroke(width=7)
        dots = Group(*dots)
        and_gate = Group(arc0, arc1, line, dots).center()

        dot0, dot1, dot2, dot3, dot4, dot5 = Dot([-0.5, -0.7, 0]), Dot(bits[0]), Dot([0.5, -0.7, 0]), Dot(bits[1]), Dot([0, 0.9, 0]), Dot(bits[2])
        g0 = Group(dot1, dot3, dot5)
        l0, l1, l2 = Line(dot1.get_center(), dot0.get_center()), Line(dot3.get_center(), dot2.get_center()), Line(dot4.get_center(), dot5.get_center())
        g1 = Group(l0, l1, l2)
        g2 = Group(g0, g1, and_gate).shift(RIGHT * 3)
        
        text0, text1, text2 = Text("I1").move_to(dot1).shift(DOWN * 0.5), Text("I2").move_to(dot3).shift(DOWN * 0.5), Text("O").move_to(dot5).shift(UP * 0.5)
        g4 = Group(text0, text1, text2)
        g3 = Group(g, g2, g4)
        self.add(g3)

        a0 = Arrow(start=RIGHT, end=LEFT, color=WHITE).shift(UP * 0.45, LEFT * 0.3)
        a0.generate_target()
        self.play(FadeIn(a0))

        dots = [Dot(bits[i]).set_color(GOLD) for i in range(3)]  # type: ignore
        for i in range(3):
            anim, fade = [], []
            if i < 2:
                anim.append(MoveAlongPath(dots[0], l0))
                fade.append(FadeOut(dots[0]))
            if i % 2 == 0:
                anim.append(MoveAlongPath(dots[1], l1))
                fade.append(FadeOut(dots[1]))
            self.play(*anim, rate_func=linear)
            self.play(*fade)
            if i == 0:
                self.play(MoveAlongPath(dots[2], l2))
                self.play(FadeOut(dots[2]))
            a0.target.shift(DOWN * 0.65)  # type: ignore
            self.play(MoveToTarget(a0))
            self.wait(0.4)
            anim.clear()
            fade.clear()
        self.wait(0.6)
