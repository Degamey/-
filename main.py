import turtle
import time
import random as r
from langue import *
from tifunc import timer
from string import  ascii_uppercase,ascii_lowercase
from testrandom import randchoes
let=ascii_uppercase+ascii_lowercase
letnum=let+"0123456789"
print(let)
t=turtle.Turtle()

t.hideturtle()
t.screen.setup(900, 600)
t.write('ИГРА ЗАПОМИНАЙКА', align='center', font=("Comic Sans MS", 18, "bold"))
turtle.title("ЗАПОМИНАЙКА")
timer(2)
t.reset()
t.hideturtle()

t.write(rusruler, align='center', font=("Comic Sans MS", 12, "bold"))
timer(5)
t.reset()
t.hideturtle()
gameover=0

sym=int(turtle.numinput("Что вы хотите запоминать?","0-Числа; 1-СИМВОЛЫ; 2-СИМВОЛЫ С ЦИФРАМИ",minval=0,maxval=2))
symnum=int(turtle.numinput("Сколько символов вы хотите запоминать?","Введите количество символов",minval=3,maxval=6))
secondnum=turtle.numinput("Сколько секунд изначаль?","Введите изначальнае количество секунд(мин.5,макс.10)",minval=5,maxval=10)
if sym==0:
    minval="1"
    maxval="9"
    for i in range(symnum-1):
        minval+="0"
        maxval+="9"
    minval=int(minval)
    maxval=int(maxval)
    while gameover != 1:
        secret=r.randint(minval,maxval)

        t.write(secret, align='center', font=("Comic Sans MS", 15, "bold"))
        #timer(secondnum)
        time.sleep(secondnum)
        t.reset()
        t.hideturtle()
        world=int(turtle.numinput("Введите число","Введите число которое вы запомнили"))

        if world != secret:
            gameover=1
        if gameover == 1:
            t.write(rusgameover, align='center', font=("Comic Sans MS", 8, "bold"))
            time.sleep(4)
            exit("You lose")
        if secondnum == 2:
            t.write(rusgamewin, align='center', font=("Comic Sans MS", 8, "bold"))
            time.sleep(4)
            exit("You win")
            secondnum-=1
elif sym == 1:
    while gameover != 1:

        secret=randchoes(let,symnum)
        print(secret)
        t.write(secret, align='center', font=("Comic Sans MS", 15, "bold"))
        #timer(secondnum)
        time.sleep(secondnum)
        t.reset()
        t.hideturtle()
        world=turtle.textinput("Введите символы","Введите символы которое вы запомнили")

        if world != secret:
            gameover=1
        if gameover == 1:
            t.write(rusgameover, align='center', font=("Comic Sans MS", 8, "bold"))
            time.sleep(4)
            exit("You lose")
        if secondnum == 2:
            t.write(rusgamewin, align='center', font=("Comic Sans MS", 8, "bold"))
            time.sleep(4)
            exit("You win")
        secondnum-=1
elif sym == 2:
    while gameover != 1:
        secret=randchoes(letnum,symnum)
        t.write(secret, align='center', font=("Comic Sans MS", 15, "bold"))

        #timer(secondnum)
        time.sleep(secondnum)
        t.reset()
        t.hideturtle()
        world=turtle.textinput("Введите символы","Введите символы которое вы запомнили")

        if world != secret:
            gameover=1
        if gameover == 1:
            t.write(rusgameover, align='center', font=("Comic Sans MS", 8, "bold"))
            time.sleep(4)
            exit("You lose")
        if secondnum == 2:
            t.write(rusgamewin, align='center', font=("Comic Sans MS", 8, "bold"))
            time.sleep(4)
            exit("You win")
