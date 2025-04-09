from manim import *

class ConclusaoMixProducao(Scene):
    def construct(self):
        self.camera.background_color = "#000000"
        config.frame_width = 12
        config.frame_height = 8
        
        # Definir os valores ótimos
        x1_otimo = 1250  # kg de iogurte
        x2_otimo = 812.5  # kg de queijo
        lucro_otimo = 0.8 * x1_otimo + 1.15 * x2_otimo  # R$1,934.38
        
        # Plano de coordenadas movido para cima e à esquerda
        axes = Axes(
            x_range=[0, 2000, 500],
            y_range=[0, 1500, 500],
            x_length=5.5,
            y_length=3.5,
            axis_config={"color": BLUE_E, "include_tip": True}
        ).scale(0.8).to_edge(LEFT, buff=1.8).shift(UP*1.0)
        
        # Ponto ótimo no plano
        ponto_otimo = Dot(axes.coords_to_point(x1_otimo, x2_otimo), color="#77CF7B", radius=0.1)
        
        # Linhas tracejadas do ponto aos eixos
        linha_x = DashedLine(
            start=axes.coords_to_point(x1_otimo, x2_otimo),
            end=axes.coords_to_point(x1_otimo, 0),
            color=BLUE_E, 
            stroke_width=2
        )
        
        linha_y = DashedLine(
            start=axes.coords_to_point(x1_otimo, x2_otimo),
            end=axes.coords_to_point(0, x2_otimo),
            color=BLUE_E, 
            stroke_width=2
        )
        
        # Rótulos dos eixos no fim de cada eixo
        label_x = MathTex("x_1", color=WHITE).next_to(axes.coords_to_point(2000, 0), RIGHT, buff=0.2).set_opacity(0.8)
        label_y = MathTex("x_2", color=WHITE).next_to(axes.coords_to_point(0, 1500), UP, buff=0.2).set_opacity(0.8)
        
        # Valores nos eixos
        valor_x = MathTex(f"{x1_otimo}", color="#77CF7B").next_to(linha_x, DOWN, buff=0.2)
        valor_y = MathTex(f"{x2_otimo}", color="#77CF7B").next_to(linha_y, LEFT, buff=0.2)
        
        # Região viável simplificada (trapézio)
        regiao_viavel = Polygon(
            axes.coords_to_point(320, 450),
            axes.coords_to_point(1457.14, 450),
            axes.coords_to_point(1250, 812.5),
            axes.coords_to_point(320, 1277.5),
            fill_color=BLUE_E,
            fill_opacity=0.2,
            stroke_color=BLUE_D,
            stroke_width=1.5
        )
        
        # Textos à direita - movidos para cima
        text_box = Rectangle(
            width=6, 
            height=3, 
            fill_color=BLACK,
            fill_opacity=0,  # Transparente 
            stroke_width=0
        ).to_edge(RIGHT, buff=0.8).shift(UP*1.5)
        
        # Textos de conclusão - movidos para cima
        texto_intro = Text(
            "Para maximizar o lucro,", 
            font="IBM Plex Sans", 
            font_size=32, 
            color=WHITE
        )
        
        texto_otimo = Text(
            "a empresa deve produzir:", 
            font="IBM Plex Sans", 
            font_size=32, 
            color=WHITE
        )
        
        texto_intro_grupo = VGroup(texto_intro, texto_otimo).arrange(DOWN, aligned_edge=LEFT)
        texto_intro_grupo.move_to(text_box).align_to(text_box, UP)
        
        # Valores de produção
        texto_prod1 = Text("• ", font_size=32, color="#77CF7B")
        texto_valor1 = Text(f"1250 kg", font="IBM Plex Sans", font_size=30, color="#77CF7B")
        texto_desc1 = Text(" de iogurte", font="IBM Plex Sans", font_size=30, color=WHITE)
        prod1_grupo = VGroup(texto_prod1, texto_valor1, texto_desc1).arrange(RIGHT, buff=0.1)
        
        texto_prod2 = Text("• ", font_size=32, color="#77CF7B")
        texto_valor2 = Text(f"812.5 kg", font="IBM Plex Sans", font_size=30, color="#77CF7B")
        texto_desc2 = Text(" de queijo", font="IBM Plex Sans", font_size=30, color=WHITE)
        prod2_grupo = VGroup(texto_prod2, texto_valor2, texto_desc2).arrange(RIGHT, buff=0.1)
        
        # Posicionar os grupos de produção
        VGroup(prod1_grupo, prod2_grupo).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        prod1_grupo.next_to(texto_otimo, DOWN, buff=0.4).align_to(texto_otimo, LEFT)
        prod2_grupo.next_to(prod1_grupo, DOWN, buff=0.3).align_to(prod1_grupo, LEFT)
        
        # Função objetivo - Reposicionada abaixo do gráfico
        funcao_obj = MathTex(
            "Z = 0{,}8x_1 + 1{,}15x_2", 
            font_size=32, 
            color=WHITE
        ).next_to(axes, DOWN, buff=0.5).shift(DOWN*0.5+LEFT*1)
        
        # Cálculo do lucro - Posicionado verticalmente abaixo da função objetivo
        eq1 = MathTex(
            "Z = 0{,}8 \\times 1250 + 1{,}15 \\times 812{,}5", 
            font_size=30, 
            color=WHITE
        ).next_to(funcao_obj, DOWN, buff=0.4)
        
        eq2 = MathTex(
            "Z = 1000 + 934{,}38", 
            font_size=30, 
            color=WHITE
        ).next_to(eq1, DOWN, buff=0.3)
        
        lucro_final = MathTex(
            "Z = 1934{,}38", 
            font_size=42, 
            color="#77CF7B"
        ).next_to(eq2, DOWN, buff=0.3)
        
        # Texto do lucro diário - REPOSICIONADO para se alinhar com o texto à direita
        lucro_texto = Text(
            "Gerando um lucro diário de", 
            font="IBM Plex Sans", 
            font_size=30,
            color=WHITE
        )
        
        lucro_valor = Text(
            "R$ 1934.38", 
            font="IBM Plex Sans", 
            font_size=30,
            color="#77CF7B"
        )
        
        # Agora vamos garantir que o grupo de lucro esteja abaixo dos textos de produção
        # e alinhado com eles, não sobre o gráfico
        lucro_grupo = VGroup(lucro_texto, lucro_valor).arrange(DOWN, buff=0.5)
        lucro_grupo.next_to(prod2_grupo, DOWN, buff=1.0).align_to(prod2_grupo, LEFT).shift(DOWN*0.8)
        
        # Destaque para o valor do lucro
        destaque_box = SurroundingRectangle(
            lucro_valor, 
            color=BLUE, 
            buff=0.2, 
            corner_radius=0.1,
            stroke_width=3
        )
         
        # Animar a construção apenas dos elementos, sem o título
        self.play(Create(axes), run_time=1.5)
        self.play(
            Write(label_x),
            Write(label_y),
            run_time=1.0
        )
        self.play(FadeIn(ponto_otimo, scale=1.2), run_time=0.8)
        self.play(
            Create(linha_x),
            Create(linha_y),
            run_time=1.5
        )
        self.play(
            Write(valor_x),
            Write(valor_y),
            run_time=1
        )
        
        # Revelação da região viável
        self.play(
            DrawBorderThenFill(regiao_viavel),
            run_time=1.5
        )
        
        # Primeiro mostrar a área para texto (invisível), depois os textos em sequência
        self.play(
            FadeIn(text_box),
            run_time=0.5
        )
        
        self.play(Write(texto_intro), run_time=1)
        self.play(Write(texto_otimo), run_time=1)
        
        # Animar os valores emergindo do gráfico
        self.play(
            TransformFromCopy(valor_x, texto_valor1),
            FadeIn(texto_prod1),
            FadeIn(texto_desc1),
            run_time=1.5
        )
        
        self.play(
            TransformFromCopy(valor_y, texto_valor2),
            FadeIn(texto_prod2),
            FadeIn(texto_desc2),
            run_time=1.5
        )
        
        # Mostrando a função objetivo e o cálculo em sequência
        self.play(Write(funcao_obj), run_time=1.5)
        self.play(Write(eq1), run_time=1.5)
        self.play(Write(eq2), run_time=1.5)
        self.play(Write(lucro_final), run_time=1.5)
        
        # Animação para transferir o resultado para a conclusão
        self.play(
            TransformFromCopy(lucro_final, lucro_valor),
            FadeIn(lucro_texto, shift=UP*0.3),
            run_time=2
        )
        
        # Adiciona o destaque com animação de pulsação
        self.play(Create(destaque_box), run_time=1)
        self.play(
            destaque_box.animate.scale(1.1).set_stroke(width=4),
            lucro_valor.animate.scale(1.05),
            rate_func=there_and_back_with_pause,
            run_time=2
        )
        
        
        self.wait(3)
        
        # Grupos para fade out
        grupo_grafico = VGroup(
            axes, ponto_otimo, linha_x, linha_y, 
            label_x, label_y, valor_x, valor_y, 
            regiao_viavel, funcao_obj, eq1, eq2, lucro_final
        )
        
        grupo_texto = VGroup(
            text_box, texto_intro_grupo,
            prod1_grupo, prod2_grupo,
            lucro_grupo, destaque_box
        )
        
        # Fade out em sequência
        self.play(FadeOut(grupo_grafico), run_time=1.5)
        self.play(FadeOut(grupo_texto), run_time=1.5)