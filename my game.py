from gamelib import *
game = Game(800,600,"Game")

bk = Animation("bk.png",56,game,3744/6,3820/10)
bk.resizeTo(game.width, game.height)

p = Image("images\\paddle.png",game)
p.resizeTo(800,175)
         
aliens = []
count = 0

for times in range(25):
    aliens.append(Image ("images\\alien.png",game)) 

for a in aliens:
    x = randint(50,750)
    y = game.height - randint(200, 10500)
    s = randint(2,5)
    a.resizeTo(125,125) 
    a.moveTo(x,y)
    a.setSpeed(s,180)
   

hero = Image("images\\hero.gif",game)           

plasma = []

plasma = Animation("images\\plasmaball1.png",11,game,352/11,32)
plasma.visible = False

game.drawText("Press [SPACE] to play",320,400)

explosion = Animation("images\\explosion.png",22,game, 285/5, 320/5)
explosion.resizeTo(game.height,game.width)

while not game.over:
    game.processInput()
    bk.draw()
    hero.draw()
    hero.move("True")
    p.moveTo(400,700)

    if keys.Pressed[K_LEFT]:
        hero.rotateBy(5,"left")
    if keys.Pressed[K_RIGHT]:
        hero.rotateBy(5,"right")
    if keys.Pressed[K_UP]:
        hero.forward(9)
    else:
        hero.speed *= 0.99


    if keys.Pressed[K_SPACE]:
        plasma.visible = True
        plasma.moveTo(hero.x,hero.y)
        plasma.setSpeed(10 , hero.getAngle())

    for a in aliens:#loop will go through the list
        a.move()
        if plasma.collidedWith(a):
            a.visible=False

        if a.collidedWith(p,"rectangle"):
            p.visible=False
            game.over=True
            explosion.visible=True
                    
    game.update(90)
game.quit() 
