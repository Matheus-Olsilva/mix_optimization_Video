from manim import *

my_template = TexTemplate()
my_template.add_to_preamble(r"""
\usepackage{fontspec}
\setmainfont{IBM Plex Sans}
""")

class grafico(Scene):
    def construct(self):
        self.modelo()
        self.camera.background_color = "#000000"
        config.frame_width = 12
        config.frame_height = 8

    def modelo(self):
        # Grafico
        axes = Axes(
            x_range=[0, 4000, 1000],
            y_range=[0, 3500, 1000],
            x_length=12,
            y_length=6,
            axis_config={"include_numbers": True, "font_size": 24},
        ).add_coordinates()

        # Definição de todas as retas com setas completas
        lines_and_equations = [
            # R1 (↓)
            (
                Line(
                    axes.coords_to_point(1714.29, 0),
                    axes.coords_to_point(0, 3000),
                    color=RED
                ),
                "R1",
                MathTex(r"0.70x_1 + 0.40x_2 \leq 1200", font_size=36)
            ),
            # R2 (↓)
            (
                Line(
                    axes.coords_to_point(2875, 0),
                    axes.coords_to_point(0, 1437.5),
                    color=GREEN
                ),
                "R2",
                MathTex(r"0.16x_1 + 0.32x_2 \leq 460", font_size=36)
            ),
            # R3 (↓)
            (
                Line(
                    axes.coords_to_point(2600, 0),
                    axes.coords_to_point(0, 1969.7),
                    color=BLUE
                ),
                "R3",
                MathTex(r"0.25x_1 + 0.33x_2 \leq 650", font_size=36)
            ),
            # R4 (↓)
            (
                Line(
                    axes.coords_to_point(3400, 0),
                    axes.coords_to_point(0, 1888.9),
                    color=YELLOW
                ),
                "R4",
                MathTex(r"0.05x_1 + 0.09x_2 \leq 170", font_size=36)
            ),
            # R5 (→)
            (
                Line(
                    axes.coords_to_point(320, 0),
                    axes.coords_to_point(320, 3500),
                    color=PURPLE
                ),
                "R5",
                MathTex(r"x_1 \geq 320", font_size=36)
            ),
            # R6 (↑)
            (
                Line(
                    axes.coords_to_point(0, 450),
                    axes.coords_to_point(4000, 450),
                    color=ORANGE
                ),
                "R6",
                MathTex(r"x_2 \geq 450", font_size=36)
            ),
        ]

        # Criação da legenda completa
        legend = VGroup()
        for line, label, equation in lines_and_equations:
            color = line.get_color()
            entry = VGroup(
                Dot(color=color, radius=0.05),
                MathTex(label, font_size=36).set_color(WHITE),
                equation.copy()
            ).arrange(RIGHT, buff=0.3)
            legend.add(entry)
        legend.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        legend.to_corner(UR, buff=0.5)
        legend.scale(0.7)
        legend.set_opacity(0)
        self.add(legend)

        # Animação inicial do eixo
        self.play(Create(axes))
        self.wait(1)

        # Lista de interceptos (agora associados às linhas)
        intercepts = [
            (1714.29, 0), (0, 3000),   # R1
            (2875, 0), (0, 1437.5),    # R2
            (2600, 0), (0, 1969.7),    # R3
            (3400, 0), (0, 1888.9),    # R4
            (320, 0),                  # R5
            (0, 450),                  # R6
        ]

        # Animação sincronizada de retas, pontos e legendas
        for i, (line, label, equation) in enumerate(lines_and_equations):
            # Determina os pontos de intercepto para esta linha
            if i < 4:
                line_intercepts = intercepts[2*i : 2*i+2]
            elif i == 4:
                line_intercepts = [intercepts[8]]
            else:
                line_intercepts = [intercepts[9]]

            # Cria pontos com a cor da linha
            line_color = line.get_color()
            line_dots = VGroup(*[
                Dot(axes.coords_to_point(x, y), color=line_color, radius=0.05)
                for x, y in line_intercepts
            ])

            # Animação combinada
            self.play(
                Create(line),
                LaggedStartMap(GrowFromCenter, line_dots, lag_ratio=0.2),
                legend[i].animate.set_opacity(1).shift(LEFT*0.1),
                run_time=2
            )
            self.wait(0.5)

        # Restante da animação (setas, região viável, etc.)
        arrow1 = Arrow(
            start=axes.coords_to_point(1800, 1800),  
            end=axes.coords_to_point(1600, 1200),  
            color="#77CF7B",
            buff=0,
            max_stroke_width_to_length_ratio=5,
            max_tip_length_to_length_ratio=0.3
        )
        arrow2 = Arrow(
            start=axes.coords_to_point(1200, 2400),  
            end=axes.coords_to_point(1000, 1800), 
            color="#77CF7B",
            buff=0,
            max_stroke_width_to_length_ratio=5,
            max_tip_length_to_length_ratio=0.3
        )
        arrow3 = Arrow(
            start=axes.coords_to_point(500, 2700),  
            end=axes.coords_to_point(900, 2700), 
            color="#77CF7B",
            buff=0,
            max_stroke_width_to_length_ratio=5,
            max_tip_length_to_length_ratio=0.3
        )
        arrow4 = Arrow(
            start=axes.coords_to_point(2800, 600),  
            end=axes.coords_to_point(2800, 1200), 
            color="#77CF7B",
            buff=0,
            max_stroke_width_to_length_ratio=5,
            max_tip_length_to_length_ratio=0.3
        )

        arrows = [arrow1, arrow2, arrow3, arrow4]
        for arrow in arrows:
            self.play(Create(arrow), run_time=1.5)
            self.wait(0.3)
        self.wait(2)

        explicacao = Tex(r"As setas sinalizam o sentido das desigualdades\\"
                        r"em cada restrição, "
                        r"apontando a região de solução", font_size=30).next_to(legend, LEFT, buff=0.5).shift(UP*1)
        self.play(Write(explicacao, run_time = 2))
        self.wait(4)
        self.play(FadeOut(explicacao))
        arrows_group = VGroup(*arrows)
        self.play(FadeOut(arrows_group))

        intersections = [
            ((320, 450), ["R5", "R6"]),     
            ((1457.14, 450), ["R1", "R6"]), 
            ((1250, 812.5), ["R1", "R2"]),  
            ((320, 1277.5), ["R2", "R5"])   
        ]

        intersection_dots = VGroup()
        intersection_labels = VGroup()
        for point, labels in intersections:
            x, y = point
            dot = Dot(axes.coords_to_point(x, y), color=YELLOW, radius=0.1)
            label = MathTex(f"{{{', '.join(labels)}}}", font_size=30, color=WHITE)
            label.next_to(dot, UP, buff=0.2)
            intersection_dots.add(dot)
            intersection_labels.add(label)

        self.play(
            LaggedStartMap(GrowFromCenter, intersection_dots, lag_ratio=0.2),
            LaggedStartMap(FadeIn, intersection_labels, shift=UP, lag_ratio=0.2),
            run_time=3
        )
        self.wait(1)

        feasible_region = Polygon(
            axes.coords_to_point(320, 450),
            axes.coords_to_point(1457.14, 450),
            axes.coords_to_point(1250, 812.5),
            axes.coords_to_point(320, 1277.5),
            color=WHITE,
            fill_color=BLUE,
            fill_opacity=0.3
        )

        explicacao_regiao = Tex(r"A região viável indica o espaço de solução,\\"
                                r"que satisfaz todas as restrições", font_size=24).next_to(legend, LEFT, buff=0.5).shift(LEFT*1)
        arrow5 = Arrow(
            start=explicacao_regiao.get_center() + DOWN*0.5,  
            end=feasible_region.get_center(),  
            color="#605CEA",
            buff=0,
            max_stroke_width_to_length_ratio=5,
            max_tip_length_to_length_ratio=0.3)
        
        self.play(Write(explicacao_regiao, run_time = 2))
        self.wait(4)
        self.play(Create(arrow5), run_time = 2)
        self.wait(3)
        self.play(FadeIn(feasible_region))

        boundary_lines_indices = [0, 1, 4, 5]
        non_boundary_lines = VGroup()
        non_boundary_legend = VGroup()
        for i, (line, _, _) in enumerate(lines_and_equations):
            if i not in boundary_lines_indices:
                non_boundary_lines.add(line)
                non_boundary_legend.add(legend[i])

        self.play(
            FadeOut(non_boundary_lines),
            FadeOut(non_boundary_legend),
            run_time=2
        )
        self.wait(5)
        self.play(FadeOut(explicacao_regiao))