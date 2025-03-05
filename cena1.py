from manim import *
from manim.mobject.geometry.line import DashedVMobject

class ProductionMixProblem(Scene):
    def construct(self):
        # Modelo Matemático
        model = MathTex(
            r"\text{Maximizar } Z = 3x + 2y",
            r"\text{sujeito a:}",
            r"2x + y \leq 18",
            r"2x + 3y \leq 42",
            r"3x + y \leq 24",
            r"x, y \geq 0",
            font_size=36
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.8)
        
        model.move_to(ORIGIN)
        self.play(Write(model), run_time=3)
        self.wait(2)
        
        # Transição do modelo para a direita
        self.play(model.animate.scale(0.7).to_corner(UR, buff=1))
        self.wait(1)

        # Tabela inicial
        table_data = [
            ["Ponto", "Coordenadas"],
            ["O", "(0,0)"],
            ["F", "(8,0)"],
            ["H", "(6,6)"],
            ["G", "(3,12)"],
            ["C", "(0,14)"],
        ]
        table = Table(
            table_data,
            include_outer_lines=True
        ).scale(0.4).to_edge(LEFT, buff=1)
        
        self.play(Create(table))
        self.wait(2)

        # Gráfico
        axes = Axes(
            x_range=[0, 30, 10],
            y_range=[0, 30, 10],
            x_length=7,
            y_length=5.5,
            axis_config={
                "include_numbers": True,
                "tip_length": 0.35,
                "tip_width": 0.35,
                "stroke_width": 3
            },
        ).to_edge(RIGHT, buff=1.5)
        
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Pontos no gráfico
        points = VGroup(
            Dot(axes.c2p(0, 0), color=WHITE),
            Dot(axes.c2p(8, 0), color=WHITE),
            Dot(axes.c2p(6, 6), color=WHITE),
            Dot(axes.c2p(3, 12), color=WHITE),
            Dot(axes.c2p(0, 14), color=WHITE),
        )
        
        labels = VGroup(
            Tex("(0,0)").scale(0.5).next_to(points[0], DL),
            Tex("(8,0)").scale(0.5).next_to(points[1], DOWN),
            Tex("(6,6)").scale(0.5).next_to(points[2], UR),
            Tex("(3,12)").scale(0.5).next_to(points[3], UR),
            Tex("(0,14)").scale(0.5).next_to(points[4], LEFT),
        )

        # Animação do gráfico
        self.play(FadeIn(axes, axes_labels))
        self.wait(1)
        
        # Plota pontos primeiro
        for point, label in zip(points, labels):
            self.play(FadeIn(point), Write(label))
            self.wait(0.5)
        self.wait(1)

        # Criação da legenda e restrições
        legend = VGroup(
            MathTex(r"2x + y \leq 18", color=YELLOW),
            MathTex(r"2x + 3y \leq 42", color=BLUE),
            MathTex(r"3x + y \leq 24", color=RED),
            Tex("Região Viável", color=PURPLE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).scale(0.6)
        legend.next_to(model, DOWN, buff=0.5)

        # Restrições
        line1 = DashedVMobject(axes.plot(lambda x: 18 - 2*x, x_range=[0,9], color=YELLOW))
        line2 = DashedVMobject(axes.plot(lambda x: (42 - 2*x)/3, x_range=[0,21], color=BLUE))
        line3 = DashedVMobject(axes.plot(lambda x: 24 - 3*x, x_range=[0,8], color=RED))

        # Região viável
        feasible_vertices = [
            axes.c2p(0, 0),
            axes.c2p(8, 0),
            axes.c2p(6, 6),
            axes.c2p(3, 12),
            axes.c2p(0, 14),
        ]
        feasible_region = Polygon(
            *feasible_vertices,
            color=PURPLE,
            fill_color=PURPLE,
            fill_opacity=0.3,
            stroke_width=4
        )

        # Animação das restrições e legenda
        self.play(Create(line1), FadeIn(legend[0]))
        self.wait(1)
        self.play(Create(line2), FadeIn(legend[1]))
        self.wait(1)
        self.play(Create(line3), FadeIn(legend[2]))
        self.wait(1)
        
        # Mostra região viável e legenda
        self.play(FadeIn(feasible_region), FadeIn(legend[3]))
        self.wait(1)

        # Atualiza tabela com Z
        new_table_data = [
            ["Ponto", "Coordenadas", "Z"],
            ["O", "(0,0)", "0"],
            ["F", "(8,0)", "24"],
            ["H", "(6,6)", "30"],
            ["G", "(3,12)", "33"],
            ["C", "(0,14)", "28"],
        ]
        new_table = Table(
            new_table_data,
            include_outer_lines=True
        ).scale(0.35).to_edge(LEFT, buff=1)
        
        highlight = SurroundingRectangle(new_table.get_rows()[4], color=GREEN, buff=0.1)
        
        # Animação da tabela e destaque do ótimo
        self.play(
            ReplacementTransform(table, new_table),
            FadeIn(highlight)
        )
        
        # Destaque do ponto ótimo
        optimal_label = Tex("Solução Ótima", color=ORANGE).scale(0.5)
        optimal_label.next_to(points[3], RIGHT, buff=0.2)
        
        self.play(
            points[3].animate.set_color(ORANGE),
            FadeIn(optimal_label),
            run_time=1.5
        )
        self.wait(3)