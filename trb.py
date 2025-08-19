import turtle

# Classe base
class Figura:
    def __init__(self, cor, tamanho, x, y):
        self.cor = cor
        self.tamanho = tamanho
        self.x = x
        self.y = y

    def mover_para_posicao(self):
        """Reposiciona a tartaruga sem desenhar"""
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()

    def desenhar(self):
        """Método genérico (será sobrescrito pelas subclasses)"""
        raise NotImplementedError("O método desenhar() deve ser sobrescrito!")


# Subclasse Quadrado
class Quadrado(Figura):
    def desenhar(self):
        self.mover_para_posicao()
        turtle.color(self.cor)
        for _ in range(4):
            turtle.forward(self.tamanho)
            turtle.right(90)


# Subclasse Triangulo
class Triangulo(Figura):
    def desenhar(self):
        self.mover_para_posicao()
        turtle.color(self.cor)
        for _ in range(3):
            turtle.forward(self.tamanho)
            turtle.left(120)


# Subclasse Círculo
class Circulo(Figura):
    def desenhar(self):
        self.mover_para_posicao()
        turtle.color(self.cor)
        turtle.circle(self.tamanho)


# Subclasse Hexágono
class Hexagono(Figura):
    def desenhar(self):
        self.mover_para_posicao()
        turtle.color(self.cor)
        for _ in range(6):
            turtle.forward(self.tamanho)
            turtle.right(60)


# ---------- PROGRAMA PRINCIPAL ----------
turtle.speed(3)

# Criando diferentes figuras
figuras = [
    Quadrado("red", 100, -200, 100),
    Triangulo("blue", 120, 0, 0),
    Circulo("green", 60, 200, 0),
    Hexagono("purple", 80, -100, -200)
]

# Desenhar todas
for figura in figuras:
    figura.desenhar()

turtle.done()
