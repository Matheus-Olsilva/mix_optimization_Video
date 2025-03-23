from manim import *

my_template = TexTemplate()
my_template.add_to_preamble(r"""
\usepackage{fontspec}
\setmainfont{IBM Plex Sans}
""")

class ProductionMix(Scene):
    def construct(self):

        self.camera.background_color = "#000000"
        
        config.frame_width = 12
        config.frame_height = 8

        self.entrada()
        self.espera()
        self.saida()
        self.conceitos_mix_producao()
        self.apresentacao_problema2()
        self.apresentacao_info_adicionais()
        self.tabela1()
        self.exemplo_fun_obj()
        self.tabela02()
        self.modelo()
        

    def entrada(self):
        logo_path = r"C:\Users\Mathe\Desktop\Free_Lance\Harumi\Videos\mix_producao\mix_optimization_Video\harumi_logo.png"
        self.logo = ImageMobject(logo_path).scale(0.9).shift(LEFT*1.5)

        # Cria retângulo com proporções específicas
        self.rect = Rectangle(
            width=self.logo.height * (102/157),
            height=self.logo.height,
            color=WHITE,
            stroke_width=10
        ).move_to(self.logo)

        # Cria letras individualmente para o texto "HARUMI"
        letters = VGroup(*[
            Text(letter, font="IBM Plex Mono", font_size=80, color=WHITE)
            for letter in "HARUMI"
        ])
        # Arranja as letras com espaçamento customizado
        letters.arrange(RIGHT, buff=0.3)
        
        # Posicionamento manual para reduzir o espaço e centralizar verticalmente
        self.harumi_text = letters
        logo_right_edge = self.logo.get_right()
        
        # Corrigido: Usar DOWN * 0 para alinhar ao centro vertical do logo
        self.harumi_text.move_to(logo_right_edge + RIGHT * 1.8).align_to(self.logo, DOWN * 0)

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
        
        text1.to_corner(UL).shift(DOWN*1.0)

        factory = SVGMobject(
            r"C:\Users\Mathe\Desktop\Free_Lance\Harumi\Videos\mix_producao\mix_optimization_Video\factory.svg"
        )
        factory.scale(0.7)
        factory.next_to(text1, RIGHT, buff=0.5)

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
            r"A sua empresa produz:",
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
        texto_intro = Tex(
            r"\raggedright \fontfamily{IBM Plex Sans}\selectfont Devido a razões contratuais, a empresa necessita produzir\\uma quantidade mínima diária:",
            font_size=40, color="#FFFFFF"
        ).to_edge(LEFT)

        lista_quantidades = BulletedList(
            r"\raggedright \fontfamily{IBM Plex Sans}\selectfont 320kg de iogurte;",
            r"\raggedright \fontfamily{IBM Plex Sans}\selectfont 380kg de queijo.",
            font_size=40,
            buff=0.5, color="#FFFFFF"
        ).to_edge(LEFT)

        texto_final = Tex(
            r"\raggedright \fontfamily{IBM Plex Sans}\selectfont A área comercial da empresa garante que existe mercado \\ para absorver qualquer nível de produção",
            font_size=40, color="#FFFFFF"
        ).to_edge(LEFT)

        grupo = VGroup(texto_intro, lista_quantidades, texto_final)

        grupo.arrange(DOWN, aligned_edge=LEFT, buff=1.0).to_edge(LEFT, buff=0.5)

        # Animações
        self.play(Write(texto_intro, run_time = 3))
        self.wait(1)
        self.play(Write(lista_quantidades, running_start=2))
        self.wait(1)
        self.play(Write(texto_final, run_time = 3))
        self.wait(4)
        self.play(FadeOut(grupo))

    def apresentacao_info_adicionais(self):
            # Texto introdutório
            texto_intro = Tex(
                r"Você também possui informações sobre:",
                font_size=40
            ).to_edge(LEFT).shift(DOWN*5.0)

            # Lista com quantidades mínimas (alinhada à esquerda)
            lista_quantidade1 = BulletedList(
                r"\raggedright \fontfamily{IBM Plex Sans}\selectfont Matérias-primas usadas para fabricar cada produto;",

                font_size=40,
            ).to_edge(LEFT).shift(DOWN*0.5)

            lista_quantidade2 = BulletedList(
                r"\raggedright \fontfamily{IBM Plex Sans}\selectfont Disponibilidade de matérias-primas e demandas;",

                font_size=40,
            ).next_to(lista_quantidade1,DOWN).to_edge(LEFT).shift(DOWN*0.5)

            lista_quantidade3 = BulletedList(
                r"\raggedright \fontfamily{IBM Plex Sans}\selectfont Margem de contribuição de cada produto.",

                font_size=40,
            ).next_to(lista_quantidade2, DOWN).to_edge(LEFT).shift(DOWN*0.5)

            lista_quantidades = VGroup(lista_quantidade1, lista_quantidade2, lista_quantidade3)
            # Agrupando elementos (sem move_to para manter alinhamento)
            grupo = VGroup(texto_intro, lista_quantidades)

            grupo.arrange(DOWN, aligned_edge=LEFT, buff=0.5).to_edge(LEFT, buff=0.5)

            # Animações
            self.play(Write(texto_intro, run_time = 3))
            self.wait(2)
            self.play(Write(lista_quantidade1, run_time = 3))
            self.play(Write(lista_quantidade2, run_time = 3))
            self.play(Write(lista_quantidade3, run_time = 3))
            self.wait(3)
            self.play(FadeOut(grupo))

    def tabela1(self):
        
        titulo = Text(
            "Tabela 1: Margem de Contribuição Unitária (R$/kg)",
            font="IBM Plex Sans", 
            color=WHITE,
            font_size=25  
        ).to_edge(UP, buff=0.3)
        
        tabela = Table(
            [
                ["3,20", "2,40", "0,80"],
                ["6,30", "5,15", "1,15"],
            ],
            row_labels=[
                Text("Iogurte", font_size=20, color=WHITE, font="IBM Plex Sans"),
                Text("Queijo Mussarela", font_size=20, color=WHITE, font="IBM Plex Sans")
            ],
            col_labels=[
                Text("Preço (R$/kg)", font_size=20, color=WHITE, font="IBM Plex Sans"),
                Text("Custos Variáveis (R$/kg)", font_size=20, color=WHITE, font="IBM Plex Sans"),
                Text("Margem (R$/kg)", font_size=20, color=WHITE, font="IBM Plex Sans")
            ],
            top_left_entry=Text("Produto", font_size=20, color=WHITE, font="IBM Plex Sans"),
            include_outer_lines=True,
            h_buff=0.5,
            v_buff=0.3,
            element_to_mobject_config={
                "font_size": 24, 
                "color": WHITE,
                "font": "IBM Plex Sans"  
            }
        ).scale(0.9).next_to(titulo, DOWN, buff=0.3)
        
        texto_intro = Tex(
            r"\raggedright " 
            r"De acordo com os dados da tabela, vamos escrever um modelo matemático simples para resolver o problema",
            font_size=32
        ).to_edge(LEFT, buff=0.5)
        
        texto_variaveis = Tex(
            r"\raggedright " 
            r"Primeiro, definimos as variáveis: \\"
            r"$x_1$ = quantidade de iogurte a ser produzida \\"
            r"$x_2$ = quantidade de queijo a ser produzida",
            font_size=32
        ).next_to(texto_intro, DOWN, aligned_edge=LEFT, buff=0.4)

        texto_fun_obj = Tex(
            r"\raggedright " 
            r"O nosso objetivo é maximizar o lucro total, que é a soma das margens de contribuição unitárias multiplicadas pelas quantidades de cada item: \\",
            font_size=32
        ).next_to(texto_variaveis, DOWN, aligned_edge=LEFT, buff=0.4)

        texto_modelo = Tex(
            r"\raggedright " 
            r"Modelo: \\"
            r"$\text{Max } Z = 0,8x_1 + 1,15x_2$",
            font_size=32
        ).next_to(texto_fun_obj, DOWN, aligned_edge=LEFT, buff=0.4)
        
        grupo = VGroup(titulo, tabela, texto_intro, texto_variaveis, texto_fun_obj, texto_modelo)
        grupo.arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(LEFT, buff=0.5)

        self.play(Write(titulo))
        self.play(Create(tabela))
        self.wait(3)
        self.play(Write(texto_intro, run_time = 3))
        self.play(Write(texto_variaveis, run_time = 4)) 
        self.wait(2)
        self.play(Write(texto_fun_obj, run_time =4))
        margem_col = tabela.get_columns()[3]  
        retangulo_destaque = SurroundingRectangle(
            margem_col,
            color=RED,
            buff=0.1,
            stroke_width=3
        )
        self.play(Create(retangulo_destaque))
        self.wait(3)

        grupo.add(retangulo_destaque)

        self.wait(4)
        self.play(Write(texto_modelo, run_time = 2))
        self.wait(4)
        self.play(FadeOut(grupo))

    def exemplo_fun_obj(self):

        exemplicificacao = Tex(
            r"\raggedright \linespread{1.5}\selectfont " 
            r"Por exemplo, se produzirmos 400 kg de iogurte e 500 kg de queijo, o lucro total será: \\"
            r"$\text{Max } Z = 0,8x_1 + 1,15x_2$ \\"
            r"$Z = 0,8 \times 400 + 1,15 \times 500 = 320 + 575 = 895.00$",
            font_size=32
        ).to_edge(LEFT, buff=0.5).shift(UP*2)
        
        exemplicificacao_restricoes = Tex(
           r"\raggedright \linespread{1.5}\selectfont "
            r"Porém, na prática, existem restrições de produção, como capacidade \\ de produção, demanda, etc.\\",
            r"Encontrar a solução que maximiza o lucro respeitando essas restrições é chamada de solução ótima",
            font_size=32
        ).next_to(exemplicificacao, DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(Write(exemplicificacao, run_time = 8))
        self.wait(1)
        self.play(Write(exemplicificacao_restricoes, run_time = 8))
        self.wait(2)
        self.play(FadeOut(exemplicificacao), FadeOut(exemplicificacao_restricoes))
        
    def tabela02(self):

        explicacao_rest_Materias_primas = Tex(
            r"\raggedright \linespread{1.5}\selectfont " 
            r"Vamos, então, elaborar um modelo simplificado para representar as restrições \\ de capacidade produtiva e demandas mínimas, conforme a tabela abaixo:",
            font_size=32
        ).to_edge(LEFT, buff=0.5).shift(UP*2.5)
        
        tabela = Table(
            [
                ["0,70", "0,16", "0,25", "0,05", "320"],
                ["0,40", "0,32", "0,33", "0,09","450"],
                ["1200", "460", "650", "170", "-"]
            ],
            row_labels=[
                Text("Iogurte", font_size=24, font="IBM Plex Sans"),
                Text("Queijo", font_size=24, font="IBM Plex Sans"),
                Text("Capacidade", font_size=24, font="IBM Plex Sans"),
            ],
            col_labels=[
                Text("Leite (L)", font_size=24, font="IBM Plex Sans"),
                Text("Soro (L)", font_size=24, font="IBM Plex Sans"),
                Text("Gordura (kg)", font_size=24, font="IBM Plex Sans"),
                Text("Mão de obra (h)", font_size=24, font="IBM Plex Sans"),
                Text("Demandas (Kg)", font_size=24, font="IBM Plex Sans")
            ],
            top_left_entry=Text("Produto", font_size=24, font="IBM Plex Sans"),
            include_outer_lines=True,
            h_buff=0.5,
            v_buff=0.3,
            element_to_mobject_config={
                "font_size": 24, 
                "color": WHITE,
                "font": "IBM Plex Sans"  
            }
        ).scale(0.7).next_to(explicacao_rest_Materias_primas, DOWN, buff=0.5)

        onde_texto1 = BulletedList(
            r"\raggedright \fontfamily{IBM Plex Sans}\selectfont Leite, soro e gordura são as matérias-primas utilizadas, enquanto a mão de obra representa o tempo, em horas-homem, necessário para a produção de cada produto;",
            font_size=25,
            buff=0.4
        ).next_to(tabela, DOWN, buff=0.4).to_edge(LEFT)

        onde_texto2 = BulletedList(
            r"\raggedright \fontfamily{IBM Plex Sans}\selectfont Capacidade é a quantidade máxima de cada matéria-prima (Kg) disponível e mão de obra (h);",
            font_size=25,
            buff=0.4
        ).next_to(tabela, DOWN, buff=0.4).to_edge(LEFT)

        complementar_onde_texto2 = Tex(
            r"\raggedright \fontfamily{IBM Plex Sans}\selectfont Vamos agora adicionar a capacidade ao modelo.",
            font_size=25,
        ).next_to(onde_texto2, DOWN, buff=0.2).to_edge(LEFT)

        onde_texto3 = BulletedList(
            r"\raggedright \fontfamily{IBM Plex Sans}\selectfont Demandas (Kg) são as quantidades mínimas de cada produto que devem ser produzidas.",
            font_size=25,
            buff=0.4
        ).next_to(tabela, DOWN, buff=0.4).to_edge(LEFT)

        restricoes = VGroup(
            MathTex(r"Leite (L): 0,70x_1 + 0,40x_2"),
            MathTex(r"Soro (L): 0,16x_1 + 0,32x_2"),
            MathTex(r"Gordura (kg): 0,25x_1 + 0,33x_2"),
            MathTex(r"\text{Mão de Obra (h)}: 0,05x_1 + 0,09x_2")).arrange(DOWN, buff=0.4).scale(0.55).next_to(onde_texto1, DOWN).to_edge(LEFT)
        
        texto_variaveis = Tex(
            r"\raggedright "
            r"$x_1$ = quantidade de iogurte a ser produzida \\"
            r"$x_2$ = quantidade de queijo a ser produzida",
            font_size=32
        ).next_to(restricoes, RIGHT, buff=0.2).shift(RIGHT*1.5+UP*0.6)

        capacidades = VGroup(
            MathTex(r"\leq 1200"),
            MathTex(r"\leq 460"),
            MathTex(r"\leq 650"),
            MathTex(r"\leq 170")).arrange(DOWN, buff=0.6).scale(0.55).next_to(restricoes, RIGHT)
    
        Demanda_modelo = VGroup(
            MathTex(r"\text{Demanda de iogurte: } x_1 \geq 320"),
            MathTex(r"\text{Demanda de queijo: } x_2 \geq 450")).arrange(DOWN, buff=0.5).scale(0.55).next_to(onde_texto3, DOWN).to_edge(LEFT)
               
        self.play(Write(explicacao_rest_Materias_primas, run_time = 5))
        self.wait(1)
        self.play(Create(tabela, run_time = 2))
        self.wait(2)
        self.play(Write(onde_texto1, run_time = 4))

        margem_col = tabela.get_columns()[1:5]
        retangulo_destaque = SurroundingRectangle(
            margem_col,
            color=RED,
            buff=0.1,
            stroke_width=3
        )
        self.play(Create(retangulo_destaque))
        self.wait(3)
        self.play(Write(restricoes, run_time = 5))
        self.wait(2)

        # Criação do retângulo de destaque
        retangulo_destaque_var = SurroundingRectangle(
            texto_variaveis,
            color=RED,
            buff=0.2,
            stroke_width=4
        )

        # Animação
        self.play(
            Write(texto_variaveis),
            Create(retangulo_destaque_var),
            run_time=2
        )
        self.wait(2)
        self.play(FadeOut(retangulo_destaque_var))

        self.play(FadeOut(onde_texto1), FadeOut(retangulo_destaque))
        self.play(Write(onde_texto2, run_time = 4))
        self.wait(2)

        margem_col = tabela.get_rows()[3]  
        retangulo_destaque1 = SurroundingRectangle(
            margem_col,
            color=RED,
            buff=0.05,
            stroke_width=3
        )
        self.play(Create(retangulo_destaque1))
        self.wait(1)
        self.play(Write(complementar_onde_texto2, run_time = 2))
        self.wait(1)
        self.play(Write(capacidades, run_time = 5))
        self.wait(2)
        self.play(FadeOut(onde_texto2), FadeOut(retangulo_destaque1), FadeOut(capacidades), 
                  FadeOut(complementar_onde_texto2), FadeOut(restricoes))
        
        self.play(Write(onde_texto3, run_time = 4))

        margem_col = tabela.get_columns()[5]
        retangulo_destaque2 = SurroundingRectangle(
            margem_col,
            color=RED,
            buff=0.05,
            stroke_width=3
        )
        self.play(Create(retangulo_destaque2))
        self.wait(2)
        self.play(Write(Demanda_modelo, run_time = 5))
        self.wait(2)
        self.play(FadeOut(onde_texto3), FadeOut(retangulo_destaque2), 
                  FadeOut(Demanda_modelo), FadeOut(texto_variaveis), 
                  FadeOut(tabela), FadeOut(explicacao_rest_Materias_primas))

    def modelo(self):

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

        dados = [
            [Text("R1"), MathTex("0.70x_1 + 0.40x_2 = 1200"), Tex("1714.29"), Tex("3000")],
            [Text("R2"), MathTex("0.16x_1 + 0.32x_2 = 460"), Tex("2875"), Tex("1437.5")],
            [Text("R3"), MathTex("0.25x_1 + 0.33x_2 = 650"), Tex("2600"), Tex("1969.7")],
            [Text("R4"), MathTex("0.05x_1 + 0.09x_2 = 170"), Tex("3400"), Tex("1888.9")]]

        # Função de conversão 
        def convert_element(element):
            return element 

        # Criação da tabela
        tabela = Table(
            table=dados,
            col_labels=[
                MathTex("\\text{Retas}"),
                MathTex("\\text{Restrição}"),
                MathTex("\\text{Intercepto } x_1"),
                MathTex("\\text{Intercepto } x_2")
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
            v_buff=0.6,
            h_buff=1.2,
            element_to_mobject=convert_element  
        ).scale(0.6).shift(LEFT*1.0)

        tabela.to_edge(DOWN, buff=0.5)
        self.play(Create(tabela), run_time=2)
        self.wait()

        self.play(FadeOut(restricoes3), FadeOut(restricoes4), FadeOut(tabela))

        restricoes_demanda1 = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"Aplicaremos agora o mesmo procedimento para as restrições de demandas mínimas.", font_size=25
        ).to_edge(LEFT, buff=0.5).shift(UP*3.0)

        restricoes_demanda2 = MathTex(
            r"x_1 \geq 320 \\",
            r"x_2 \geq 450", font_size=25
        ).next_to(restricoes_demanda1, DOWN, aligned_edge=LEFT, buff=0.4)

        restricoes_demanda3 = MathTex(
            r"x_1 &= 320 \\",
            r"x_2 &= 450", font_size=25
        ).next_to(restricoes_demanda2, RIGHT, aligned_edge=LEFT, buff=1.5).shift(RIGHT*1.0)

        seta1 = Arrow(
            start=restricoes_demanda2.get_right(), 
            end=restricoes_demanda3.get_left(),
            buff=0.2,
            color="#77CF7B",
            max_stroke_width_to_length_ratio=5,
            max_tip_length_to_length_ratio=0.5
        )

        self.play(Write(restricoes_demanda1, run_time=2))
        self.wait(1)
        self.play(Write(restricoes_demanda2, run_time=2))
        self.wait(1)
        self.play(Create(seta1))
        self.wait(1)
        self.play(Write(restricoes_demanda3, run_time = 2))
        self.wait(1)

        explicativo = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"Como as restrições de demanda são equações mais diretas, não precisamos fazer a divisão dos coeficientes.\\"
            r"Assim, temos que $x_1 = 320$ e $x_2 = 450$.", 
            font_size=25).next_to(restricoes_demanda2, DOWN, aligned_edge=LEFT, buff=0.5)
        
        dados_final = [
            [Text("R1"), MathTex("0.70x_1 + 0.40x_2 = 1200"), Tex("1714.29"), Tex("3000")],
            [Text("R2"), MathTex("0.16x_1 + 0.32x_2 = 460"), Tex("2875"), Tex("1437.5")],
            [Text("R3"), MathTex("0.25x_1 + 0.33x_2 = 650"), Tex("2600"), Tex("1969.7")],
            [Text("R4"), MathTex("0.05x_1 + 0.09x_2 = 170"), Tex("3400"), Tex("1888.9")],
            [Text("R5"), MathTex("x_1 = 320"), Tex("320"), Tex("0")],
            [Text("R6"), MathTex("x_2 = 450"), Tex("0"), Tex("450")]
        ]

        # Função de conversão 
        def convert_element(element):
            return element 

        # Criação da tabela
        tabela_final = Table(
            table=dados_final,
            col_labels=[
                MathTex("\\text{Retas}"),
                MathTex("\\text{Restrição}"),
                MathTex("\\text{Intercepto } x_1"),
                MathTex("\\text{Intercepto } x_2")
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
            v_buff=0.6,
            h_buff=1.2,
            element_to_mobject=convert_element  
        ).scale(0.4)

        tabela_final.next_to(explicativo,DOWN, buff=0.5).shift(LEFT*1.0)

        self.play(Write(explicativo, run_time = 5))
        self.wait(1)
        self.play(Create(tabela_final), run_time=2)
        self.wait()
