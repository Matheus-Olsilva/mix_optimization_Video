from manim import *

class ProductionMix(Scene):
    def construct(self):
        self.conceitos_mix_producao()
        self.apresentacao_problema()
        self.apresentacao_problema2()
        self.apresentacao_tabela1()
        self.apresentacao_tabela2()
        self.apresentacao_tabela3()
        self.variaveis_decisao()
        self.funcao_objetivo()
        self.restricoes_recursos()
        self.restricoes_demanda()
        self.modelagem_parametros()
        self.modelagem_modelo()

    def conceitos_mix_producao(self):
        titulo = Text(
            "Problema do Mix de Produção", 
            font_size=45, 
            color=BLUE, 
            font="Inter"
        ).to_edge(UP)
        
        conceitos = VGroup(
            Text("Desafios:", font_size=40, color=YELLOW, font="Inter"),
            Tex(r"- Recursos limitados (matérias-primas, mão de obra)", font_size=35),
            Tex(r"- Diversos produtos com características distintas", font_size=35),
            Tex(r"- Restrições operacionais e contratuais", font_size=35),
            
            Text("Objetivos:", font_size=40, color=YELLOW, font="Inter"),
            Tex(r"- Otimização da alocação de recursos", font_size=35),
            Tex(r"- Maximização do lucro total", font_size=35),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).scale(0.9).next_to(titulo, DOWN, buff=0.5)
        
        self.play(Write(titulo))
        self.play(LaggedStart(*[FadeIn(c, shift=RIGHT) for c in conceitos], lag_ratio=0.8))
        self.wait(4)
        self.play(FadeOut(VGroup(titulo, conceitos)))

    def apresentacao_problema(self):
        titulo = Text("Caso Prático: Empresa Naturelat", font_size=40, color=BLUE, font="Inter").to_edge(UP)
        
        texto = Tex(
            r"A empresa Naturelat do setor de laticínios fabrica:\\"
            r"Iogurte, Queijo Minas, Mussarela, Parmesão e Provolone.\\"
            r"Em função de mudanças estratégicas e concorrência,\\"
            r"a empresa precisa redefinir seu mix de produção,\\"
            r"buscando maximizar os lucros dentro dos recursos disponíveis",
            font_size=35
        ).next_to(titulo, DOWN, buff=0.6).move_to(ORIGIN)
        
        self.play(Write(titulo))
        self.play(Write(texto))
        self.wait(10)
        self.play(FadeOut(VGroup(titulo, texto)))

    def apresentacao_problema2(self):
      
        titulo = Text(
            "Informações Comerciais",
            font_size=40,
            color=BLUE,
            font="Inter"
        ).to_edge(UP, buff=1.0)  

      
        texto = Tex(
            r"Devido a razões contratuais, a empresa necessita produzir uma quantidade mínima diária:\\",
            r"320kg de iogurte, 380kg de queijo minas, 450kg de queijo mussarela\\",
            r"240kg de queijo parmesão e 180kg de queijo provolone.\\",
            r"A área comercial da empresa garante que existe mercado para absorver,\\",
            r"qualquer nível de produção, independentemente do produto.",
            font_size=35,
            tex_environment="center" 
        ).next_to(titulo, DOWN, buff=0.8)  

   
        grupo = VGroup(titulo, texto).move_to(ORIGIN)

       
        self.play(Write(titulo))
        self.play(Write(texto))
        self.wait(10)
        self.play(FadeOut(grupo))

    def apresentacao_tabela1(self):
        titulo = Text("Tabela 1: Matérias-primas por kg de produto", font_size=30, color=YELLOW, font="Inter").to_edge(UP)
        
        tabela = Table(
            [
                ["0,70", "0,16", "0,25", "0,05"],
                ["0,40", "0,22", "0,33", "0,12"],
                ["0,40", "0,32", "0,33", "0,09"],
                ["0,60", "0,19", "0,40", "0,04"],
                ["0,60", "0,23", "0,47", "0,16"]
            ],
            row_labels=[
                Text("Iogurte", font_size=24, font="Inter"),
                Text("Queijo Minas", font_size=24, font="Inter"),
                Text("Queijo Mussarela", font_size=24, font="Inter"),
                Text("Queijo Parmesão", font_size=24, font="Inter"),
                Text("Queijo Provolone", font_size=24, font="Inter")
            ],
            col_labels=[
                Text("Leite (L)", font_size=24, font="Inter"),
                Text("Soro (L)", font_size=24, font="Inter"),
                Text("Gordura (kg)", font_size=24, font="Inter"),
                Text("Mão de obra (h)", font_size=24, font="Inter")
            ],
            top_left_entry=Text("Produto", font_size=24, font="Inter"),
            include_outer_lines=True
        ).scale(0.7).move_to(ORIGIN)
        
        self.play(Write(titulo))
        self.play(Create(tabela))
        self.wait(4)
        self.play(FadeOut(VGroup(titulo, tabela)))

    def apresentacao_tabela2(self):
        titulo = Text("Tabela 2: Margem de Contribuição Unitária (R$/kg)", font_size=30, color=YELLOW, font="Inter").to_edge(UP)
        
        tabela = Table(
            [
                ["3,20", "2,40", "0,80"],
                ["4,10", "3,40", "0,70"],
                ["6,30", "5,15", "1,15"],
                ["8,25", "6,95", "1,30"],
                ["7,50", "6,80", "0,70"]
            ],
            row_labels=[
                Text("Iogurte", font_size=24, font="Inter"),
                Text("Queijo Minas", font_size=24, font="Inter"),
                Text("Queijo Mussarela", font_size=24, font="Inter"),
                Text("Queijo Parmesão", font_size=24, font="Inter"),
                Text("Queijo Provolone", font_size=24, font="Inter")
            ],
            col_labels=[
                Text("Preço (R$/kg)", font_size=24, font="Inter"),
                Text("Custos Variáveis (R$/kg)", font_size=24, font="Inter"),
                Text("Margem (R$/kg)", font_size=24, color=YELLOW, font="Inter")
            ],
            top_left_entry=Text("Produto", font_size=24, font="Inter"),
            include_outer_lines=True
        ).scale(0.7).move_to(ORIGIN)
        
        self.play(Write(titulo))
        self.play(Create(tabela))
        self.wait(4)
        self.play(FadeOut(VGroup(titulo, tabela)))

    def apresentacao_tabela3(self):
        titulo = Text("Tabela 3: Capacidades e Demandas", font_size=30, color=YELLOW, font="Inter").to_edge(UP)
        
        tabela = Table(
            [
                ["0,70", "0,16", "0,25", "0,05", "0,80", "320"],
                ["0,40", "0,22", "0,33", "0,12", "0,70", "380"],
                ["0,40", "0,32", "0,33", "0,09", "1,15", "450"],
                ["0,60", "0,19", "0,40", "0,04", "1,30", "240"],
                ["0,60", "0,23", "0,47", "0,16", "0,70", "180"],
                ["1200", "460", "650", "170", "", ""]
            ],
            row_labels=[
                Text("Iogurte", font_size=24, font="Inter"),
                Text("Queijo Minas", font_size=24, font="Inter"),
                Text("Queijo Mussarela", font_size=24, font="Inter"),
                Text("Queijo Parmesão", font_size=24, font="Inter"),
                Text("Queijo Provolone", font_size=24, font="Inter"),
                Text("Capacidade", font_size=24, font="Inter")
            ],
            col_labels=[
                Text("Leite (L)", font_size=24, font="Inter"),
                Text("Soro (L)", font_size=24, font="Inter"),
                Text("Gordura (kg)", font_size=24, font="Inter"),
                Text("Mão de obra (h)", font_size=24, font="Inter"),
                Text("Margem (R$/kg)", font_size=24, font="Inter"),
                Text("Demanda (kg)", font_size=24, font="Inter")
            ],
            top_left_entry=Text("Produto", font_size=24, font="Inter"),
            include_outer_lines=True
        ).scale(0.6).move_to(ORIGIN)
        
        self.play(Write(titulo))
        self.play(Create(tabela))
        self.wait(4)
        self.play(FadeOut(VGroup(titulo, tabela)))

    def variaveis_decisao(self):
        titulo = Text("Variáveis de Decisão", color=YELLOW, font="Inter").to_edge(UP)
        variaveis = VGroup(
            MathTex(r"x_1: \text{Iogurte (kg/dia)}"),
            MathTex(r"x_2: \text{Queijo Minas (kg/dia)}"),
            MathTex(r"x_3: \text{Queijo Mussarela (kg/dia)}"),
            MathTex(r"x_4: \text{Queijo Parmesão (kg/dia)}"),
            MathTex(r"x_5: \text{Queijo Provolone (kg/dia)}")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(titulo, DOWN)
        
        self.play(Write(titulo))
        self.play(LaggedStart(*[Write(v) for v in variaveis], lag_ratio=0.6))
        self.wait(2)
        self.play(FadeOut(VGroup(titulo, variaveis)))

    def funcao_objetivo(self):
        titulo = Text("Função Objetivo: Maximizar Lucro", color=YELLOW, font="Inter").to_edge(UP)
        lucro = MathTex(
            r"\text{Max } Z = 0,80x_1 + 0,70x_2 + 1,15x_3 + 1,30x_4 + 0,70x_5",
            color=WHITE
        ).scale(0.8).next_to(titulo, DOWN)
        
        explicacao = Tex(r"Cada coeficiente representa\\a margem de contribuição\\por quilograma produzido",
                         font_size=28).next_to(lucro, DOWN)
        
        self.play(Write(titulo))
        self.play(Write(lucro))
        self.play(FadeIn(explicacao, shift=UP))
        self.wait(3)
        self.play(FadeOut(VGroup(titulo, lucro, explicacao)))

    def restricoes_recursos(self):
        titulo = Text("Restrições de Recursos", color=YELLOW, font="Inter").to_edge(UP)
        restricoes = VGroup(
            MathTex(r"Leite (L): 0,70x_1 + 0,40x_2 + 0,40x_3 + 0,60x_4 + 0,60x_5 \leq 1200", color=WHITE),
            MathTex(r"Soro (L): 0,16x_1 + 0,22x_2 + 0,32x_3 + 0,19x_4 + 0,23x_5 \leq 460", color=WHITE),
            MathTex(r"Gordura (kg): 0,25x_1 + 0,33x_2 + 0,33x_3 + 0,40x_4 + 0,47x_5 \leq 650", color=WHITE),
            MathTex(r"\text{Mão de Obra (h)}: 0,05x_1 + 0,12x_2 + 0,09x_3 + 0,04x_4 + 0,16x_5 \leq 170", color=WHITE)
        ).arrange(DOWN, buff=0.6).scale(0.6).next_to(titulo, DOWN)
        
        restricoes.move_to(ORIGIN)
        
        self.play(Write(titulo))
        self.play(LaggedStart(*[Write(r) for r in restricoes], lag_ratio=0.5))
        self.wait(3)
        self.play(FadeOut(VGroup(titulo, restricoes)))

    def restricoes_demanda(self):
        titulo = Text("Demandas Mínimas", color=YELLOW, font="Inter").to_edge(UP)
        restricoes = VGroup(
            MathTex(r"\text{Iogurte (Kg)}: x_1 \geq 320", color=WHITE),
            MathTex(r"\text{Queijo Minas (Kg)}: x_2 \geq 380", color=WHITE),
            MathTex(r"\text{Mussarela (Kg)}: x_3 \geq 450", color=WHITE),
            MathTex(r"\text{Parmesão (Kg)}: x_4 \geq 240", color=WHITE),
            MathTex(r"\text{Provolone (Kg)}: x_5 \geq 180", color=WHITE)
        ).arrange(DOWN, buff=0.6).scale(0.8).next_to(titulo, DOWN)
        
        restricoes.move_to(ORIGIN)
        
        self.play(Write(titulo))
        self.play(LaggedStart(*[Write(r) for r in restricoes], lag_ratio=0.5))
        self.wait(2)
        self.play(FadeOut(VGroup(titulo, restricoes)))

    def modelagem_parametros(self):
        titulo_principal = Text("Modelagem Matemática", color=YELLOW, font="Inter").to_edge(UP)
        
        titulo_indices = Text("Índices/Conjuntos", color=BLUE, font="Inter").scale(0.8).next_to(titulo_principal, DOWN, buff=0.5)
        indices = VGroup(
            MathTex(r"I: \{1, \ldots, m\} \quad \text{Conjunto de produtos}"),
            MathTex(r"J: \{1, \ldots, n\} \quad \text{Conjunto de recursos}")
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).scale(0.7).next_to(titulo_indices, DOWN, buff=0.3)
        
        titulo_parametros = Text("Parâmetros", color=BLUE, font="Inter").scale(0.8).next_to(indices, DOWN, buff=0.5)
        parametros = VGroup(
            MathTex(r"l_i: \text{Margem por kg do produto } i \in I"),
            MathTex(r"a_{ij}: \text{Consumo do recurso } j \in J \text{ pelo produto } i \in I"),
            MathTex(r"b_j: \text{Disponibilidade do recurso } j \in J"),
            MathTex(r"d_i: \text{Demanda mínima do produto } i \in I")
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).scale(0.7).next_to(titulo_parametros, DOWN, buff=0.3)
        
        grupo = VGroup(titulo_indices, indices, titulo_parametros, parametros)
        
        self.play(Write(titulo_principal))
        self.play(FadeIn(titulo_indices))
        self.play(LaggedStart(*[Write(i) for i in indices], lag_ratio=0.6))
        self.play(FadeIn(titulo_parametros))
        self.play(LaggedStart(*[Write(p) for p in parametros], lag_ratio=0.6))
        self.wait(4)
        self.play(FadeOut(VGroup(titulo_principal, grupo)))

    def modelagem_modelo(self):
        titulo = Text("Modelo de Otimização", color=YELLOW, font="Inter").to_edge(UP)
        
        modelo = VGroup(
            MathTex(r"\text{Variáveis:} \quad x_i = \text{Quantidade diária do produto } i \in I"),
            MathTex(r"\text{Max } Z = \sum_{i \in I} l_i x_i"),
            MathTex(r"\text{Sujeito a:}"),
            VGroup(
                MathTex(r"\sum_{i \in I} a_{ij} x_i \leq b_j \quad \forall j \in J"),
                MathTex(r"x_i \geq d_i \quad \forall i \in I"),
                MathTex(r"x_i \geq 0 \quad \forall i \in I")
            ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT).scale(0.8).next_to(titulo, DOWN)
        
        modelo[3].shift(RIGHT*0.5)
        
        self.play(Write(titulo))
        self.play(LaggedStart(
            Write(modelo[0]),
            Write(modelo[1]),
            Write(modelo[2]),
            LaggedStart(*[Write(eq) for eq in modelo[3]], lag_ratio=0.5),
            lag_ratio=0.8
        ))
        self.wait(5)
        self.play(FadeOut(VGroup(titulo, modelo)))