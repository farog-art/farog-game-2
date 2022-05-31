function Carsh () {
    if (Bullet.isTouching(Enemys)) {
        game.addScore(1)
        Bullet.delete()
        Enemys.delete()
        Enemys = game.createSprite(randint(0, 4), 0)
        Canshoot = true
    } else if (Bullet.get(LedSpriteProperty.Y) == 0) {
        Bullet.delete()
        Canshoot = true
    }
}
input.onButtonPressed(Button.A, function () {
    if (Canshoot) {
        Bullet = game.createSprite(Spaceship, Spaceship)
        Bullet.turn(Direction.Left, 90)
        Canshoot = false
    }
})
let Bullet: game.LedSprite = null
let Canshoot = false
let Enemys: game.LedSprite = null
let Spaceship: game.LedSprite = null
Spaceship = game.createSprite(2, 4)
Enemys = game.createSprite(randint(0, 4), 0)
Canshoot = true
game.startCountdown(40000)
basic.forever(function () {
    Spaceship.move(1)
    Spaceship.ifOnEdgeBounce()
    if (Bullet) {
        Bullet.move(1)
        Carsh()
    }
    basic.pause(200)
})
