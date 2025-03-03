from manim import *

class ProductionMix(Scene):
    def construct(self):
        self.conceitos_mix_producao()
        self.apresentacao_problema()
        self.apresentacao_tabela1()
        self.apresentacao_tabela2()
        self.apresentacao_tabela3()
        self.variaveis_decisao()
        self.funcao_objetivo()
        self.restricoes_recursos()
        self.restricoes_demanda()
        self.modelo_completo()
        self.conclusao()

    def conceitos_mix_producao(self):
        titulo = Text("Problema do Mix de Produção", 
                     font_size=45, color=BLUE).to_edge(UP)
        
        conceitos = VGroup(
            Text("Desafios:", font_size=30, color=YELLOW),
            Tex(r"- Recursos limitados (matérias-primas, mão de obra)", 
                font_size=28),
            Tex(r"- Diversos produtos com características distintas", 
                font_size=28),
            Tex(r"- Restrições operacionais e contratuais", 
                font_size=28),
            
            Text("Objetivos:", font_size=30, color=YELLOW),
            Tex(r"- Otimização da alocação de recursos", 
                font_size=28),
            Tex(r"- Maximização do lucro total", 
                font_size=28),
            
            Tex(r"Programação linear: \textit{Ferramenta matemática para tomada de decisão ótima}", 
                color=GREEN, font_size=28)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).scale(0.9).next_to(titulo, DOWN, buff=0.5)
        
        self.play(Write(titulo))
        self.play(LaggedStart(*[FadeIn(c, shift=RIGHT) for c in conceitos], lag_ratio=0.8))
        self.wait(4)
        self.play(FadeOut(VGroup(titulo, conceitos)))

    def apresentacao_problema(self):
        titulo = Text("Caso Prático: Empresa Naturelat", font_size=40, color=BLUE).to_edge(UP)
        
        texto = Tex(
            r"A empresa Naturelat do setor de laticínios fabrica:\\"
            r"Iogurte, Queijo Minas, Mussarela, Parmesão e Provolone\\"
            r"Em função de mudanças estratégicas e concorrência,\\"
            r"a empresa precisa redefinir seu mix de produção",
            font_size=30
        ).next_to(titulo, DOWN, buff=0.5)
        
        self.play(Write(titulo))
        self.play(Write(texto))
        self.wait(5)
        self.play(FadeOut(VGroup(titulo, texto)))

    def apresentacao_tabela1(self):
        titulo = Text("Tabela 1: Matérias-primas por kg de produto", font_size=30, color=YELLOW).to_edge(UP)
        
        tabela = Table(
            [
                ["0,70", "0,16", "0,25", "0,05"],
                ["0,40", "0,22", "0,33", "0,12"],
                ["0,40", "0,32", "0,33", "0,09"],
                ["0,60", "0,19", "0,40", "0,04"],
                ["0,60", "0,23", "0,47", "0,16"]
            ],
            row_labels=[
                Text("Iogurte", font_size=24),
                Text("Queijo Minas", font_size=24),
                Text("Queijo Mussarela", font_size=24),
                Text("Queijo Parmesão", font_size=24),
                Text("Queijo Provolone", font_size=24)
            ],
            col_labels=[
                Text("Leite (L)", font_size=24),
                Text("Soro (L)", font_size=24),
                Text("Gordura (kg)", font_size=24),
                Text("Mão de obra (h)", font_size=24)
            ],
            top_left_entry=Text("Produto", font_size=24),
            include_outer_lines=True
        ).scale(0.7).move_to(ORIGIN)
        
        self.play(Write(titulo))
        self.play(Create(tabela))
        self.wait(4)
        self.play(FadeOut(VGroup(titulo, tabela)))

    def apresentacao_tabela2(self):
        titulo = Text("Tabela 2: Margem de Contribuição Unitária (R$/kg)", font_size=30, color=YELLOW).to_edge(UP)
        
        tabela = Table(
            [
                ["3,20", "2,40", "0,80"],
                ["4,10", "3,40", "0,70"],
                ["6,30", "5,15", "1,15"],
                ["8,25", "6,95", "1,30"],
                ["7,50", "6,80", "0,70"]
            ],
            row_labels=[
                Text("Iogurte", font_size=24),
                Text("Queijo Minas", font_size=24),
                Text("Queijo Mussarela", font_size=24),
                Text("Queijo Parmesão", font_size=24),
                Text("Queijo Provolone", font_size=24)
            ],
            col_labels=[
                Text("Preço (R$/kg)", font_size=24),
                Text("Custos Variáveis (R$/kg)", font_size=24),
                Text("Margem (R$/kg)", font_size=24, color=YELLOW)
            ],
            top_left_entry=Text("Produto", font_size=24),
            include_outer_lines=True
        ).scale(0.7).move_to(ORIGIN)
        
        self.play(Write(titulo))
        self.play(Create(tabela))
        self.wait(4)
        self.play(FadeOut(VGroup(titulo, tabela)))

    def apresentacao_tabela3(self):
        titulo = Text("Tabela 3: Capacidades e Demandas", font_size=30, color=YELLOW).to_edge(UP)
        
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
                Text("Iogurte", font_size=24),
                Text("Queijo Minas", font_size=24),
                Text("Queijo Mussarela", font_size=24),
                Text("Queijo Parmesão", font_size=24),
                Text("Queijo Provolone", font_size=24),
                Text("Capacidade", font_size=24, color=RED)
            ],
            col_labels=[
                Text("Leite (L)", font_size=24),
                Text("Soro (L)", font_size=24),
                Text("Gordura (kg)", font_size=24),
                Text("Mão de obra (h)", font_size=24),
                Text("Margem (R$/kg)", font_size=24, color=YELLOW),
                Text("Demanda (kg)", font_size=24, color=GREEN)
            ],
            top_left_entry=Text("Produto", font_size=24),
            include_outer_lines=True
        ).scale(0.6).move_to(ORIGIN)
        
        self.play(Write(titulo))
        self.play(Create(tabela))
        self.wait(4)
        self.play(FadeOut(VGroup(titulo, tabela)))

    def variaveis_decisao(self):
        titulo = Text("Variáveis de Decisão", color=YELLOW).to_edge(UP)
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
        titulo = Text("Função Objetivo: Maximizar Lucro", color=YELLOW).to_edge(UP)
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
        titulo = Text("Restrições de Recursos", color=YELLOW).to_edge(UP)
        restricoes = VGroup(
            MathTex(r"0,70x_1 + 0,40x_2 + 0,40x_3 + 0,60x_4 + 0,60x_5 \leq 1200", color=BLUE),
            MathTex(r"0,16x_1 + 0,22x_2 + 0,32x_3 + 0,19x_4 + 0,23x_5 \leq 460", color=GREEN),
            MathTex(r"0,25x_1 + 0,33x_2 + 0,33x_3 + 0,40x_4 + 0,47x_5 \leq 650", color=ORANGE),
            MathTex(r"0,05x_1 + 0,12x_2 + 0,09x_3 + 0,04x_4 + 0,16x_5 \leq 170", color=PURPLE)
        ).arrange(DOWN, buff=0.3).scale(0.6).next_to(titulo, DOWN)
        
        legendas = VGroup(
            Text("Leite (L)", color=BLUE, font_size=24),
            Text("Soro (L)", color=GREEN, font_size=24),
            Text("Gordura (kg)", color=ORANGE, font_size=24),
            Text("Mão de Obra (h)", color=PURPLE, font_size=24)
        ).arrange(DOWN, buff=0.5).next_to(restricoes, RIGHT, buff=1)
        
        self.play(Write(titulo))
        self.play(LaggedStart(*[Write(r) for r in restricoes], lag_ratio=0.5))
        self.play(Write(legendas))
        self.wait(3)
        self.play(FadeOut(VGroup(titulo, restricoes, legendas)))

    def restricoes_demanda(self):
        titulo = Text("Demandas Mínimas", color=YELLOW).to_edge(UP)
        restricoes = VGroup(
            MathTex(r"x_1 \geq 320", color=WHITE),
            MathTex(r"x_2 \geq 380", color=WHITE),
            MathTex(r"x_3 \geq 450", color=WHITE),
            MathTex(r"x_4 \geq 240", color=WHITE),
            MathTex(r"x_5 \geq 180", color=WHITE)
        ).arrange(DOWN, buff=0.4).scale(0.8).next_to(titulo, DOWN)
        
        legenda = VGroup(
            Text("x₁ = Iogurte", font_size=24),
            Text("x₂ = Queijo Minas", font_size=24),
            Text("x₃ = Mussarela", font_size=24),
            Text("x₄ = Parmesão", font_size=24),
            Text("x₅ = Provolone", font_size=24)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).next_to(restricoes, RIGHT, buff=2)
        
        self.play(Write(titulo))
        self.play(LaggedStart(*[Write(r) for r in restricoes], lag_ratio=0.5))
        self.play(FadeIn(legenda, shift=LEFT))
        self.wait(2)
        self.play(FadeOut(VGroup(titulo, restricoes, legenda)))

    def modelo_completo(self):
        titulo = Text("Modelo de Programação Linear", color=YELLOW).to_edge(UP)
        modelo = VGroup(
            MathTex(r"\text{Max } Z = \sum_{i=1}^5 c_i x_i"),
            MathTex(r"\text{Sujeito a:}"),
            MathTex(r"\sum_{i=1}^5 a_{ij} x_i \leq b_j \quad \forall j \in \text{Recursos}"),
            MathTex(r"x_i \geq d_i \quad \forall i \in \text{Produtos}"),
            MathTex(r"x_i \geq 0")
        ).arrange(DOWN, buff=0.4).scale(0.8).next_to(titulo, DOWN)
        
        explicacoes = VGroup(
            Tex(r"$c_i$: Margem de contribuição do produto $i$", font_size=28),
            Tex(r"$a_{ij}$: Consumo do recurso $j$ por produto $i$", font_size=28),
            Tex(r"$b_j$: Disponibilidade do recurso $j$", font_size=28),
            Tex(r"$d_i$: Demanda mínima do produto $i$", font_size=28)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).next_to(modelo, RIGHT, buff=2)
        
        self.play(Write(titulo))
        self.play(LaggedStart(*[Write(m) for m in modelo], lag_ratio=0.5))
        self.play(FadeIn(explicacoes, shift=LEFT))
        self.wait(3)
        self.play(FadeOut(VGroup(titulo, modelo, explicacoes)))

    def conclusao(self):
        mensagem = Text("A programação linear permite encontrar\n"
                       "a combinação ótima de produção\n"
                       "que maximiza o lucro respeitando\n"
                       "todas as restrições operacionais!",
                       font_size=30, color=WHITE)
        
        self.play(Write(mensagem))
        self.wait(4)