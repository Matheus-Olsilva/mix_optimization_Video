from manim import *

# Configure TexTemplate to use XeLaTeX and fontspec
my_template = TexTemplate()
my_template.add_to_preamble(r"""
\usepackage{fontspec}
\setmainfont{IBM Plex Sans}
""")

class ProductionMix(Scene):
    def construct(self):
        self.entrada()
        self.espera()
        self.saida()
        self.conceitos_mix_producao()
        self.apresentacao_problema2()
        self.apresentacao_info_adicionais()

    def entrada(self):
        logo_path = r"C:\Users\Mathe\Desktop\Free_Lance\Harumi\Videos\mix_producao\mix_optimization_Video\harumi_logo.png"
        self.logo = ImageMobject(logo_path).scale(0.9)
        
        # Cria retângulo com proporções específicas
        self.rect = Rectangle(
            width=self.logo.height * (102/157),
            height=self.logo.height,
            color=WHITE,
            stroke_width=10
        ).move_to(self.logo)

        # Texto formatado
        self.harumi_text = Text(
            "HARUMI",
            font="IBM Plex Sans",
            weight=BOLD,
            font_size=40,
            color=WHITE
        ).next_to(self.logo, DOWN, buff=0.5)

        # Animação de entrada
        self.play(
            Create(self.rect, run_time=2),
            rate_func=rate_functions.ease_in_out_sine
        )
        self.play(
            FadeIn(self.logo, run_time=1.5),
            self.rect.animate.set_stroke(opacity=0),
            lag_ratio=0.5
        )
        self.play(
            Write(self.harumi_text, run_time=1.5),
            rate_func=rate_functions.ease_in_out_sine
        )

    def espera(self):
        self.wait(1)

    def saida(self):
        self.play(
            FadeOut(self.logo),
            FadeOut(self.harumi_text),
            run_time=1.2
        )
        self.wait(0.3)

    def conceitos_mix_producao(self):

        text1 = Tex(
            r"Imagine que você possui uma empresa de laticínios",
            font_size=40, color="#FFFFFF")
        
        text1.to_corner(UL).shift(RIGHT * 0.2 + DOWN*1.0)

        factory = SVGMobject(
            r"C:\Users\Mathe\Desktop\Free_Lance\Harumi\Videos\mix_producao\mix_optimization_Video\factory.svg"
        )
        factory.scale(0.7)
        factory.next_to(text1, RIGHT, buff=0.5)

        #factory.shift(DOWN*0.5 + LEFT*6.0)

        text2 = Tex(
            r"e deseja aumentar os seus lucros",
            font_size=40, color="#FFFFFF"
        )
        text2.next_to(factory, DOWN * 2.5 , buff=0.5).to_edge(LEFT)

        money = SVGMobject(
            r"C:\Users\Mathe\Desktop\Free_Lance\Harumi\Videos\mix_producao\mix_optimization_Video\money.svg"
        ).scale(0.4)
        money.next_to(text2, RIGHT, buff=0.2)

        grupo_text_money = VGroup(text2, money)

        # --- Crie aqui a seta (arrow) ---
        arrow = SVGMobject(
            r"C:\Users\Mathe\Desktop\Free_Lance\Harumi\Videos\mix_producao\mix_optimization_Video\seta.svg"
        ).scale(0.4)
        # Posicione a seta na região demarcada (por exemplo, logo à direita do money)
        arrow.next_to(money, RIGHT, buff=0.2)

        heading = Tex(
            r"A sua empresa Produz:",
            font_size=40, color="#FFFFFF"
        )
        heading.to_edge(LEFT).shift(DOWN * 2.0)

        cheese = SVGMobject(
            r"C:\Users\Mathe\Desktop\Free_Lance\Harumi\Videos\mix_producao\mix_optimization_Video\cheese.svg"
        ).scale(0.4)
        cheese_text = Tex("Queijo", font_size=30)
        cheese_group = VGroup(cheese, cheese_text).arrange(DOWN, buff=0.2)

        iorgute = SVGMobject(
            r"C:\Users\Mathe\Desktop\Free_Lance\Harumi\Videos\mix_producao\mix_optimization_Video\iorgute.svg"
        ).scale(0.4)
        iorgute_text = Tex("Iorgute", font_size=30)
        iorgute_group = VGroup(iorgute, iorgute_text).arrange(DOWN, buff=0.2)

        products = VGroup(cheese_group, iorgute_group).arrange(RIGHT, buff=0.5)
        products.next_to(heading, RIGHT, buff=0.4)

        grupo = VGroup(text1, factory, text2, money, heading, products)

        # --- Animações ---
        self.play(Write(text1, run_time = 3))
        self.wait(0.5)
        self.play(FadeIn(factory))
        self.play(FadeIn(grupo_text_money))
        self.wait(1)
        self.play(GrowFromEdge(arrow, edge=DOWN)) 
        self.wait(0.5)
        self.play(FadeIn(heading))
        self.wait(1)
        self.play(FadeIn(products))
        self.wait(3)
        self.play(FadeOut(grupo), FadeOut(arrow))

    def apresentacao_problema2(self):
        # Texto introdutório
        texto_intro = Tex(
            r"\raggedright \fontfamily{IBM Plex Sans}\selectfont Devido a razões contratuais, a empresa necessita produzir\\uma quantidade mínima diária:",
            font_size=40, color="#FFFFFF"
        ).to_edge(LEFT)

        # Lista com quantidades mínimas (alinhada à esquerda)
        lista_quantidades = BulletedList(
            r"\raggedright \fontfamily{IBM Plex Sans}\selectfont 320kg de iogurte;",
            r"\raggedright \fontfamily{IBM Plex Sans}\selectfont 380kg de queijo Mussarela;",
            font_size=40,
            buff=0.5, color="#FFFFFF"
        ).to_edge(LEFT)

        # Texto final sobre mercado garantido
        texto_final = Tex(
            r"\raggedright \fontfamily{IBM Plex Sans}\selectfont A área comercial da empresa garante que existe mercado \\ para absorver qualquer nível de produção",
            font_size=40, color="#FFFFFF"
        ).to_edge(LEFT)

        # Agrupando elementos (sem move_to para manter alinhamento)
        grupo = VGroup(texto_intro, lista_quantidades, texto_final).arrange(DOWN, buff=0.5, aligned_edge=LEFT)

        # Animações
        self.play(Write(texto_intro))
        self.wait(1)
        self.play(Write(lista_quantidades))
        self.wait(1)
        self.play(Write(texto_final))
        self.wait(4)
        self.play(FadeOut(grupo))

    def apresentacao_info_adicionais(self):
            # Texto introdutório
            texto_intro = Tex(
                r"Você também possui informações sobre:",
                font_size=40
            ).to_edge(LEFT)

            # Lista com quantidades mínimas (alinhada à esquerda)
            lista_quantidades = BulletedList(
                r"\raggedright \fontfamily{IBM Plex Sans}\selectfont Matérias-primas usadas para fabricar cada produto;",
                r"\raggedright \fontfamily{IBM Plex Sans}\selectfont Disponibilidade de matérias-primas e demandas;",
                r"\raggedright \fontfamily{IBM Plex Sans}\selectfont Margem de contribuição de cada produto.",

                font_size=40,
                buff=0.5  
            ).to_edge(LEFT)


            # Agrupando elementos (sem move_to para manter alinhamento)
            grupo = VGroup(texto_intro, lista_quantidades).arrange(DOWN, buff=0.5, aligned_edge=LEFT)

            # Animações
            self.play(Write(texto_intro, run_time = 1))
            self.wait(2)
            self.play(Write(lista_quantidades, run_time = 3))
            self.wait(3)
            self.play(FadeOut(grupo))