import turtle
turtle.title("LUDO-GAME")
t=turtle.Turtle()
t.penup()
t.speed(0)
t.goto(-300,300)
t.pendown()
t.pensize(3)
for i in range(4):
    t.fd(600)
    t.right(90)
t.begin_fill()
for j in range(4):
    t.fd(220)
    t.right(90)
t.fillcolor("yellow")
t.end_fill()
t.fd(380)
t.begin_fill()
for k in range(4):
    t.fd(220)
    t.right(90)
t.fillcolor("red")
t.end_fill()
t.fd(220)
t.right(90)
t.fd(600)
t.right(90)
t.begin_fill()
for i in range(4):
    t.fd(220)
    t.right(90)
t.fillcolor("green")
t.end_fill()

t.fd(380)
t.begin_fill()
for k in range(4):
    t.fd(220)
    t.right(90)
t.fillcolor("blue")
t.end_fill()
t.begin_fill()
t.right(90)
t.fd(220)
t.fillcolor("blue")
t.goto(0,0)
t.goto(80,-80)
t.goto(-80,-80)
t.end_fill()
t.begin_fill()
t.fillcolor("yellow")
t.fd(160)
t.goto(0,0)
t.end_fill()
t.begin_fill()
t.fillcolor("red")
t.goto(80,80)
t.goto(-80,80)
t.end_fill()
t.goto(80,80)
t.begin_fill()
t.fillcolor("green")
t.goto(80,-80)
t.goto(0,0)
t.end_fill()
t.penup()
t.goto(300,26)
t.pendown()
t.goto(80,26)
t.penup()
t.goto(80,-26)
t.pendown()
t.goto(300,-26)
t.left(90)
i=44
k=51
t.begin_fill()
t.fillcolor("green")
for j in range(9):
    t.fd(i)
    t.right(90)
    t.fd(k)
    t.right(90)
    if j%2==0:
        i=44
    else:
        i+=44
t.fd(220)
t.end_fill()
t.begin_fill()
t.fillcolor("white")
t.bk(44)
t.left(90)
t.bk(51)
t.left(90)
t.bk(44)
t.end_fill()
for j in range(9):
    t.fd(i)
    t.left(90)
    t.fd(53)
    t.left(90)
    if j%2==0:
        i=44
    else:
        i+=44
t.fd(220)
t.begin_fill()
t.fillcolor("green")
t.bk(88)
t.left(90)
t.fd(53)
t.right(90)
t.fd(44)
t.right(90)
t.fd(53)
t.end_fill()
t.bk(105)
t.left(90)
t.fd(44)
t.left(90)
t.fd(53)
t.left(90)
t.fd(44)
for j in range(8):
    t.fd(i)
    t.left(90)
    t.fd(53)
    t.left(90)
    if j%2==0:
        i=44
    else:
        i+=44
t.fd(160)
for j in range(10):
    t.fd(i)
    t.left(90)
    t.fd(53)
    t.left(90)
    if j%2==0:
        i=44
    else:
        i+=44
t.begin_fill()
t.fillcolor("yellow")
t.left(90)
t.fd(53)
t.left(90)
t.fd(44)
t.left(90)
t.fd(53)
t.end_fill()
t.left(90)
t.bk(132)
t.left(90)
t.fd(53)
t.right(90)
a=44
t.begin_fill()
t.fillcolor("yellow")
for j in range(9):
    t.fd(a)
    t.left(90)
    t.fd(53)
    t.left(90)
    if j%2==0:
        a=44
    else:
        a+=44
t.fd(220)
t.end_fill()
t.left(180)
b=44
for j in range(9):
    t.fd(b)
    t.left(90)
    t.fd(53)
    t.left(90)
    if j%2==0:
        b=44
    else:
        b+=44
t.fd(44)
t.left(90)
t.fd(53)
t.left(90)
t.begin_fill()
t.fillcolor("white")
t.fd(44)
t.right(90)
t.fd(53)
t.right(90)
t.fd(44)
t.right(90)
t.fd(53)
t.end_fill()
t.penup()
t.goto(80,80)
t.right(180)
t.pendown()
s=44
for j in range(10):
    t.fd(s)
    t.left(90)
    t.fd(53)
    t.left(90)
    if j%2==0:
        s=44
    else:
        s+=44
t.bk(176)
t.left(90)
t.fd(106)
t.right(90)
m=44
for j in range(10):
    t.fd(m)
    t.left(90)
    t.fd(53)
    t.left(90)
    if j%2==0:
        m=44
    else:
        m+=44
t.bk(176)
t.right(90)
t.fd(53)
t.left(90)
l=44
t.begin_fill()
t.fillcolor("red")
for j in range(10):
    t.fd(l)
    t.left(90)
    t.fd(53)
    t.left(90)
    if j%2==0:
        l=44
    else:
        l+=44
t.end_fill()
t.begin_fill()
t.fillcolor("white")
t.fd(44)
t.left(90)
t.fd(53)
t.left(90)
t.fd(44)
t.left(90)
t.fd(53)
t.end_fill()
t.begin_fill()
t.fillcolor("red")
t.fd(53)
t.right(90)
t.fd(44)
t.right(90)
t.fd(53)
t.right(90)
t.fd(44)
t.end_fill()
t.penup()
t.goto(80,-300)
t.pendown()
a=44
for j in range(10):
    t.fd(a)
    t.left(90)
    t.fd(53)
    t.left(90)
    if j%2==0:
        a=44
    else:
        a+=44
t.bk(176)
t.left(90)
t.fd(53)
t.right(90)
v=44
t.begin_fill()
t.fillcolor("blue")
for j in range(10):
    t.fd(v)
    t.left(90)
    t.fd(53)
    t.left(90)
    if j%2==0:
        v=44
    else:
        v+=44
t.end_fill()
t.bk(176)
t.left(90)
t.fd(53)
t.right(90)
x=44
for j in range(10):
    t.fd(x)
    t.left(90)
    t.fd(53)
    t.left(90)
    if j%2==0:
        x=44
    else:
        x+=44
t.bk(176)
t.begin_fill()
t.fillcolor("white")
t.fd(44)
t.right(90)
t.fd(53)
t.right(90)
t.fd(44)
t.right(90)
t.fd(53)
t.end_fill()
t.begin_fill()
t.fillcolor("blue")
t.right(90)
t.fd(88)
t.left(90)
t.fd(53)
t.left(90)
t.fd(44)
t.left(90)
t.fd(53)
t.left(90)
t.fd(44)
t.end_fill()
t.left(90)
t.penup()
t.goto(260,260)
t.pendown()
t.begin_fill()
t.fillcolor("white")
for i in range(4):
    t.fd(140)
    t.left(90)
t.end_fill()
t.penup()
t.goto(260,-260)
t.pendown()
t.begin_fill()
t.fillcolor("white")
for i in range(4):
    t.fd(140)
    t.right(90)
t.end_fill()
t.penup()
t.goto(-260,-260)
t.right(180)
t.pendown()
t.begin_fill()
t.fillcolor("white")
for i in range(4):
    t.fd(140)
    t.left(90)
t.end_fill()
t.penup()
t.goto(-260,260)
t.pendown()
t.begin_fill()
t.fillcolor("white")
for i in range(4):
    t.fd(140)
    t.right(90)
t.end_fill()
t.penup()
t.goto(240,240)
t.right(90)
t.pendown()
t.begin_fill()
t.fillcolor("red")
for i in range(4):
    t.fd(40)
    t.right(90)
t.end_fill()
t.penup()
t.goto(-240,240)
t.right(90)
t.pendown()
t.begin_fill()
t.left(90)
t.fillcolor("yellow")
for i in range(4):
    t.fd(40)
    t.left(90)
t.end_fill()
t.penup()
t.goto(-240,-240)
t.pendown()
t.left(90)
t.begin_fill()
t.fillcolor("blue")
for i in range(4):
    t.fd(40)
    t.left(90)
t.end_fill()
t.penup()
t.goto(240,-240)
t.pendown()
t.left(90)
t.begin_fill()
t.fillcolor("green")
for i in range(4):
    t.fd(40)
    t.left(90)
t.end_fill()
t.penup()
t.goto(180,240)
t.pendown()
t.left(90)
t.begin_fill()
t.fillcolor("red")
for i in range(4):
    t.fd(40)
    t.left(90)
t.end_fill()
t.penup()
t.goto(-180,240)
t.pendown()
t.left(90)
t.begin_fill()
t.fillcolor("yellow")
for i in range(4):
    t.fd(40)
    t.left(90)
t.end_fill()
t.penup()
t.goto(-180,-240)
t.pendown()
t.left(90)
t.begin_fill()
t.fillcolor("blue")
for i in range(4):
    t.fd(40)
    t.left(90)
t.end_fill()
t.penup()
t.goto(180,-240)
t.pendown()
t.left(90)
t.begin_fill()
t.fillcolor("green")
for i in range(4):
    t.fd(40)
    t.left(90)
t.end_fill()
t.penup()
t.goto(240,180)
t.pendown()
t.left(90)
t.begin_fill()
t.fillcolor("red")
for i in range(4):
    t.fd(40)
    t.left(90)
t.end_fill()
t.penup()
t.goto(-240,180)
t.pendown()
t.left(90)
t.begin_fill()
t.fillcolor("yellow")
for i in range(4):
    t.fd(40)
    t.left(90)
t.end_fill()
t.penup()
t.goto(-240,-180)
t.pendown()
t.left(90)
t.begin_fill()
t.fillcolor("blue")
for i in range(4):
    t.fd(40)
    t.left(90)
t.end_fill()
t.penup()
t.goto(240,-180)
t.pendown()
t.left(90)
t.begin_fill()
t.fillcolor("green")
for i in range(4):
    t.fd(40)
    t.left(90)
t.end_fill()
t.penup()
t.goto(140,180)
t.right(90)
t.pendown()
t.begin_fill()
t.fillcolor("red")
for i in range(4):
    t.fd(40)
    t.right(90)
t.end_fill()
t.penup()
t.goto(-140,180)
t.right(90)
t.pendown()
t.begin_fill()
t.fillcolor("yellow")
for i in range(4):
    t.fd(40)
    t.right(90)
t.end_fill()
t.penup()
t.goto(-140,-180)
t.right(90)
t.pendown()
t.begin_fill()
t.fillcolor("blue")
for i in range(4):
    t.fd(40)
    t.right(90)
t.end_fill()
t.penup()
t.goto(140,-180)
t.right(90)
t.pendown()
t.begin_fill()
t.fillcolor("green")
for i in range(4):
    t.fd(40)
    t.right(90)
t.end_fill()







import turtle
import random
s = turtle.Screen()
p_1 = turtle.Turtle()
p_1.color("lime")
p_1.shape("turtle")
p_1.lt(90)
p_1.lt(90)
p_1.penup()
p_1.pensize(5)
p_1.goto(160,-160)
p_1.rt(90) 
p_2 = turtle.Turtle()
p_2.color("skyblue")
p_2.shape("turtle")
p_2.lt(90)
p_2.penup()
p_2.pensize(5)
p_2.goto(-160,-160)
p_2.rt(90)
p_3 = turtle.Turtle()
p_3.color("orange")
p_3.shape("turtle")
p_3.penup()
p_3.pensize(5)
p_3.goto(-160,160)
p_3.rt(90)
p_4 = turtle.Turtle()
p_4.color("pink")
p_4.shape("turtle")
p_4.rt(90)
p_4.penup()
p_4.pensize(5)
p_4.goto(160,160)
p_4.rt(90)


p_5 = turtle.Turtle()
p_5.color("lime")
p_5.shape("turtle")
p_5.lt(90)
p_5.lt(90)
p_5.penup()
p_5.pensize(5)
p_5.goto(220,-160)
p_5.rt(90) 
p_6 = turtle.Turtle()
p_6.color("skyblue")
p_6.shape("turtle")
p_6.lt(90)
p_6.penup()
p_6.pensize(5)
p_6.goto(-220,-160)
p_6.rt(90)
p_7 = turtle.Turtle()
p_7.color("orange")
p_7.shape("turtle")
p_7.penup()
p_7.pensize(5)
p_7.goto(-220,160)
p_7.rt(90)
p_8 = turtle.Turtle()
p_8.color("pink")
p_8.shape("turtle")
p_8.rt(90)
p_8.penup()
p_8.pensize(5)
p_8.goto(220,160)
p_8.rt(90)




p_9 = turtle.Turtle()
p_9.color("lime")
p_9.shape("turtle")
p_9.lt(90)
p_9.lt(90)
p_9.penup()
p_9.pensize(5)
p_9.goto(160,-220)
p_9.rt(90) 
p_10 = turtle.Turtle()
p_10.color("skyblue")
p_10.shape("turtle")
p_10.lt(90)
p_10.penup()
p_10.pensize(5)
p_10.goto(-160,-220)
p_10.rt(90)
p_11 = turtle.Turtle()
p_11.color("orange")
p_11.shape("turtle")
p_11.penup()
p_11.pensize(5)
p_11.goto(-160,220)
p_11.rt(90)
p_12 = turtle.Turtle()
p_12.color("pink")
p_12.shape("turtle")
p_12.rt(90)
p_12.penup()
p_12.pensize(5)
p_12.goto(160,220)
p_12.rt(90)


p_13 = turtle.Turtle()
p_13.color("lime")
p_13.shape("turtle")
p_13.lt(90)
p_13.lt(90)
p_13.penup()
p_13.pensize(5)
p_13.goto(220,-220)
p_13.rt(90) 
p_14 = turtle.Turtle()
p_14.color("skyblue")
p_14.shape("turtle")
p_14.lt(90)
p_14.penup()
p_14.pensize(5)
p_14.goto(-220,-220)
p_14.rt(90)
p_15 = turtle.Turtle()
p_15.color("orange")
p_15.shape("turtle")
p_15.penup()
p_15.pensize(5)
p_15.goto(-220,220)
p_15.rt(90)
p_16 = turtle.Turtle()
p_16.color("pink")
p_16.shape("turtle")
p_16.rt(90)
p_16.penup()
p_16.pensize(5)
p_16.goto(220,220)
p_16.rt(90)

for i in range(5):
    
    roll = int (random.randint(1,6))
    if roll==6:
      print('The number on the die is',roll)
      p_7.pensize(2)
      p_7.forward(roll*20) 
      roll_1 =int (random.randint(1,6))
      print('The number on the die is',roll)
      p_7.pensize(2)
      p_7.lt(90)
      p_7.forward(roll_1*20) 
        
    else:
        roll<=0
        print("move to red")




    roll = int (random.randint(1,6))
    if roll==6:
      print('The number on the die is',roll)
      p_2.pensize(2)
      p_2.forward(roll*20) 
      roll_1 =int (random.randint(1,6))
      print('The number on the die is',roll_1)
      p_2.pensize(2)
      p_2.lt(90)
      p_2.forward(roll_1*20) 
      
      
    else:
        roll<=0
        print("move to green")



    roll = int (random.randint(1,6))
    if roll==6:
      print('The number on the die is',roll)
      p_5.pensize(2)
      p_5.forward(roll*20) 
      roll_1 =int (random.randint(1,6))
      print('The number on the die is',roll_1)
      p_5.pensize(2)
      p_5.lt(90)
      p_5.forward(roll_1*20) 
      
      
    else:
        roll<=0
        print("move to blue")



    roll = int (random.randint(1,6))
    if roll==6:
      print('The number on the die is',roll)
      p_10.pensize(2)
      p_10.forward(roll*20) 
      roll_1 =int (random.randint(1,6))
      print('The number on the die is',roll_1)
      p_10.pensize(2)
      p_10.lt(90)
      p_10.forward(roll_1*20) 
      
      
    else:
        roll<=0
        print("move to yellow")
