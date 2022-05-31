def Carsh():
    global Enemys, Canshoot
    if Bullet.is_touching(Enemys):
        game.add_score(1)
        Bullet.delete()
        Enemys.delete()
        Enemys = game.create_sprite(randint(0, 4), 0)
        Canshoot = True
    elif Bullet.get(LedSpriteProperty.Y) == 0:
        Bullet.delete()
        Canshoot = True

def on_button_pressed_a():
    global Bullet, Canshoot
    if Canshoot:
        Bullet = game.create_sprite(Spaceship, Spaceship)
        Bullet.turn(Direction.LEFT, 90)
        Canshoot = False
input.on_button_pressed(Button.A, on_button_pressed_a)

Bullet: game.LedSprite = None
Canshoot = False
Enemys: game.LedSprite = None
Spaceship: game.LedSprite = None
Spaceship = game.create_sprite(2, 4)
Enemys = game.create_sprite(randint(0, 4), 0)
Canshoot = True
game.start_countdown(40000)

def on_forever():
    Spaceship.move(1)
    Spaceship.if_on_edge_bounce()
    if Bullet:
        Bullet.move(1)
        Carsh()
    basic.pause(200)
basic.forever(on_forever)
