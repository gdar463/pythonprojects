from manim import *  # type: ignore

bits = [[-0.5, -2.5, 0], [0.5, -2.5, 0], [0, 2.5, 0]]

class XNORGate(Scene):
    def construct(self):
        t0 = Table(
            [["1", "1", "1"],
            ["1", "0", "0"],
            ["0", "1", "0"],
            ["0", "0", "1"],],
            col_labels=[Text("Input 1").set_color(BLUE), Text("Input 2").set_color(BLUE), Text("Output").set_color(ORANGE)]  # type: ignore
        )
        
        gate = Text("XNOR Gate")
        g = Group(gate, t0).arrange_in_grid(2,1,row_heights=[3.5,3.5]).shift(LEFT * 4).scale(0.5)

        arc_conf = {"stroke_width": 0}
        arc_confi = {"stroke_width": 10, "color": WHITE}
        poly_conf = {"stroke_width": 10, "stroke_color": WHITE, "fill_opacity": 0, "color": BLACK}
        a, b, c, d, e = [-1, 0, 0], [1, 0, 0], [0, np.sqrt(3), 0], [-1, -0.25, 0], [1, -0.25, 0]
        arcs = [ArcBetweenPoints(a, b, radius=-2, **arc_conf), ArcBetweenPoints(b, c, radius=2, **arc_conf), ArcBetweenPoints(c, a, radius=2, **arc_conf), ArcBetweenPoints(d, e, radius=-2, **arc_confi)]
        gate = ArcPolygonFromArcs(arcs[0], arcs[1], arcs[2], **poly_conf)
        circle = Circle(1).set_color(WHITE).scale(0.15).set_stroke(width=5) # type: ignore
        gate1 = Group(gate, arcs[3]).center()
        xnor_gate = Group(gate1, circle).arrange_in_grid(2,1, row_heights=[-2.9,0])

        dot0, dot1, dot2, dot3, dot4, dot5 = Dot([-0.5, -0.72, 0]), Dot(bits[0]), Dot([0.5, -0.72, 0]), Dot(bits[1]), Dot([0, 1.15, 0]), Dot(bits[2])
        g0 = Group(dot1, dot3, dot5)
        l0, l1, l2 = Line(dot1.get_center(), dot0.get_center()), Line(dot3.get_center(), dot2.get_center()), Line(dot4.get_center(), dot5.get_center())
        g1 = Group(l0, l1, l2)
        g2 = Group(g0, g1, xnor_gate).shift(RIGHT * 3)
        
        text0, text1, text2 = Text("I1").move_to(dot1).shift(DOWN * 0.5), Text("I2").move_to(dot3).shift(DOWN * 0.5), Text("O").move_to(dot5).shift(UP * 0.5)
        g4 = Group(text0, text1, text2)
        g3 = Group(g, g2, g4)
        self.add(g3)

        a0 = Arrow(start=RIGHT, end=LEFT, color=WHITE).shift(UP * 0.45, LEFT * 0.3)
        a0.generate_target()
        self.play(FadeIn(a0))

        dots = [Dot(bits[i]).set_color(GOLD) for i in range(3)]  # type: ignore
        for i in range(4):
            anim, fade = [], []
            if i < 2:
                anim.append(MoveAlongPath(dots[0], l0))
                fade.append(FadeOut(dots[0]))
            if i % 2 == 0:
                anim.append(MoveAlongPath(dots[1], l1))
                fade.append(FadeOut(dots[1]))
            if i != 3:
                self.play(*anim, rate_func=linear)
                self.play(*fade)
            if i == 0 or i == 3:
                self.play(MoveAlongPath(dots[2], l2))
                self.play(FadeOut(dots[2]))
            a0.target.shift(DOWN * 0.65)  # type: ignore
            if i != 3:
                self.play(MoveToTarget(a0))
                self.wait(0.4)
        self.wait(1)
