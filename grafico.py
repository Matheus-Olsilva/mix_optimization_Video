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
                MathTex(r"0.70x_1 + 0.40x_2 \leq 1200", font_size=36),
                [(1714.29, 0), (0, 3000)]  # Interceptos específicos
            ),
            # R2 (↓)
            (
                Line(
                    axes.coords_to_point(2875, 0),
                    axes.coords_to_point(0, 1437.5),
                    color=GREEN
                ),
                "R2",
                MathTex(r"0.16x_1 + 0.32x_2 \leq 460", font_size=36),
                [(2875, 0), (0, 1437.5)]
            ),
            # R3 (↓)
            (
                Line(
                    axes.coords_to_point(2600, 0),
                    axes.coords_to_point(0, 1969.7),
                    color=BLUE
                ),
                "R3",
                MathTex(r"0.25x_1 + 0.33x_2 \leq 650", font_size=36),
                [(2600, 0), (0, 1969.7)]
            ),
            # R4 (↓)
            (
                Line(
                    axes.coords_to_point(3400, 0),
                    axes.coords_to_point(0, 1888.9),
                    color=YELLOW
                ),
                "R4",
                MathTex(r"0.05x_1 + 0.09x_2 \leq 170", font_size=36),
                [(3400, 0), (0, 1888.9)]
            ),
            # R5 (→)
            (
                Line(
                    axes.coords_to_point(320, 0),
                    axes.coords_to_point(320, 3500),
                    color=PURPLE
                ),
                "R5",
                MathTex(r"x_1 \geq 320", font_size=36),
                [(320, 0)]  # Intercepto único
            ),
            # R6 (↑)
            (
                Line(
                    axes.coords_to_point(0, 450),
                    axes.coords_to_point(4000, 450),
                    color=ORANGE
                ),
                "R6",
                MathTex(r"x_2 \geq 450", font_size=36),
                [(0, 450)]  # Intercepto único
            ),
        ]

        # Criação da legenda
        legend = VGroup()
        all_line_dots = []  # Armazena todos os pontos das retas
        for line, label, equation, _ in lines_and_equations:
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

        # Animação sincronizada de retas e pontos
        for i, (line, label, equation, intercepts) in enumerate(lines_and_equations):
            # Cria pontos com a cor da linha
            line_dots = VGroup(*[
                Dot(axes.coords_to_point(x, y), color=line.get_color(), radius=0.07)
                for x, y in intercepts
            ])
            all_line_dots.append(line_dots)  # Armazena os pontos

            # Animação combinada
            self.play(
                Create(line),
                LaggedStartMap(GrowFromCenter, line_dots, lag_ratio=0.3),
                legend[i].animate.set_opacity(1).shift(LEFT*0.1),
                run_time=2.5
            )
            self.wait(0.5)

        # Definição dos grupos de setas por área
        arrow_groups = {
            "horizontal_top": [
                ([390, 2900], [550, 2900]),
                ([390, 2750], [550, 2750]),
                ([390, 2600], [550, 2600]),
                ([390, 2450], [550, 2450])
            ],
            "diagonal": [
                ([600, 2400], [500, 2200]),
                ([650, 2300], [550, 2100]),
                ([710, 2200], [610, 2000]),
                ([770, 2100], [670, 1900]),
                ([830, 2000], [730, 1800]),
                ([890, 1900], [790, 1700]),
                ([950, 1800], [850, 1600]),
                ([1010, 1700], [910, 1500])
            ],
            "diagonal_long": [
                ([1050, 1600.0], [960, 1380.0]),
                ([1140, 1555.0], [1050, 1335.0]),
                ([1230, 1510.0], [1140, 1290.0]),
                ([1320, 1465.0], [1230, 1245.0]),
                ([1410, 1420.0], [1320, 1200.0]),
                ([1500, 1375.0], [1410, 1155.0]),
                ([1590, 1330.0], [1500, 1110.0]),
                ([1680, 1285.0], [1590, 1065.0]),
                ([1770, 1240.0], [1680, 1020.0]),
                ([1860, 1195.0], [1770, 975.0]),
                ([1950, 1150.0], [1860, 930.0]),
                ([2040, 1105.0], [1950, 885.0]),
                ([2130, 1060.0], [2040, 840.0]),
                ([2220, 1015.0], [2130, 795.0]),
                ([2310, 970.0], [2220, 750.0]),
                ([2400, 925.0], [2310, 705.0]),
                ([2490, 880.0], [2400, 660.0]),
                ([2580, 835.0], [2490, 615.0]),
                ([2670, 790.0], [2580, 570.0])
            ],
            "vertical_right": [
                ([2800, 550], [2800, 800]),
                ([2900, 550], [2900, 800]),
                ([3000, 550], [3000, 800]),
                ([3100, 550], [3100, 800]),
                ([3200, 550], [3200, 800]),
                ([3300, 550], [3300, 800]),
                ([3400, 550], [3400, 800]),
                ([3500, 550], [3500, 800]),
                ([3600, 550], [3600, 800]),
                ([3700, 550], [3700, 800])
            ]
        }
        
        # Função para criar setas com estilo aprimorado
        def create_arrow(start, end):
            return Arrow(
                axes.coords_to_point(start[0], start[1]),
                axes.coords_to_point(end[0], end[1]),
                color="#4E4AE8",
                buff=0,
                stroke_width=6,  # Ligeiramente mais fino para um estilo mais elegante
                tip_length=0.25,  # Ponta ligeiramente menor
                max_stroke_width_to_length_ratio=6,
                max_tip_length_to_length_ratio=0.35
            )
        
        # Criar grupos de setas
        arrow_mobjects = {}
        for group_name, arrow_coords in arrow_groups.items():
            arrow_mobjects[group_name] = VGroup(*[
                create_arrow(start, end) for start, end in arrow_coords
            ])
            
        # Animação com estilo 3Blue1Brown: aparecimento gradual por grupos
        # Cada grupo tem uma leve cascata interna
        
        # 1. Horizontal superior (da esquerda para a direita)
        self.play(
            LaggedStart(*[
                FadeIn(arrow, scale=0.95) 
                for arrow in arrow_mobjects["horizontal_top"]
            ], lag_ratio=0.15),
            run_time=1.2
        )
        
        # 2. Diagonal superior (aparecimento em cascata)
        self.play(
            LaggedStart(*[
                FadeIn(arrow, scale=0.95) 
                for arrow in arrow_mobjects["diagonal"]
            ], lag_ratio=0.08),
            run_time=1.3
        )
        
        # 3. Diagonal longa (aparecimento em cascata)
        self.play(
            LaggedStart(*[
                FadeIn(arrow, scale=0.95) 
                for arrow in arrow_mobjects["diagonal_long"]
            ], lag_ratio=0.04),
            run_time=1.5
        )
        
        # 4. Vertical direita (de baixo para cima)
        self.play(
            LaggedStart(*[
                FadeIn(arrow, scale=0.95) 
                for arrow in arrow_mobjects["vertical_right"]
            ], lag_ratio=0.08),
            run_time=1.2
        )
        
        # Reagrupar todas as setas para manipulação posterior
        all_arrows = VGroup(
            *arrow_mobjects["horizontal_top"],
            *arrow_mobjects["diagonal"],
            *arrow_mobjects["diagonal_long"],
            *arrow_mobjects["vertical_right"]
        )
        
        # Efeito sutil de destaque (estilo 3Blue1Brown)
        self.play(
            AnimationGroup(
                all_arrows.animate.set_color("#6E6EFF"),  # Azul ligeiramente mais claro
                all_arrows.animate.set_stroke_width(7),   # Ligeiramente mais grosso
            ),
            run_time=1,
            rate_func=there_and_back_with_pause
        )
        
        self.wait(1)

        # Explicação das setas
        explicacao = Tex(r"As setas sinalizam o sentido das desigualdades\\em cada restrição, apontando a região de solução", 
                        font_size=30).next_to(legend, LEFT, buff=0.5).shift(UP*1)
        self.play(Write(explicacao, run_time=2))
        self.wait(4)
        
        # Fade out mais elegante
        self.play(
            FadeOut(explicacao, shift=UP*0.2),
            FadeOut(all_arrows, lag_ratio=0.04, scale=0.9),
            run_time=1.5
        )

        # # Interseções relevantes
        # intersections = [
        #     ((320, 450), ["R5", "R6"]),
        #     ((1457.14, 450), ["R1", "R6"]),
        #     ((1250, 812.5), ["R1", "R2"]),
        #     ((320, 1277.5), ["R2", "R5"])
        # ]

        # # Criação dos destaques
        # intersection_dots = VGroup()
        # intersection_labels = VGroup()
        # for point, labels in intersections:
        #     x, y = point
        #     dot = Dot(axes.coords_to_point(x, y), color=YELLOW, radius=0.1)
        #     label = MathTex(f"{{{', '.join(labels)}}}", font_size=30, color=WHITE).next_to(dot, UP, buff=0.2)
        #     intersection_dots.add(dot)
        #     intersection_labels.add(label)

        # # Animação dos destaques
        # self.play(
        #     LaggedStartMap(GrowFromCenter, intersection_dots, lag_ratio=0.2),
        #     LaggedStartMap(FadeIn, intersection_labels, shift=UP, lag_ratio=0.2),
        #     run_time=3
        # )
        # self.wait(1)

        # # Região viável
        # feasible_region = Polygon(
        #     axes.coords_to_point(320, 450),
        #     axes.coords_to_point(1457.14, 450),
        #     axes.coords_to_point(1250, 812.5),
        #     axes.coords_to_point(320, 1277.5),
        #     fill_color=BLUE,
        #     fill_opacity=0.3,
        #     stroke_opacity=0  # Remove borda branca
        # )

        # # Linhas recortadas
        # clipped_lines = VGroup(
        #     Line(axes.coords_to_point(1457.14, 450), axes.coords_to_point(1250, 812.5), color=RED),
        #     Line(axes.coords_to_point(1250, 812.5), axes.coords_to_point(320, 1277.5), color=GREEN),
        #     Line(axes.coords_to_point(320, 450), axes.coords_to_point(320, 1277.5), color=PURPLE),
        #     Line(axes.coords_to_point(320, 450), axes.coords_to_point(1457.14, 450), color=ORANGE)
        # )

        # # Remoção de linhas não-essenciais e seus pontos
        # non_boundary_indices = [2, 3]  # R3 e R4
        # non_boundary_lines = VGroup(*[lines_and_equations[i][0] for i in non_boundary_indices])
        # non_boundary_dots = VGroup(*[all_line_dots[i] for i in non_boundary_indices])

        # self.play(
        #     FadeOut(non_boundary_lines),
        #     FadeOut(non_boundary_dots),  
        #     run_time=1.5
        # )

        # # Transição para região viável
        # original_line_indices = [0, 1, 4, 5]  # R1, R2, R5, R6
        # original_lines = VGroup(*[lines_and_equations[i][0] for i in original_line_indices])
        # original_dots = VGroup(*[all_line_dots[i] for i in original_line_indices])

        # self.play(
        #     FadeOut(original_lines),
        #     FadeOut(original_dots),  
        #     Create(clipped_lines),
        #     FadeIn(feasible_region),
        #     run_time=2
        # )

        # # Explicação final
        # explicacao_regiao = Tex(r"A região viável indica o espaço de solução,\\que satisfaz todas as restrições", 
        #                         font_size=24).next_to(legend, LEFT, buff=0.5).shift(LEFT*1)
        # arrow5 = Arrow(explicacao_regiao.get_center() + DOWN*0.5, feasible_region.get_center(), 
        #               color="#605CEA", buff=0, max_stroke_width_to_length_ratio=5,
        #               max_tip_length_to_length_ratio=0.3)

        # self.play(Write(explicacao_regiao, run_time=2))
        # self.play(Create(arrow5))
        # self.wait(6)
        # self.play(FadeOut(explicacao_regiao), FadeOut(arrow5))