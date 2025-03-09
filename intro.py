from manim import *

class HarumiIntro(Scene):
    def construct(self):
        # Configurações da imagem
        logo_path = r"C:\Users\Mathe\Desktop\Free_Lance\Harumi\Videos\mix_producao\mix_optimization_Video\harumi_logo.png"
        logo = ImageMobject(logo_path).scale(0.9)
        
        # Calcula as proporções do retângulo
        image_width = 102
        image_height = 157
        aspect_ratio = image_width / image_height
        
        # Cria retângulo com as mesmas proporções
        rect = Rectangle(
            width=logo.height * aspect_ratio,  # Mantém proporção baseado na altura da imagem
            height=logo.height,
            color=WHITE,
            stroke_width=10
        )
        rect.move_to(logo.get_center())

        # Texto "HARUMI"
        harumi_text = Text("HARUMI", font_size=40, color=WHITE, font= "IBM Plex Mono")
        harumi_text.next_to(logo, DOWN, buff=0.5)

        # Animação do retângulo
        self.play(
            Create(rect, run_time=2),
            rate_func=rate_functions.ease_in_out_sine
        )

        # Animação de revelação da logo
        self.play(
            FadeIn(logo, run_time=1.5),
            rect.animate.set_stroke(opacity=0),
            lag_ratio=0.5
        )

        # Animação do texto
        self.play(
            Write(harumi_text, run_time=1.5),
            rate_func=rate_functions.ease_in_out_sine
        )

        self.wait(1)