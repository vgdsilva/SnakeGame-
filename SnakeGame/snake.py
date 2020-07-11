# Game Snake in Python
# by Vinicius

import turtle
import time
import random

delay = 0.1

#Score
score = 0
high_score = 0

# Screen
wn = turtle.Screen()
wn.title('SnakeGame') #Titulo
wn.bgcolor('green') #cor de fundo da tela
wn.setup(width= 600, height= 600) #tamanho da tela
wn.tracer(0) #retira as atualizações da tela

# Snake Head
head = turtle.Turtle() #crianção do modelo turtle
head.speed(0) #animação do modelo turtle
head.shape('square') #modelo da cabeça
head.color('black') #cor da cabeça
head.penup() # para nao desenhar nada
head.goto(0,0) #local da tela que inicia
head.direction = 'stop' #como estara o modelo quando inicia

# Apple
food = turtle.Turtle() #crianção do modelo turtle
food.speed(0) #animação do modelo turtle
food.shape('circle') #modelo da comida
food.color('red') #cor da cabeça
food.penup() # para nao desenhar nada
food.goto(0,100) #local da tela que inicia

# Segments = lista e cada lista = Turtle
segments = []

# Pen
pen = turtle.Turtle() # Crianção do modelo turtle
pen.speed(0) # velocidade da animação turtle
pen.shape('square') # modelo do turtle
pen.color('white') #Cor do turtle
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Score: 0  High Score: 0', align='center', font=('Courier', 18, 'normal'))

# Funções
def go_up():
    if head.direction != 'down':
        head.direction = 'up' #mostra a direção que ira

def go_down():
    if head.direction != 'up':
        head.direction = 'down' #mostra a direção que ira

def go_left():
    if head.direction != 'right':
        head.direction = 'left' #mostra a direção que ira

def go_right():
    if head.direction != 'left':
        head.direction = 'right' #mostra a direção que ira

def move():
    if head.direction == "up": #calcula as coordenadas para a direção
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down": #calcula as coordenadas para a direção
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left": #calcula as coordenadas para a direção
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right": #calcula as coordenadas para a direção
        x = head.xcor()
        head.setx(x + 20)

# Movimentação pelo teclado
wn.listen()
wn.onkeypress(go_up, 'w')
wn.onkeypress(go_down, 's')
wn.onkeypress(go_left, 'a')
wn.onkeypress(go_right, 'd')

# Main game loop
while True:
    wn.update()

    # Check colisão com a borda
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = 'stop'

        # Esconder os segmentos
        for segment in segments:
            segment.goto(1000, 1000)

        # Limpar a lista de segmentos
        segments.clear()

        # Reseta o placar
        score = 0
        
        pen.clear()
        pen.write('Score: {}  High Score: {}'.format(score, high_score), align='center', font=('Courier', 18, 'normal'))

    # check a colisão entre a cobra e a maça
    if head.distance(food) < 20:
        #Move a comida para uma posição aleatoria
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # adciona um segmento
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('grey')
        new_segment.penup()
        segments.append(new_segment)

        #Shorten the deplay
        deplay = 0.001

        # Aumentar o placar
        score += 10

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write('Score: {}  High Score: {}'.format(score, high_score), align='center', font=('Courier', 18, 'normal'))

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    # Mover segmento 0 ate onde a cabeça da cobra esta
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # Check colisão entre a cabeça da cobra e os segmentos do corpo
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'stop'

            # Esconder os segmentos
            for segment in segments:
                segment.goto(1000, 1000)

            # Limpar a lista de segmentos
            segments.clear()

            # Reseta o placar
            score = 0

            # Reseta o delay
            delay = 0.1
        
            pen.clear()
            pen.write('Score: {}  High Score: {}'.format(score, high_score), align='center', font=('Courier', 18, 'normal'))

    time.sleep(delay)

wn.mainloop() #manter a tela aberta