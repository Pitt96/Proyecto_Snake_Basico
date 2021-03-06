#instale la libreria pygame para la musica: pip install pygame
import turtle
import time
import random
import pygame, sys


posponer=0.1
#marcador
score=0
high_score=0
#configuracion de la ventana
wn = turtle.Screen()
wn.title("Juego del Snake")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

#cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction="stop"
#Comida
comida=turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(100,0)
#Crecer a la serpiente
segmentos=[]
#texto
texto=turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0   High Score: 0",align="center",font=("Courier",24,"normal"))
#funciones
def arriba():
    cabeza.direction="up"
def abajo():
    cabeza.direction="down"
def derecha():
    cabeza.direction="right"
def izquierda():
    cabeza.direction="left"
#movimiento
def mov():
    if cabeza.direction=="up":
        y=cabeza.ycor()
        cabeza.sety(y+20)
    if cabeza.direction=="down":
        y=cabeza.ycor()
        cabeza.sety(y-20)
    if cabeza.direction=="left":
        x=cabeza.xcor()
        cabeza.setx(x-20)
    if cabeza.direction=="right":
        x=cabeza.xcor()
        cabeza.setx(x+20)

#presionar el teclado
wn.listen()
wn.onkeypress(arriba,"Up")
wn.onkeypress(abajo,"Down")
wn.onkeypress(izquierda,"Left")
wn.onkeypress(derecha,"Right")
pygame.init()
pygame.mixer.music.load('./Sonidos/fondo.mp3')
pygame.mixer.music.play(100)
sonidoChoque=pygame.mixer.Sound("./Sonidos/choque.wav")
sonidoComida=pygame.mixer.Sound("./Sonidos/comida.wav")
while True:
    wn.update()
    #chocar a los costados
    if cabeza.xcor()>280 or cabeza.xcor()<-280 or cabeza.ycor()>280 or cabeza.ycor()<-280:
        pygame.mixer.music.pause()
        sonidoChoque.play()
        time.sleep(2)
        pygame.mixer.music.unpause()
        pygame.mixer.music.rewind()
        cabeza.goto(0,0)
        cabeza.direction="stop"
        #esconder los fragmentos
        for segmento in segmentos:
            segmento.goto(1000,1000)
        #limpiar los elementos de la lista
        segmentos.clear()
        #resetear marcador
        score=0
        texto.clear()
        texto.write("Score: {}      High Score: {}".format(score,high_score),align="center",font=("Courier",24,"normal"))

        
    #crecer la serpiente
    if cabeza.distance(comida)<20:
        sonidoComida.play()
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        comida.goto(x,y)
        
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("grey")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)
        #aumentar marcador
        score+=100
        if score>high_score:
            high_score=score
        texto.clear()
        texto.write("Score: {}   High Score: {}".format(score,high_score),align="center",font=("Courier",24,"normal"))
    #mover el cuerpo de la serpiente
    totalSeg = len(segmentos)
    for index in range(totalSeg-1,0,-1):
        x=segmentos[index-1].xcor()
        y=segmentos[index-1].ycor()
        segmentos[index].goto(x,y)
    if totalSeg>0:
        x=cabeza.xcor()
        y=cabeza.ycor()
        segmentos[0].goto(x,y)
    
    mov()
    #colision con el cuerpo de la serpiente  
    for segmento in segmentos:
        if segmento.distance(cabeza)<20:
            pygame.mixer.music.pause()
            sonidoChoque.play()
            time.sleep(2)
            pygame.mixer.music.unpause()
            pygame.mixer.music.rewind()
            cabeza.goto(0,0)
            cabeza.direction="stop"
            #esconder los fragmentos
            for segmento in segmentos:
                segmento.goto(1000,1000)
            segmentos.clear()
            #resetear marcador
            score=0
            texto.clear()
            texto.write("Score: {}      High Score: {}".format(score,high_score),align="center",font=("Courier",24,"normal"))
    time.sleep(posponer)