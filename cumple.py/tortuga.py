import turtle
import time

# ======================
# CONFIGURACIÓN VENTANA
# ======================
screen = turtle.Screen()
screen.title("Feliz Cumpleaños 💖")
screen.bgcolor("#fff0f5")

# ======================
# TORTUGA ESCRITORA (OCULTA)
# ======================
writer = turtle.Turtle()
writer.shape("turtle")
writer.showturtle()
writer.speed(2)
writer.color("deeppink")
writer.pensize(3)

# Texto
writer.penup()
writer.goto(0, 250)
writer.write("Feliz Cumpleaños 💖", align="center",
             font=("Arial", 28, "bold"))

time.sleep(1)

# ======================
# CORAZÓN (SIN SALTO VISUAL)
# ======================
writer.color("red")
writer.pensize(3)

writer.penup()
writer.goto(0, -20)

# Orientación inicial del corazón
writer.setheading(140)

# AHORA aparece (ya orientada)
writer.showturtle()
time.sleep(0.3)

writer.pendown()
writer.begin_fill()

writer.forward(113)

for _ in range(200):
    writer.right(1)
    writer.forward(1)

writer.left(120)

for _ in range(200):
    writer.right(1)
    writer.forward(1)

writer.forward(112)
writer.end_fill()

time.sleep(0.5)
writer.hideturtle()



# ======================
# TORTUGA 1 (VISIBLE)
# ======================
t1 = turtle.Turtle()
t1.shape("turtle")
t1.color("red")
t1.shapesize(3, 3)
t1.speed(2)
t1.penup()
t1.goto(-220, -140)
t1.showturtle()

# ======================
# TORTUGA 2 (VISIBLE)
# ======================
t2 = turtle.Turtle()
t2.shape("turtle")
t2.color("pink")
t2.shapesize(2.75, 2.75)
t2.speed(2)
t2.penup()
t2.goto(-220, -190)
t2.showturtle()

# ======================
# CAMINAN JUNTAS
# ======================
while True:
    t1.forward(2)
    t2.forward(2)

# ======================
# MANTENER VENTANA ABIERTA
# ======================
screen.mainloop()
