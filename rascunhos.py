from manim import *

class GraficoOtimizacao(Scene):
    def construct(self):
        # Configurar o background e frame
        self.camera.background_color = "#000000"
        config.frame_width = 12
        config.frame_height = 8
        
        # Configuração global da fonte
        Text.set_default(font="IBM Plex Sans")
        
        # Título dos cálculos
        titulo_calculos = Text("Cálculo dos Vértices da Região Viável", font="IBM Plex Sans", font_size=35).set_color(WHITE)
        titulo_calculos.to_edge(UP, buff=0.5).shift(LEFT*1.0)
        self.play(Write(titulo_calculos), run_time=1.5)
        
        # Calcular e mostrar cada vértice com o gráfico correspondente
        self.calcular_vertice_320_450()
        self.calcular_vertice_1457_450()
        self.calcular_vertice_1250_812()
        self.calcular_vertice_320_1277()
        
        # # Mostrar a tabela com os valores dos pontos na função objetivo
        self.mostrar_tabela_funcao_objetivo()
        
        # Fade out do título principal no final
        self.play(FadeOut(titulo_calculos))
        
        self.wait(3)
    
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
        
        # Grupo do gráfico
        grafico = VGroup(axes, feasible_region, clipped_lines)
        
        # Criar o ponto destacado
        x, y = ponto
        ponto_destacado = Dot(axes.coords_to_point(x, y), color=YELLOW, radius=0.12)
        
        # Criando uma label para o ponto
        label = MathTex(f"({x}, {y})", font_size=20, color=WHITE).next_to(ponto_destacado, UR, buff=0.1)
        
        # Título do gráfico (agora como parte do grupo)
        titulo_grafico = Text(titulo_ponto, font="IBM Plex Sans", font_size=24, color=WHITE)
        titulo_grafico.next_to(grafico, UP, buff=0.2)
        
        # Adicionando tudo ao grupo
        grupo_grafico = VGroup(grafico, ponto_destacado, label)
        
        return grupo_grafico, titulo_grafico
    
    def calcular_vertice_320_450(self):
        # Título e cálculos do primeiro vértice
        titulo = Text("Vértice (320; 450)", font="IBM Plex Sans", font_size=25, color=WHITE).shift(LEFT*2.0)
        
        calculos = VGroup(
            MathTex(r"\text{Interseção direta das restrições de demanda:}", font_size=25),
            MathTex(r"\text{Definido por } x_1 = 320 \text{ e } x_2 = 450", font_size=25),
            MathTex(r"\text{Solução: } (320, 450)", font_size=25, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Posicionar todos os elementos à esquerda com mais espaço
        grupo_esquerda = VGroup(titulo, calculos).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        grupo_esquerda.to_edge(LEFT, buff=1.7).shift(LEFT*1.5)
        
        # Criar gráfico para o ponto (320, 450)
        grafico, titulo_grafico = self.criar_grafico_com_destaque(ponto=(320, 450), titulo_ponto="Vértice (320; 450)")
        
        # Colocar o título do gráfico acima do grupo esquerda
        titulo_grafico.next_to(grafico, UP, buff=0.2)
        
        # Posicionar o gráfico à direita
        grafico_grupo = VGroup(titulo_grafico, grafico)
        grafico_grupo.to_edge(RIGHT, buff=0.9).shift(DOWN*0.2)
        
        # Animação
        self.play(Write(titulo), run_time=1.5)
        self.play(LaggedStartMap(FadeIn, calculos, lag_ratio=0.2), run_time=2)
        self.play(FadeIn(titulo_grafico), Create(grafico), run_time=2)
        
        # Destaque adicional para o ponto
        destaque = Circumscribe(grafico[1], color=YELLOW, time_width=2, run_time=2, stroke_width=5)
        self.play(destaque)
        
        self.wait(2)
        self.play(FadeOut(grupo_esquerda), FadeOut(grafico_grupo))
    
    def calcular_vertice_1457_450(self):
        # Título e cálculos do segundo vértice
        titulo = Text("Vértice (1457.14; 450)", font="IBM Plex Sans", font_size=25, color=WHITE)
        
        calculos = VGroup(
            MathTex(r"\text{Interseção de R1 com } x_2 = 450\text{:}", font_size=25),
            MathTex(r"0.70x_1 + 0.40 \cdot 450 = 1200", font_size=25),
            MathTex(r"0.70x_1 = 1020", font_size=25),
            MathTex(r"x_1 = \frac{1020}{0.70} \approx 1457.14", font_size=25),
            MathTex(r"\text{Solução: } (1457.14, 450)", font_size=25, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Posicionar todos os elementos à esquerda com mais espaço
        grupo_esquerda = VGroup(titulo, calculos).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        grupo_esquerda.to_edge(LEFT, buff=1.7).shift(LEFT*1.5)
        
        # Criar gráfico para o ponto (1457.14, 450)
        grafico, titulo_grafico = self.criar_grafico_com_destaque(ponto=(1457.14, 450), titulo_ponto="Vértice (1457.14; 450)")
        
        # Colocar o título do gráfico acima do grupo esquerda
        titulo_grafico.next_to(grafico, UP, buff=0.2)
        
        # Posicionar o gráfico à direita
        grafico_grupo = VGroup(titulo_grafico, grafico)
        grafico_grupo.to_edge(RIGHT, buff=0.9).shift(DOWN*0.2)
        
        # Animação
        self.play(Write(titulo), run_time=1.5)
        self.play(LaggedStartMap(FadeIn, calculos, lag_ratio=0.2), run_time=2)
        self.play(FadeIn(titulo_grafico), Create(grafico), run_time=2)
        self.play(Circumscribe(grafico[1], color=YELLOW, time_width=2, run_time=2, stroke_width=5))
        
        self.wait(2)
        self.play(FadeOut(grupo_esquerda), FadeOut(grafico_grupo))
    
    def calcular_vertice_1250_812(self):
        # Título e cálculos do terceiro vértice
        titulo = Text("Vértice (1250; 812.5)", font="IBM Plex Sans", font_size=25, color=WHITE)
        
        calculos = VGroup(
            MathTex(r"\text{Interseção de R1 e R2:}", font_size=25),
            MathTex(r"0.70x_1 + 0.40x_2 = 1200", font_size=25),
            MathTex(r"0.16x_1 + 0.32x_2 = 460", font_size=25),
            MathTex(r"\text{Multiplicar a segunda equação por 1.25:}", font_size=25),
            MathTex(r"0.20x_1 + 0.40x_2 = 575", font_size=25),
            MathTex(r"\text{Subtrair da primeira: } 0.50x_1 = 625", font_size=25),
            MathTex(r"x_1 = 1250", font_size=25),
            MathTex(r"\text{Substituir em R2: } 0.16 \cdot 1250 + 0.32x_2 = 460", font_size=25),
            MathTex(r"x_2 = 812.5", font_size=25),
            MathTex(r"\text{Solução: } (1250, 812.5)", font_size=25, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        
        # Posicionar todos os elementos à esquerda com mais espaço
        grupo_esquerda = VGroup(titulo, calculos).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        grupo_esquerda.to_edge(LEFT, buff=1.7).shift(LEFT*1.5)
        
        # Ajustar a escala para caber tudo na tela
        grupo_esquerda.scale(0.9)
        
        # Criar gráfico para o ponto (1250, 812.5)
        grafico, titulo_grafico = self.criar_grafico_com_destaque(ponto=(1250, 812.5), titulo_ponto="Vértice (1250; 812.5)")
        
        # Colocar o título do gráfico acima do grupo esquerda
        titulo_grafico.next_to(grafico, UP, buff=0.2)
        
        # Posicionar o gráfico à direita
        grafico_grupo = VGroup(titulo_grafico, grafico)
        grafico_grupo.to_edge(RIGHT, buff=0.7).shift(DOWN*0.2)
        
        # Animação
        self.play(Write(titulo), run_time=1.5)
        self.play(LaggedStartMap(FadeIn, calculos, lag_ratio=0.2), run_time=3)
        self.play(FadeIn(titulo_grafico), Create(grafico), run_time=2)
        
        # Destaque das equações em uso
        destaques = [
            Indicate(calculos[1], color=RED, scale_factor=1.2),  # R1
            Indicate(calculos[2], color=GREEN, scale_factor=1.2)  # R2
        ]
        
        self.play(AnimationGroup(*destaques, lag_ratio=0.5))
        self.play(Circumscribe(grafico[1], color=YELLOW, time_width=2, run_time=2, stroke_width=5))
        
        self.wait(2)
        self.play(FadeOut(grupo_esquerda), FadeOut(grafico_grupo))
    
    def calcular_vertice_320_1277(self):
        # Título e cálculos do quarto vértice
        titulo = Text("Vértice (320; 1277.5)", font="IBM Plex Sans", font_size=25, color=WHITE)
        
        calculos = VGroup(
            MathTex(r"\text{Interseção de R2 com } x_1 = 320\text{:}", font_size=25),
            MathTex(r"0.16 \cdot 320 + 0.32x_2 = 460", font_size=25),
            MathTex(r"51.2 + 0.32x_2 = 460", font_size=25),
            MathTex(r"0.32x_2 = 408.8", font_size=25),
            MathTex(r"x_2 = \frac{408.8}{0.32} = 1277.5", font_size=25),
            MathTex(r"\text{Solução: } (320, 1277.5)", font_size=25, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Posicionar todos os elementos à esquerda com mais espaço
        grupo_esquerda = VGroup(titulo, calculos).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        grupo_esquerda.to_edge(LEFT, buff=1.7).shift(LEFT*1.5)
        
        # Criar gráfico para o ponto (320, 1277.5)
        grafico, titulo_grafico = self.criar_grafico_com_destaque(ponto=(320, 1277.5), titulo_ponto="Vértice (320; 1277.5)")
        
        # Colocar o título do gráfico acima do grupo esquerda
        titulo_grafico.next_to(grafico, UP, buff=0.2)
        
        # Posicionar o gráfico à direita
        grafico_grupo = VGroup(titulo_grafico, grafico)
        grafico_grupo.to_edge(RIGHT, buff=0.7).shift(DOWN*0.2)
        
        # Animação
        self.play(Write(titulo), run_time=1.5)
        self.play(LaggedStartMap(FadeIn, calculos, lag_ratio=0.2), run_time=2)
        self.play(FadeIn(titulo_grafico), Create(grafico), run_time=2)
        self.play(Circumscribe(grafico[1], color=YELLOW, time_width=2, run_time=2, stroke_width=5))
        
        self.wait(2)
        self.play(FadeOut(grupo_esquerda), FadeOut(grafico_grupo))

        
    def mostrar_tabela_funcao_objetivo(self):
        # Título da tabela
        titulo_tabela = Text("Comparação dos Valores na Função Objetivo", font="IBM Plex Sans", font_size=35)
        titulo_tabela.to_edge(UP, buff=0.5)
        
        # Definir a função objetivo - usando MathTex
        funcao_objetivo = MathTex(r"\text{Função Objetivo: Maximizar } Z = 0{,}8x_1 + 1{,}15x_2", font_size=34, color=GOLD)
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
                cor = GOLD
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
        ponto_destacado = Dot(axes.coords_to_point(x_opt, y_opt), color=YELLOW, radius=0.1)
        
        # Criando uma label para o ponto
        label = MathTex(f"({x_opt}, {y_opt})", font_size=18, color=WHITE).next_to(ponto_destacado, UR, buff=0.1)
        
        # Adicionar tudo ao grupo do gráfico
        grafico_final = VGroup(grafico_base, ponto_destacado, label)
        
        # Criar os textos de solução ótima com MathTex
        titulo_otimo = MathTex(r"\text{Solução Ótima}", font_size=28, color=WHITE)
        valor_otimo = MathTex(f"Z = {z_opt:.2f}", font_size=28, color=WHITE)
        
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
        self.play(Write(titulo_tabela), run_time=1.5)
        self.play(Write(funcao_objetivo), run_time=1.5)
        self.play(
            Create(box),
            Write(cabecalho),
            run_time=2
        )
        
        # Mostrar cada linha da tabela uma por uma
        for i in range(1, len(tabela)):
            self.play(FadeIn(tabela[i]), run_time=0.5)
        
        self.play(FadeIn(solucao_grupo), Create(grafico_final), run_time=2)
        
        # Destaque para o valor máximo
        destaque_max = Circumscribe(
            tabela[max_z_index + 1], 
            color=GOLD, 
            time_width=2, 
            run_time=2, 
            stroke_width=5
        )
        self.play(destaque_max)
        
        # Destaque para o ponto ótimo no gráfico
        destaque_ponto = Circumscribe(
            ponto_destacado, 
            color=GOLD, 
            time_width=2, 
            run_time=2, 
            stroke_width=5
        )
        self.play(destaque_ponto)
        
        self.wait(3)