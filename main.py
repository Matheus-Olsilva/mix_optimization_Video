from manim import *
# Esta classe é a principal que executa ambas as animações sequencialmente
class MixProducaoCompleto(Scene):
    def construct(self):
        self.camera.background_color = "#000000"
        config.frame_width = 12
        config.frame_height = 8
        
        # ========== PRIMEIRA PARTE: ProductionMix ==========
        # Utilizamos os métodos diretamente aqui, em vez de criar uma instância
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
        
        # Transição entre as duas partes
        self.wait(1)
        
        # ========== SEGUNDA PARTE: GraficoOtimizacao ==========
        # Configurar o título e definição
        titulo_calculos = Text("Cálculo dos Vértices da Região Viável", font="IBM Plex Sans", font_size=35).set_color(WHITE)
        titulo_calculos.to_edge(UP, buff=0.5).shift(LEFT*1.0)
        self.play(Write(titulo_calculos), run_time=1.5)
        
        # Definição do Teorema Fundamental da Programação Linear
        definicao = Text("O Teorema Fundamental da Programação Linear afirma que, se existir uma", 
                         font="IBM Plex Sans", font_size=24).set_color(WHITE)
        definicao2 = Text("solução ótima para um problema de programação linear, ela estará em",
                         font="IBM Plex Sans", font_size=24).set_color(WHITE)
        
        cor_vertices = "#605CEA"
        um_dos = Text("um dos ", font="IBM Plex Sans", font_size=24).set_color(WHITE)
        vertices_text = Text("vértices", font="IBM Plex Sans", font_size=24).set_color(cor_vertices)
        da_regiao = Text(" da região viável.", font="IBM Plex Sans", font_size=24).set_color(WHITE)
        
        linha_modificada = VGroup(um_dos, vertices_text, da_regiao).arrange(RIGHT, buff=0.2)
        
        grupo_definicao = VGroup(definicao, definicao2, linha_modificada).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        grupo_definicao.next_to(titulo_calculos, DOWN, buff=0.5)
        
        self.play(Write(definicao), run_time=2)
        self.play(Write(definicao2), run_time=2)
        self.play(Write(um_dos), run_time=0.8)
        self.play(Write(vertices_text), run_time=1, rate_func=rate_functions.linear)
        self.play(Write(da_regiao), run_time=1.2)
        self.play(Indicate(vertices_text, color="#605CEA", scale_factor=1.2))
        self.wait(2)
        
        # Calcular vértices (usando os métodos da classe original)
        self.calcular_vertice_320_450(grupo_definicao)
        self.calcular_vertice_1457_450(grupo_definicao)
        self.calcular_vertice_1250_812(grupo_definicao)
        self.calcular_vertice_320_1277(grupo_definicao)
        
        # Limpar tela e mostrar tabela final
        self.clear()
        self.mostrar_tabela_funcao_objetivo()
        
        self.wait(3)
        
    # ============ INCLUINDO MÉTODOS DE ProductionMix ============
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

        # Use MathTex em vez de Tex para melhor renderização das equações
        restricoes = VGroup(
            MathTex(r"Leite(L) : 0,70x_1 + 0,40x_2"),
            MathTex(r"Soro(L) : 0,16x_1 + 0,32x_2"),
            MathTex(r"Gordura(kg) : 0,25x_1 + 0,33x_2"),
            MathTex(r"\text{Mão de Obra (h)} : 0,05x_1 + 0,09x_2")
        ).arrange(DOWN, buff=0.4).scale(0.55).next_to(onde_texto1, DOWN).to_edge(LEFT)
        
        # Aqui está a parte que garante o alinhamento - agrupamos os símbolos ≤ como um MathTex único
        capacidades = VGroup(
            MathTex(r"&\leq 1200"),
            MathTex(r"&\leq 460"),
            MathTex(r"&\leq 650"),
            MathTex(r"&\leq 170")
        ).arrange(DOWN, buff=0.4).scale(0.55)
        
        # Posicionamento preciso para alinhar com as expressões anteriores
        for i, cap in enumerate(capacidades):
            cap.next_to(restricoes[i], RIGHT, buff=0.1)
        
        texto_variaveis = Tex(
            r"\raggedright "
            r"$x_1$ = quantidade de iogurte a ser produzida \\"
            r"$x_2$ = quantidade de queijo a ser produzida",
            font_size=32
        ).next_to(restricoes, RIGHT, buff=0.2).shift(RIGHT*1.5+UP*0.6)
    
        Demanda_modelo = VGroup(
            MathTex(r"\text{Demanda de iogurte: } x_1 \geq 320"),
            MathTex(r"\text{Demanda de queijo: } x_2 \geq 450")
        ).arrange(DOWN, buff=0.5).scale(0.55).next_to(onde_texto3, DOWN).to_edge(LEFT)
               
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
        ).next_to(restricoes, DOWN, aligned_edge=LEFT, buff=0.3)

        self.play(Write(metodo_grafico, run_time=5))
        self.play(FadeOut(metodo_grafico))

        resolucao = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"Consideraremos as inequações como equações e as representaremos graficamente por meio de retas nos eixos $x_1$ e $x_2$. Vamos agora encontrar interseções em $x_1$ e $x_2$",
            font_size=25
        ).next_to(restricoes, DOWN, aligned_edge=LEFT, buff=0.3)


        restricoes2 = MathTex(
            r"""
            0.70x_1 + 0.40x_2 &= 1200 \\
            0.16x_1 + 0.32x_2 &= 460 \\
            0.25x_1 + 0.33x_2 &= 650 \\
            0.05x_1 + 0.09x_2 &= 170
            """,
            font_size=25
        ).next_to(resolucao, DOWN, aligned_edge=LEFT, buff=0.3)

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
        ).next_to(resolucao, DOWN, aligned_edge=LEFT, buff=0.3)

        restricoes4 = MathTex(r"0.25x_1 + 0.33x_2 &= 650\\",
            r"\quad \text{Para } x_1 = 0 &\rightarrow 0.33x_2 = 650 \rightarrow x_2 = 1969.7\\",
            r"\quad \text{Para } x_2 = 0 &\rightarrow 0.25x_1 = 650 \rightarrow x_1 = 2600\\",
            r"0.05x_1 + 0.09x_2 &= 170\\",
            r"\quad \text{Para } x_1 = 0 &\rightarrow 0.09x_2 = 170 \rightarrow x_2 = 1888.9\\",
            r"\quad \text{Para } x_2 = 0 &\rightarrow 0.05x_1 = 170 \rightarrow x_1 = 3400", font_size=25
        ).next_to(restricoes3, RIGHT, aligned_edge=LEFT, buff=0.3).shift(RIGHT*3.0)

        
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
        self.clear()

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
                ([390, 3500], [550, 3500]),
                ([390, 3350], [550, 3350]),
                ([390, 3200], [550, 3200]),
                ([390, 3050], [550, 3050]),
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
                ([2710, 550], [2710, 800]),
                ([2800, 550], [2800, 800]),
                ([2900, 550], [2900, 800]),
                ([3000, 550], [3000, 800]),
                ([3100, 550], [3100, 800]),
                ([3200, 550], [3200, 800]),
                ([3300, 550], [3300, 800]),
                ([3400, 550], [3400, 800]),
                ([3500, 550], [3500, 800]),
                ([3600, 550], [3600, 800]),
                ([3700, 550], [3700, 800]),
                ([3800, 550], [3800, 800]),
                ([3900, 550], [3900, 800]),
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
        
        # Efeito sutil de destaque
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
        explicacao = Tex(r"As setas sinalizam o sentido das \\ desigualdades em cada restrição, \\ apontando a região de solução", 
                        font_size=30).next_to(legend, LEFT, buff=1.0).shift(UP*1)
        self.play(Write(explicacao, run_time=2))
        self.wait(4)
        
        # Fade out mais elegante
        self.play(
            FadeOut(explicacao, shift=UP*0.2),
            FadeOut(all_arrows, lag_ratio=0.04, scale=0.9),
            run_time=1.5
        )

        # Interseções relevantes
        intersections = [
            ((320, 450), ["R5", "R6"]),
            ((1457.14, 450), ["R1", "R6"]),
            ((1250, 812.5), ["R1", "R2"]),
            ((320, 1277.5), ["R2", "R5"])
        ]

        # Criação dos destaques
        intersection_dots = VGroup()
        intersection_labels = VGroup()
        for point, labels in intersections:
            x, y = point
            dot = Dot(axes.coords_to_point(x, y), color=YELLOW, radius=0.1)
            label = MathTex(f"{{{', '.join(labels)}}}", font_size=30, color=WHITE).next_to(dot, UP, buff=0.2)
            intersection_dots.add(dot)
            intersection_labels.add(label)

        # Animação dos destaques
        self.play(
            LaggedStartMap(GrowFromCenter, intersection_dots, lag_ratio=0.2),
            LaggedStartMap(FadeIn, intersection_labels, shift=UP, lag_ratio=0.2),
            run_time=3
        )
        self.wait(1)

        # Região viável
        feasible_region = Polygon(
            axes.coords_to_point(320, 450),
            axes.coords_to_point(1457.14, 450),
            axes.coords_to_point(1250, 812.5),
            axes.coords_to_point(320, 1277.5),
            fill_color=BLUE,
            fill_opacity=0.3,
            stroke_opacity=0  # Remove borda branca
        )

        # Linhas recortadas
        clipped_lines = VGroup(
            Line(axes.coords_to_point(1457.14, 450), axes.coords_to_point(1250, 812.5), color=RED),
            Line(axes.coords_to_point(1250, 812.5), axes.coords_to_point(320, 1277.5), color=GREEN),
            Line(axes.coords_to_point(320, 450), axes.coords_to_point(320, 1277.5), color=PURPLE),
            Line(axes.coords_to_point(320, 450), axes.coords_to_point(1457.14, 450), color=ORANGE)
        )

        # Remoção de linhas não-essenciais e seus pontos
        non_boundary_indices = [2, 3]  # R3 e R4
        non_boundary_lines = VGroup(*[lines_and_equations[i][0] for i in non_boundary_indices])
        non_boundary_dots = VGroup(*[all_line_dots[i] for i in non_boundary_indices])

        self.play(
            FadeOut(non_boundary_lines),
            FadeOut(non_boundary_dots),  
            run_time=1.5
        )

        # Transição para região viável
        original_line_indices = [0, 1, 4, 5]  # R1, R2, R5, R6
        original_lines = VGroup(*[lines_and_equations[i][0] for i in original_line_indices])
        original_dots = VGroup(*[all_line_dots[i] for i in original_line_indices])

        self.play(
            FadeOut(original_lines),
            FadeOut(original_dots),  
            Create(clipped_lines),
            FadeIn(feasible_region),
            run_time=2
        )

        # Explicação final
        explicacao_regiao = Tex(r"A região viável indica o espaço de solução,\\que satisfaz todas as restrições", 
                                font_size=24).next_to(legend, LEFT, buff=0.5).shift(LEFT*1)
        arrow5 = Arrow(explicacao_regiao.get_center() + DOWN*0.5, feasible_region.get_center(), 
                      color="#605CEA", buff=0, max_stroke_width_to_length_ratio=5,
                      max_tip_length_to_length_ratio=0.3)

        self.play(Write(explicacao_regiao, run_time=2))
        self.play(Create(arrow5))
        self.wait(6)
        self.play(FadeOut(explicacao_regiao), FadeOut(arrow5))
        self.clear()

    # ============ INCLUINDO MÉTODOS DE GraficoOtimizacao ============
    
    def criar_eixos(self):
        # Configuração do gráfico
        axes = Axes(
            x_range=[0, 4000, 1000],
            y_range=[0, 3500, 1000],
            x_length=4,  # Reduzindo ainda mais o tamanho
            y_length=3,  # Reduzindo ainda mais o tamanho
            axis_config={
                "include_numbers": True,
                "font_size": 20,
            },
        )
        axes.add_coordinates()
        return axes
    
    def criar_restricoes(self, axes):
        # Definição das restrições
        restricoes = [
            {
                "linha": Line(
                    axes.coords_to_point(1714.29, 0),
                    axes.coords_to_point(0, 3000),
                    color=RED
                ),
                "nome": "R1",
                "equacao": "0.70x_1 + 0.40x_2 \\leq 1200",
                "interceptos": [(1714.29, 0), (0, 3000)]
            },
            {
                "linha": Line(
                    axes.coords_to_point(2875, 0),
                    axes.coords_to_point(0, 1437.5),
                    color=GREEN
                ),
                "nome": "R2",
                "equacao": "0.16x_1 + 0.32x_2 \\leq 460",
                "interceptos": [(2875, 0), (0, 1437.5)]
            },
            {
                "linha": Line(
                    axes.coords_to_point(2600, 0),
                    axes.coords_to_point(0, 1969.7),
                    color=BLUE
                ),
                "nome": "R3",
                "equacao": "0.25x_1 + 0.33x_2 \\leq 650",
                "interceptos": [(2600, 0), (0, 1969.7)]
            },
            {
                "linha": Line(
                    axes.coords_to_point(3400, 0),
                    axes.coords_to_point(0, 1888.9),
                    color=YELLOW
                ),
                "nome": "R4",
                "equacao": "0.05x_1 + 0.09x_2 \\leq 170",
                "interceptos": [(3400, 0), (0, 1888.9)]
            },
            {
                "linha": Line(
                    axes.coords_to_point(320, 0),
                    axes.coords_to_point(320, 3500),
                    color=PURPLE
                ),
                "nome": "R5",
                "equacao": "x_1 \\geq 320",
                "interceptos": [(320, 0)]
            },
            {
                "linha": Line(
                    axes.coords_to_point(0, 450),
                    axes.coords_to_point(4000, 450),
                    color=ORANGE
                ),
                "nome": "R6",
                "equacao": "x_2 \\geq 450",
                "interceptos": [(0, 450)]
            },
        ]
        return restricoes
    
    def criar_regiao_viavel(self, axes):
        # Região viável
        feasible_region = Polygon(
            axes.coords_to_point(320, 450),
            axes.coords_to_point(1457.14, 450),
            axes.coords_to_point(1250, 812.5),
            axes.coords_to_point(320, 1277.5),
            fill_color=BLUE,
            fill_opacity=0.3,
            stroke_opacity=0
        )
        
        # Linhas recortadas para o contorno da região viável
        clipped_lines = VGroup(
            Line(axes.coords_to_point(1457.14, 450), axes.coords_to_point(1250, 812.5), color=RED),
            Line(axes.coords_to_point(1250, 812.5), axes.coords_to_point(320, 1277.5), color=GREEN),
            Line(axes.coords_to_point(320, 450), axes.coords_to_point(320, 1277.5), color=PURPLE),
            Line(axes.coords_to_point(320, 450), axes.coords_to_point(1457.14, 450), color=ORANGE)
        )
        
        return feasible_region, clipped_lines
    
    def criar_grafico_com_destaque(self, ponto, titulo_ponto):
        # Criar um gráfico com destaque para o ponto específico
        axes = self.criar_eixos()
        restricoes = self.criar_restricoes(axes)
        feasible_region, clipped_lines = self.criar_regiao_viavel(axes)
        
        # Componentes básicos do gráfico (sem o ponto)
        grafico_base = VGroup(axes, feasible_region, clipped_lines)
        
        # Criar o ponto destacado
        x, y = ponto
        ponto_destacado = Dot(axes.coords_to_point(x, y), color=YELLOW, radius=0.1)  # Ponto MENOR
        
        # Criando uma label para o ponto
        label = MathTex(f"({x}, {y})", font_size=24, color=WHITE).next_to(ponto_destacado, UR, buff=0.1)
        
        # Retornar os componentes separadamente
        return grafico_base, ponto_destacado, label
    
    def calcular_vertice_320_450(self, grupo_definicao):
        # Título mostrando apenas as retas que se cruzam
        titulo = Text("Interseção de R5 e R6", font="IBM Plex Sans", font_size=25, color="#FFFFFF")
        
        calculos = VGroup(
            MathTex(r"\text{Interseção direta das restrições de demanda:}", font_size=28, color="#FFFFFF"),
            MathTex(r"\text{Definido por } x_1 = 320 \text{ e } x_2 = 450", font_size=28, color="#FFFFFF"),
            MathTex(r"\text{Solução: } (320, 450)", font_size=30, color="#FFFFFF")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        # Agrupar o título e os cálculos
        grupo_direita = VGroup(titulo, calculos).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        grupo_direita.scale(1.0).to_edge(RIGHT, buff=1.0)
        
        # Criar gráfico para o ponto (320, 450)
        grafico_base, ponto_destacado, label = self.criar_grafico_com_destaque(ponto=(320, 450), titulo_ponto="Vértice (320; 450)")
        
        # Criar grupo gráfico para animação
        grafico = VGroup(grafico_base, ponto_destacado, label)
        grafico_grupo = grafico.scale(1.0).to_edge(LEFT, buff=1.5)
        
        # Ambos os grupos devem ser posicionados abaixo do grupo de definição
        grafico_grupo.next_to(grupo_definicao, DOWN, buff=0.5).shift(LEFT*3)
        grupo_direita.next_to(grupo_definicao, DOWN, buff=0.5).align_to(grafico_grupo, UP).shift(RIGHT*3)
        
        # Animação
        self.play(Write(titulo), run_time=2)
        
        # Mostrar primeiro o gráfico completo, mas sem o ponto
        self.play(Create(grafico_base), run_time=2)
        
        # Animar cada linha do cálculo individualmente com Write
        for linha in calculos:
            self.play(Write(linha), run_time=1.5)
        
        # Mostrar o ponto do vértice após o cálculo estar completo
        self.play(
            Create(ponto_destacado),
            Write(label),
            run_time=1.5
        )
        
        # Destaque adicional para o ponto
        destaque = Circumscribe(ponto_destacado, color=YELLOW, time_width=2, run_time=2, stroke_width=5)
        self.play(destaque)
        
        self.wait(2)
        self.play(
            FadeOut(grupo_direita), 
            FadeOut(grafico_grupo),
            # Não remover grupo_definicao, ele permanece na tela
        )
    
    def calcular_vertice_1457_450(self, grupo_definicao):
        # Título mostrando apenas as retas que se cruzam
        titulo = Text("Interseção de R1 e R6", font="IBM Plex Sans", font_size=25, color="#FFFFFF")
        
        calculos = VGroup(
            MathTex(r"\text{Interseção de R1 com } x_2 = 450\text{:}", font_size=28, color="#FFFFFF"),
            MathTex(r"0.70x_1 + 0.40 \cdot 450 = 1200", font_size=28, color="#FFFFFF"),
            MathTex(r"0.70x_1 = 1020", font_size=28, color="#FFFFFF"),
            MathTex(r"x_1 = \frac{1020}{0.70} \approx 1457.14", font_size=28, color="#FFFFFF"),
            MathTex(r"\text{Solução: } (1457.14, 450)", font_size=30, color="#FFFFFF")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        # Agrupar o título e os cálculos
        grupo_direita = VGroup(titulo, calculos).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        grupo_direita.scale(1.0).to_edge(RIGHT, buff=1.0)
        
        # Criar gráfico para o ponto (1457.14, 450)
        grafico_base, ponto_destacado, label = self.criar_grafico_com_destaque(ponto=(1457.14, 450), titulo_ponto="Vértice (1457.14; 450)")
        
        # Criar grupo gráfico para animação
        grafico = VGroup(grafico_base, ponto_destacado, label)
        grafico_grupo = grafico.scale(1.0).to_edge(LEFT, buff=1.5)
        
        # Ambos os grupos devem ser posicionados abaixo do grupo de definição
        grafico_grupo.next_to(grupo_definicao, DOWN, buff=0.5).shift(LEFT*3)
        grupo_direita.next_to(grupo_definicao, DOWN, buff=0.5).align_to(grafico_grupo, UP).shift(RIGHT*3)
        
        # Animação
        self.play(Write(titulo), run_time=2)
        
        # Mostrar primeiro o gráfico completo, mas sem o ponto
        self.play(Create(grafico_base), run_time=2)
        
        # Animar cada linha do cálculo individualmente com Write
        for linha in calculos:
            self.play(Write(linha), run_time=1.0)
        
        # Mostrar o ponto do vértice após o cálculo estar completo
        self.play(
            Create(ponto_destacado),
            Write(label),
            run_time=1.5
        )
        
        self.play(Circumscribe(ponto_destacado, color=YELLOW, time_width=2, run_time=2, stroke_width=5))
        
        self.wait(2)
        self.play(
            FadeOut(grupo_direita), 
            FadeOut(grafico_grupo),
            # Não remover grupo_definicao, ele permanece na tela
        )
    
    def calcular_vertice_1250_812(self, grupo_definicao):
        # Título mostrando apenas as retas que se cruzam
        titulo = Text("Interseção de R1 e R2", font="IBM Plex Sans", font_size=25, color="#FFFFFF")
        
        calculos = VGroup(
            MathTex(r"\text{Interseção de R1 e R2:}", font_size=28, color="#FFFFFF"),
            MathTex(r"0.70x_1 + 0.40x_2 = 1200", font_size=28, color="#FFFFFF"),
            MathTex(r"0.16x_1 + 0.32x_2 = 460", font_size=28, color="#FFFFFF"),
            MathTex(r"\text{Multiplicar a segunda equação por 1.25:}", font_size=28, color="#FFFFFF"),
            MathTex(r"0.20x_1 + 0.40x_2 = 575", font_size=28, color="#FFFFFF"),
            MathTex(r"\text{Subtrair da primeira: } 0.50x_1 = 625", font_size=28, color="#FFFFFF"),
            MathTex(r"x_1 = 1250", font_size=28, color="#FFFFFF"),
            MathTex(r"\text{Substituir em R2: } 0.16 \cdot 1250 + 0.32x_2 = 460", font_size=28, color="#FFFFFF"),
            MathTex(r"x_2 = 812.5", font_size=28, color="#FFFFFF"),
            MathTex(r"\text{Solução: } (1250, 812.5)", font_size=30, color="#FFFFFF")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Agrupar o título e os cálculos
        grupo_direita = VGroup(titulo, calculos).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        grupo_direita.scale(0.9).to_edge(RIGHT, buff=1.0)
        
        # Criar gráfico para o ponto (1250, 812.5)
        grafico_base, ponto_destacado, label = self.criar_grafico_com_destaque(ponto=(1250, 812.5), titulo_ponto="Vértice (1250; 812.5)")
        
        # Criar grupo gráfico para animação
        grafico = VGroup(grafico_base, ponto_destacado, label)
        grafico_grupo = grafico.scale(1.0).to_edge(LEFT, buff=1.5)
        
        # Ambos os grupos devem ser posicionados abaixo do grupo de definição
        grafico_grupo.next_to(grupo_definicao, DOWN, buff=0.5).shift(LEFT*3)
        grupo_direita.next_to(grupo_definicao, DOWN, buff=0.5).align_to(grafico_grupo, UP).shift(RIGHT*3)
        
        # Animação
        self.play(Write(titulo), run_time=2)
        
        # Mostrar primeiro o gráfico completo, mas sem o ponto
        self.play(Create(grafico_base), run_time=2)
        
        # Animar cada linha do cálculo individualmente com Write
        for linha in calculos:
            self.play(Write(linha), run_time=0.7)
        
        # Mostrar o ponto do vértice após o cálculo estar completo
        self.play(
            Create(ponto_destacado),
            Write(label),
            run_time=1.5
        )
        
        # Destaque das equações em uso
        destaques = [
            Indicate(calculos[1], color=RED, scale_factor=1.2),  # R1
            Indicate(calculos[2], color=GREEN, scale_factor=1.2)  # R2
        ]
        
        self.play(AnimationGroup(*destaques, lag_ratio=0.5))
        self.play(Circumscribe(ponto_destacado, color=YELLOW, time_width=2, run_time=2, stroke_width=5))
        
        self.wait(2)
        self.play(
            FadeOut(grupo_direita), 
            FadeOut(grafico_grupo),
            # Não remover grupo_definicao, ele permanece na tela
        )
    
    def calcular_vertice_320_1277(self, grupo_definicao):
        # Título mostrando apenas as retas que se cruzam
        titulo = Text("Interseção de R2 e R5", font="IBM Plex Sans", font_size=25, color="#FFFFFF")
        
        calculos = VGroup(
            MathTex(r"\text{Interseção de R2 com } x_1 = 320\text{:}", font_size=28, color="#FFFFFF"),
            MathTex(r"0.16 \cdot 320 + 0.32x_2 = 460", font_size=28, color="#FFFFFF"),
            MathTex(r"51.2 + 0.32x_2 = 460", font_size=28, color="#FFFFFF"),
            MathTex(r"0.32x_2 = 408.8", font_size=28, color="#FFFFFF"),
            MathTex(r"x_2 = \frac{408.8}{0.32} = 1277.5", font_size=28, color="#FFFFFF"),
            MathTex(r"\text{Solução: } (320, 1277.5)", font_size=30, color="#FFFFFF")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        # Agrupar o título e os cálculos
        grupo_direita = VGroup(titulo, calculos).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        grupo_direita.scale(1.0).to_edge(RIGHT, buff=1.0)
        
        # Criar gráfico para o ponto (320, 1277.5)
        grafico_base, ponto_destacado, label = self.criar_grafico_com_destaque(ponto=(320, 1277.5), titulo_ponto="Vértice (320; 1277.5)")
        
        # Criar grupo gráfico para animação
        grafico = VGroup(grafico_base, ponto_destacado, label)
        grafico_grupo = grafico.scale(1.0).to_edge(LEFT, buff=1.5)
        
        # Ambos os grupos devem ser posicionados abaixo do grupo de definição
        grafico_grupo.next_to(grupo_definicao, DOWN, buff=0.5).shift(LEFT*3)
        grupo_direita.next_to(grupo_definicao, DOWN, buff=0.5).align_to(grafico_grupo, UP).shift(RIGHT*3)
        
        # Animação
        self.play(Write(titulo), run_time=2)
        
        # Mostrar primeiro o gráfico completo, mas sem o ponto
        self.play(Create(grafico_base), run_time=2)
        
        # Animar cada linha do cálculo individualmente com Write
        for linha in calculos:
            self.play(Write(linha), run_time=1.0)
        
        # Mostrar o ponto do vértice após o cálculo estar completo
        self.play(
            Create(ponto_destacado),
            Write(label),
            run_time=1.5
        )
        
        self.play(Circumscribe(ponto_destacado, color=YELLOW, time_width=2, run_time=2, stroke_width=5))
        
        self.wait(2)
        self.play(
            FadeOut(grupo_direita), 
            FadeOut(grafico_grupo),
            FadeOut(grupo_definicao)  # Agora sim, removemos a definição antes da tabela final
        )
        
    def mostrar_tabela_funcao_objetivo(self):
        # Título da tabela
        titulo_tabela = Text("Comparação dos Valores na Função Objetivo", font="IBM Plex Sans", font_size=25, color="#FFFFFF")
        titulo_tabela.to_edge(UP, buff=0.5)
        
        # Definir a função objetivo - usando MathTex
        funcao_objetivo = MathTex(r"\text{Função Objetivo: Maximizar } Z = 0{,}8x_1 + 1{,}15x_2", font_size=34, color="#77CF7B")  # Alterado para verde
        funcao_objetivo.next_to(titulo_tabela, DOWN, buff=0.5).to_edge(LEFT, buff=0.7)
        
        # Recalcular os valores da função objetivo com a nova fórmula
        # Usando a fórmula Z = 0,8x₁ + 1,15x₂ (com vírgula, não ponto)
        # Para cálculos em Python, convertemos a vírgula para ponto
        vertices = [
            (320, 450, 0.8*320 + 1.15*450),
            (1457.14, 450, 0.8*1457.14 + 1.15*450),
            (1250, 812.5, 0.8*1250 + 1.15*812.5),
            (320, 1277.5, 0.8*320 + 1.15*1277.5)
        ]
        
        # Encontrar o maior valor de Z
        max_z_value = max(vertices, key=lambda x: x[2])
        max_z_index = vertices.index(max_z_value)
        
        # Criar a tabela com MathTex
        tabela = VGroup()
        
        # Cabeçalho
        cabecalho = VGroup(
            MathTex(r"\text{\textbf{Vértice }} (x_1, x_2)", font_size=34),
            MathTex(r"\text{\textbf{Valor de }} Z", font_size=34)
        ).arrange(RIGHT, buff=2.5)
        tabela.add(cabecalho)
        
        # Linhas
        for i, (x, y, z) in enumerate(vertices):
            if i == max_z_index:
                cor = "#77CF7B"  # Alterado para verde
            else:
                cor = WHITE
                
            linha = VGroup(
                MathTex(f"({x}, {y})", font_size=30, color=cor),
                MathTex(f"{z:.2f}", font_size=30, color=cor)
            ).arrange(RIGHT, buff=2.5)
            
            # Alinhar com o cabeçalho
            linha[0].align_to(cabecalho[0], LEFT)
            linha[1].align_to(cabecalho[1], LEFT)
            
            tabela.add(linha)
        
        # Organizar as linhas verticalmente e colocar toda a tabela mais à esquerda
        tabela.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        tabela.next_to(funcao_objetivo, DOWN, buff=0.7).to_edge(LEFT, buff=0.7)
        
        # Adicionar uma caixa em torno da tabela
        box = SurroundingRectangle(tabela, color=WHITE, buff=0.3)
        
        # Criar o gráfico final com tamanho reduzido
        axes = self.criar_eixos()
        feasible_region, clipped_lines = self.criar_regiao_viavel(axes)
        
        # Grupo do gráfico
        grafico_base = VGroup(axes, feasible_region, clipped_lines)
        grafico_base.scale(0.75)  # Reduzir ainda mais o tamanho
        
        # Criar o ponto destacado
        x_opt, y_opt, z_opt = max_z_value
        ponto_destacado = Dot(axes.coords_to_point(x_opt, y_opt), color="#77CF7B", radius=0.1)  # Alterado para verde e menor
        
        # Criando uma label para o ponto
        label = MathTex(f"({x_opt}, {y_opt})", font_size=18, color=WHITE).next_to(ponto_destacado, UR, buff=0.1)
        
        # Adicionar tudo ao grupo do gráfico
        grafico_final = VGroup(grafico_base, ponto_destacado, label)
        
        # Criar os textos de solução ótima com MathTex
        titulo_otimo = MathTex(r"\text{Solução Ótima}", font_size=28, color=WHITE)
        valor_otimo = MathTex(f"Z = {z_opt:.2f}", font_size=28, color="#77CF7B")  # Alterado para verde
        
        # Posicionamento da solução ótima e do gráfico
        solucao_grupo = VGroup(titulo_otimo, valor_otimo).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Posicionar o gráfico à direita da tabela, mas não muito longe
        grafico_grupo = VGroup(solucao_grupo, grafico_final)
        grafico_grupo.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        grafico_grupo.next_to(box, RIGHT, buff=1.0)
        
        # Ajustar a posição para não sair da tela
        if grafico_grupo.get_right()[0] > config.frame_width - 0.5:
            grafico_grupo.align_to(config.frame_width - 0.5, RIGHT)
        
        # Animação
        self.play(Write(titulo_tabela), run_time=2)
        self.play(Write(funcao_objetivo), run_time=2)
        self.play(
            Create(box),
            Write(cabecalho),
            run_time=2
        )
        
        # Mostrar cada linha da tabela uma por uma
        for i in range(1, len(tabela)):
            self.play(Write(tabela[i]), run_time=2)
        
        # Animar a solução ótima e o gráfico
        self.play(Write(titulo_otimo), run_time=2)
        self.play(Write(valor_otimo), run_time=2)
        self.play(Create(grafico_final), run_time=2)
        
        # Destaque para o valor máximo
        destaque_max = Circumscribe(
            tabela[max_z_index + 1], 
            color="#77CF7B",  
            time_width=2, 
            run_time=2, 
            stroke_width=5
        )
        self.play(destaque_max)
        
        # Destaque para o ponto ótimo no gráfico
        destaque_ponto = Circumscribe(
            ponto_destacado, 
            color="#77CF7B",  
            time_width=2, 
            run_time=2, 
            stroke_width=5
        )
        self.play(destaque_ponto)
        
        self.wait(3)