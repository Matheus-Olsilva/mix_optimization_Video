from manim import *

my_template = TexTemplate()
my_template.add_to_preamble(r"""
\usepackage{fontspec}
\setmainfont{IBM Plex Sans}
""")

class grafico(Scene):
    def construct(self):
        self.grafico()

        self.camera.background_color = "#000000"
        config.frame_width = 12
        config.frame_height = 8
        
    def grafico(self):

        Resumo_modelo = Tex(
            r"\raggedright \linespread{1.5}\selectfont " 
            r"Recapitulando o que abordamos até o momento, temos o seguinte modelo matemático:",
            font_size=25
        ).to_edge(LEFT, buff=0.5).shift(UP*2.5)
    
        variaveis_decisao = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"As variáveis de decisão, que representam a decisão que devemos tomar \\"
            r"$x_1$ = quantidade de iogurte a ser produzida \\"
            r"$x_2$ = quantidade de queijo a ser produzida",
            font_size=25
        ).next_to(Resumo_modelo, DOWN, aligned_edge=LEFT, buff=0.4)

        funcao_objetivo = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"Função objetivo: \\"
            r"Maximizar $Z = 0,80x_1 + 1,15x_2$",
            font_size=25
        ).next_to(variaveis_decisao, DOWN, aligned_edge=LEFT, buff=0.4)

        restricoes = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"Restrições de Capacidade Produtiva: \\"
            r"$0.70x_1 + 0.40x_2 \leq 1200$ \\"
            r"$0.16x_1 + 0.32x_2 \leq 460$ \\"
            r"$0.25x_1 + 0.33x_2 \leq 650$ \\"
            r"$0.05x_1 + 0.09x_2 \leq 170$",
            font_size=25
        ).next_to(funcao_objetivo, DOWN, aligned_edge=LEFT, buff=0.4)

        restricoes_demanda = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"Restrições de Demanda: \\"
            r"$x_1 \geq 320$ \\"
            r"$x_2 \geq 450$",
            font_size=25
        ).next_to(restricoes, RIGHT, aligned_edge=LEFT, buff=0.4).shift(RIGHT*2.5+UP*0.45)

        self.play(Write(Resumo_modelo, run_time=2))
        self.play(Write(variaveis_decisao, run_time=2))
        self.play(Write(funcao_objetivo, run_time=5))
        self.play(Write(restricoes, run_time=5))
        self.play(Write(restricoes_demanda, run_time=5))
        self.wait(1)
        self.play(FadeOut(Resumo_modelo), FadeOut(variaveis_decisao))

        # Animação de subida
        self.play(
            funcao_objetivo.animate.scale(0.9).shift(UP * 3.0),
            restricoes.animate.scale(0.9).shift(UP * 3.2),
            restricoes_demanda.animate.scale(0.9).shift(UP * 3.2+LEFT*0.5),
            run_time=2
        )

        metodo_grafico = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"Para resolver este problema, utilizaremos o Método Gráfico que consiste em \\"
            r"encontrar a solução ótima do problema através da análise gráfica das restrições do modelo. Vamos começar analisando as restrições de capacidade produtiva:\\",
            font_size=25
        ).next_to(restricoes, DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(Write(metodo_grafico, run_time=5))
        self.play(FadeOut(metodo_grafico))

        resolucao = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"Consideraremos as inequações como equações e as representaremos graficamente por meio de retas nos eixos $x_1$ e $x_2$ \\",
            font_size=25
        ).next_to(restricoes, DOWN, aligned_edge=LEFT, buff=0.5)


        restricoes2 = MathTex(
            r"""
            0.70x_1 + 0.40x_2 &= 1200 \\
            0.16x_1 + 0.32x_2 &= 460 \\
            0.25x_1 + 0.33x_2 &= 650 \\
            0.05x_1 + 0.09x_2 &= 170
            """,
            font_size=25
        ).next_to(resolucao, DOWN, aligned_edge=LEFT, buff=0.4)

        self.play(Write(resolucao, run_time=5))
        self.play(Write(restricoes2, run_time=5))

        self.play(FadeOut(restricoes2))

        restricoes3 = MathTex(
            r"0.70x_1 + 0.40x_2 &= 1200\\",
            r"\quad \text{Para } x_1 = 0 &\rightarrow 0.40x_2 = 1200 \rightarrow x_2 = 3000\\",
            r"\quad \text{Para } x_2 = 0 &\rightarrow 0.70x_1 = 1200 \rightarrow x_1 = 1714.29\\",
            r"0.16x_1 + 0.32x_2 &= 460\\",
            r"\quad \text{Para } x_1 = 0 &\rightarrow 0.32x_2 = 460 \rightarrow x_2 = 1437.5\\",
            r"\quad \text{Para } x_2 = 0 &\rightarrow 0.16x_1 = 460 \rightarrow x_1 = 2875\\",
            font_size=25
        ).next_to(resolucao, DOWN, aligned_edge=LEFT, buff=0.4)

        restricoes4 = MathTex(r"0.25x_1 + 0.33x_2 &= 650\\",
            r"\quad \text{Para } x_1 = 0 &\rightarrow 0.33x_2 = 650 \rightarrow x_2 = 1969.7\\",
            r"\quad \text{Para } x_2 = 0 &\rightarrow 0.25x_1 = 650 \rightarrow x_1 = 2600\\",
            r"0.05x_1 + 0.09x_2 &= 170\\",
            r"\quad \text{Para } x_1 = 0 &\rightarrow 0.09x_2 = 170 \rightarrow x_2 = 1888.9\\",
            r"\quad \text{Para } x_2 = 0 &\rightarrow 0.05x_1 = 170 \rightarrow x_1 = 3400", font_size=25
        ).next_to(restricoes3, RIGHT, aligned_edge=LEFT, buff=0.4).shift(RIGHT*3.0)

        
        self.play(Write(restricoes3), run_time=10)
        self.play(Write(restricoes4), run_time=10)
        self.play(FadeOut(resolucao), FadeOut(restricoes), FadeOut(funcao_objetivo), FadeOut(restricoes_demanda))

        # Animação de subida

        self.play(
            restricoes3.animate.scale(0.9).shift(UP * 4.0),
            restricoes4.animate.scale(0.9).shift(UP * 4.0),
            run_time=2
        )
        restricoes = [
            [MathTex("0.70x_1 + 0.40x_2 = 1200"), Tex("1714.29"), Tex("3000")],
            [MathTex("0.16x_1 + 0.32x_2 = 460"), Tex("2875"), Tex("1437.5")],
            [MathTex("0.25x_1 + 0.33x_2 = 650"), Tex("2600"), Tex("1969.7")],
            [MathTex("0.05x_1 + 0.09x_2 = 170"), Tex("3400"), Tex("1888.9")]
        ]


        # Dados já formatados como MObjects
        dados = [
            [MathTex("0.70x_1 + 0.40x_2 = 1200"), Tex("1714.29"), Tex("3000")],
            [MathTex("0.16x_1 + 0.32x_2 = 460"), Tex("2875"), Tex("1437.5")],
            [MathTex("0.25x_1 + 0.33x_2 = 650"), Tex("2600"), Tex("1969.7")],
            [MathTex("0.05x_1 + 0.09x_2 = 170"), Tex("3400"), Tex("1888.9")]
        ]

        # Função de conversão personalizada
        def convert_element(element):
            return element  # Retorna o próprio elemento já formatado

        # Criação da tabela
        tabela = Table(
            table=dados,
            row_labels=[Text(f"R{i+1}") for i in range(4)],
            col_labels=[
                MathTex("\\text{Restrição}"),
                MathTex("\\text{Intercepto } x_1"),
                MathTex("\\text{Intercepto } x_2")
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
            v_buff=0.6,
            h_buff=1.2,
            element_to_mobject=convert_element  
        ).scale(0.6)

        # Posicionamento e animação
        tabela.to_edge(DOWN, buff=0.5)
        self.play(Create(tabela), run_time=2)
        self.wait()
