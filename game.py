       # Imports
import pygame
import random


# Window settings
WIDTH = 1000
HEIGHT = 800
TITLE = "Generic Space shooter"
FPS = 60

# Game Stages
START = 0
PLAYING = 1
END = 2
WIN = 3
PAUSE = 4

# Create window
pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()


#game settings

difficulty = "normal"


# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Load fonts
title_font = pygame.font.Font('assets/fonts/Inversionz.ttf', 60)
default_font = pygame.font.Font('assets/fonts/Inversionz Unboxed.otf', 40)

#player images
ship_img = pygame.image.load('assets/images/player/playerShipbasic.png').convert_alpha()
doubleship_img = pygame.image.load('assets/images/player/playerShipdouble.png').convert_alpha()
invicship_img = pygame.image.load('assets/images/player/playerShipinvic.png').convert_alpha()

#Space rocks
rock1_img = pygame.image.load('assets/images/background/asteroid1.png').convert_alpha()
rock2_img = pygame.image.load('assets/images/background/asteroid2.png').convert_alpha()
rock3_img = pygame.image.load('assets/images/background/asteroid3.png').convert_alpha()
rock4_img = pygame.image.load('assets/images/background/asteroid4.png').convert_alpha()
rock5_img = pygame.image.load('assets/images/background/asteroid5.png').convert_alpha()
rock6_img = pygame.image.load('assets/images/background/asteroid6.png').convert_alpha()
rock7_img = pygame.image.load('assets/images/background/asteroid7.png').convert_alpha()
rock8_img = pygame.image.load('assets/images/background/asteroid8.png').convert_alpha()
rock9_img = pygame.image.load('assets/images/background/asteroid9.png').convert_alpha()
rock10_img = pygame.image.load('assets/images/background/asteroid10.png').convert_alpha()
rocks_img = [rock1_img,rock2_img,rock3_img,rock4_img,rock5_img,rock6_img,rock7_img,rock8_img,rock9_img,rock10_img]
#everthing else
laser_img = pygame.image.load('assets/images/lasers+powers/playerLaserbasic.png').convert_alpha()
deathray_img = pygame.image.load('assets/images/lasers+powers/enemylaser.png').convert_alpha()
bg_img = pygame.image.load('assets/images/background/ulukai/corona_bk.png').convert_alpha()
shieldpowerup_img = pygame.image.load('assets/images/lasers+powers/healthpowerup.png').convert_alpha()
laserpowerup_img = pygame.image.load('assets/images/lasers+powers/laserpowerup.png').convert_alpha()
invicpowerup_img = pygame.image.load('assets/images/lasers+powers/invicpowerup.png').convert_alpha()
rapidpowerup_img = pygame.image.load('assets/images/lasers+powers/rapidpowerup.png').convert_alpha()

#enemy images
    #ship
e1bh_img = pygame.image.load('assets/images/enemies/shipGrunt3.png').convert_alpha()
et1bh_img = pygame.image.load('assets/images/enemies/shipTank3.png').convert_alpha()
b1bh_img = pygame.image.load('assets/images/enemies/shipBoss3.png').convert_alpha()
e1h_img = pygame.image.load('assets/images/enemies/shipGrunt2.png').convert_alpha()
et1h_img = pygame.image.load('assets/images/enemies/shipTank2.png').convert_alpha()
b1h_img = pygame.image.load('assets/images/enemies/shipBoss2.png').convert_alpha()
e1n_img = pygame.image.load('assets/images/enemies/shipGrunt1.png').convert_alpha()
et1n_img = pygame.image.load('assets/images/enemies/shipTank1.png').convert_alpha()
b1n_img = pygame.image.load('assets/images/enemies/shipBoss1.png').convert_alpha()
    #parasite
e2bh_img = pygame.image.load('assets/images/enemies/parasiteGrunt3.png').convert_alpha()
et2bh_img = pygame.image.load('assets/images/enemies/parasiteTank3.png').convert_alpha()
b2bh_img = pygame.image.load('assets/images/enemies/parasiteBoss3.png').convert_alpha()
e2h_img = pygame.image.load('assets/images/enemies/parasiteGrunt2.png').convert_alpha()
et2h_img = pygame.image.load('assets/images/enemies/parasiteTank2.png').convert_alpha()
b2h_img = pygame.image.load('assets/images/enemies/parasiteBoss2.png').convert_alpha()
e2n_img = pygame.image.load('assets/images/enemies/parasiteGrunt1.png').convert_alpha()
et2n_img = pygame.image.load('assets/images/enemies/parasiteTank1.png').convert_alpha()
b2n_img = pygame.image.load('assets/images/enemies/parasiteBoss1.png').convert_alpha()
    #abyssal
e3bh_img = pygame.image.load('assets/images/enemies/abyssalGrunt3.png').convert_alpha()
et3bh_img = pygame.image.load('assets/images/enemies/abyssalTank3.png').convert_alpha()
b3bh_img = pygame.image.load('assets/images/enemies/abyssalBoss3.png').convert_alpha()
e3h_img = pygame.image.load('assets/images/enemies/abyssalGrunt2.png').convert_alpha()
et3h_img = pygame.image.load('assets/images/enemies/abyssalTank2.png').convert_alpha()
b3h_img = pygame.image.load('assets/images/enemies/abyssalBoss2.png').convert_alpha()
e3n_img = pygame.image.load('assets/images/enemies/abyssalGrunt1.png').convert_alpha()
et3n_img = pygame.image.load('assets/images/enemies/abyssalTank1.png').convert_alpha()
b3n_img = pygame.image.load('assets/images/enemies/abyssalBoss1.png').convert_alpha()


#level endless images
    

# Load sounds
laser_snd = pygame.mixer.Sound('assets/sounds/laser.ogg')
explosion_snd = pygame.mixer.Sound('assets/sounds/explosion.ogg')
powerup_snd = pygame.mixer.Sound('assets/sounds/powerup.ogg')

# Music
start_music = ['assets/music/titlemusic1.ogg', 'assets/music/titlemusic2.ogg']
play_music = ['assets/music/thememusic1.ogg','assets/music/thememusic2.ogg',
              'assets/music/thememusic3.ogg','assets/music/thememusic4.ogg',
              'assets/music/thememusic5.ogg','assets/music/thememusic6.ogg']


# Game classes
class Ship(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = x, y

        self.speed = 6
        self.shield = 3
        self.shoots_double = False
        self.invicibility_time = 0
        self.shot_wait_time = 0
        self.shot_delay = 30

    def move_left(self):
        self.rect.x -= self.speed

        if self.rect.left < 0:
            self.rect.left = 0

    def move_right(self):
        self.rect.x += self.speed

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH


    def shoot(self):
        if self.shoots_double:
            if self.shot_wait_time == 0:
                x = self.rect.left + 3
                y = self.rect.centery + 15

                laser = (Laser(x, y, laser_img) )
                lasers.add(laser)
                
                
                x = self.rect.right - 3
                y = self.rect.centery + 15

                laser = (Laser(x, y, laser_img) )
                lasers.add(laser)
                self.shot_wait_time = self.shot_delay
            
        else:
            if self.shot_wait_time == 0:
                x = self.rect.centerx
                y = self.rect.top

                laser = (Laser(x, y, laser_img) )
                lasers.add(laser)
                self.shot_wait_time = self.shot_delay
                
        laser_snd.play()

    def set_image(self):
        if self.invicibility_time > 0:
            self.image = invicship_img
            
        elif self.invicibility_time == 0 and self.shoots_double == True:
            self.image = doubleship_img
            
        else:
            self.image = ship_img
            
    def check_deathrays(self):
        hits = pygame.sprite.spritecollide(self, deathrays, True,
                                           pygame.sprite.collide_mask)
        
        if self.invicibility_time == 0:
            
            for hit in hits:
                self.shield -= 1

                self.shoots_double = False
                
                
                if self.shield <= 0:
                    self.kill()
                    explosion_snd.play()

        else:
            self.invicibility_time -= 1

    def check_powerups(self):
        hits = pygame.sprite.spritecollide(self, powerups, True)

        
        for hit in hits:
            hit.apply(self)
            print("insert powerup sound here")
        
    def update(self):
        self.check_deathrays()
        self.check_powerups()
        self.set_image()
        if self.shot_wait_time > 0:
            self.shot_wait_time -=1

class Fallingrocks(pygame.sprite.Sprite):
    
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = x, y

        self.speed = 12
        
    def update(self):
        self.rect.y += self.speed
        self.rect.x += 2

        if self.rect.top > HEIGHT:
            self.rect.y = random.randrange(-4000, -1000)
            self.rect.x = random.randrange(0, WIDTH)
            self.image = random.choice(rocks_img)
            

        
class Laser(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = x, y

        self.speed = 8

    def update(self):
        self.rect.y -= self.speed

        if self.rect.bottom < 0:
            self.kill()
            
class ShieldPowerup(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = x, y

        self.speed = 5

    def apply(self, ship):
        if ship.shield >= 3:
            ship.shield += 1
            powerup_snd.play()
        else:
            ship.shield = 3
            powerup_snd.play()

    def update(self):
        self.rect.y += self.speed

        if self.rect.top > HEIGHT:
            self.kill()

class LaserPowerup(pygame.sprite.Sprite):
#adds more lasers everytime picked up stops at 5

    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = x, y

        self.speed = 5

    def apply(self, ship):
        ship.shoots_double = True

        powerup_snd.play()

    def update(self):
        self.rect.y += self.speed

        if self.rect.top > HEIGHT:
            self.kill()

class InviciblityPowerup(pygame.sprite.Sprite):
#5 seconds of undeath
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = x, y

        self.speed = 5

    def apply(self, ship):
        ship.invicibility_time = 5 * FPS


        powerup_snd.play()
    
    def update(self):
        
        self.rect.y += self.speed

        if self.rect.top > HEIGHT:
            self.kill()

class AllyPowerup(pygame.sprite.Sprite):
#adds one mini ship on right until picked up again then add another on left
#then just add health to them with each consecutive pick up

    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = x, y

        self.speed = 5

    def apply(self, ship):
        pass

class Deathray(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = x, y

        self.speed = 4

    def update(self):
        self.rect.y += self.speed

        if self.rect.top > HEIGHT:
            self.kill()

class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y, image, shield, value):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = x, y

        self.shield = shield
        self.value = value

    def fire(self):
        x = self.rect.centerx
        y = self.rect.bottom
        deathrays.add(Deathray(x, y, deathray_img))
        laser_snd.play()

    def update(self):
        hits = pygame.sprite.spritecollide(self, lasers, True)

        for laser in hits:
            self.shield -= 1

        if self.shield <= 0:
            self.kill()
            explosion_snd.play()
            player.score += self.value
            print(player.score)

class Boss(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = x, y

        self.shield = 30

    def fire(self):
        x = self.rect.centerx
        y = self.rect.bottom

        deathray = Deathray(x, y, deathray_img)
        deathrays.add(deathray)
        
        laser_snd.play()

    def update(self):
        hits = pygame.sprite.spritecollide(self, lasers, True)

        for laser in hits:
            self.shield -= 1

            if self.shield <= 0:
                self.kill()
                explosion_snd.play()
                player.score += 500


class Fleet(pygame.sprite.Group):

    def __init__(self, *sprites):
        super().__init__(*sprites)

        self.speed = 2
        self.deathray_rate = 1
        
    def move(self):
        reverse = False

        for sprite in self.sprites():
             sprite.rect.x += self.speed

             if sprite.rect.right > WIDTH or sprite.rect.left < 0:
                 reverse = True

        if reverse:
             self.speed *= -1
                
    def select_attacker(self):
        sprites = self.sprites()
        
        if len(sprites) > 0:
            r = random.randrange(0, 120)
            
            if r < self.deathray_rate + player.level:
                attacker = random.choice(sprites)
                attacker.fire()
    
    def update(self, *args):
        super().update(*args)

        self.move()

        if len(player) > 0:
            self.select_attacker()

        
# Setup
def new_game():
    global player, ship
    
    start_x = WIDTH/2
    start_y = HEIGHT - 100
    ship = Ship(start_x, start_y,ship_img)
    
    player = pygame.sprite.GroupSingle(ship)
    player.score = 0
    player.level = 1

def play_random_track(tracks):
    song = random.choice(tracks)

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(0)

def make_random_enemies(num_enemies, num_enemytanks):
    global enemies
    
    locs = [(50,50),(100,50),(200,50),(300,50),
            (400,50),(500,50),(600,50),(700,50),
            (800,50),(900,50),(0,100),(100,100),
            (200,100),(300,100),(400,100),(500,100),
            (600,100),(700,100),(800,100),(900,100),
            (50,150),(100,150),(200,150),(300,150),
            (400,150),(500,150),(600,150),(700,150),
            (800,200),(900,200),(50,200),(100,200),
            (200,200),(300,200),(400,200),(500,200),
            (600,200),(700,200),(800,200),(900,200),
            (50,250),(100,250),(200,250),(300,250),
            (400,250),(500,250),(600,250),(700,250),
            (800,250),(900,250),(50,300),(100,300),
            (200,300),(300,300),(400,300),(500,300),
            (600,300),(700,300),(800,300),(900,300),
            (400,350),(450,350),(500,350),(550,350)]

    for _ in range(num_enemies):
        loc = random.choice(locs)

        x = loc[0] + random.randrange (0, 75)
        y = loc[1] + random.randrange (0, 25)
        enemies.add(Enemy(x, y, e2n_img, 1, 10))

        locs.remove(loc)
        
    for _ in range(num_enemytanks):
        loc = random.choice(locs)

        x = loc[0] + random.randrange (0, 75)
        y = loc[1] + random.randrange (0, 25)
        enemies.add(Enemy(x, y, et2n_img, 3, 50))

        locs.remove(loc)
 
def start_level():
    global enemies, lasers, deathrays, powerups, rockstorm

    enemies = Fleet()
    
    if player.level == 1:
        e1 = Enemy(50,100, e1n_img, 1, 10)
        e2 = Enemy(150,100, e1n_img, 1, 10)
        e3 = Enemy(250,100, e1n_img, 1, 10)
        e4 = Enemy(350,100, e1n_img, 1, 10)
        e5 = Enemy(450,100, et1n_img, 3, 10)
        e6 = Enemy(550,100, et1n_img, 3, 10)
        e7 = Enemy(650,100, e1n_img, 1, 10)
        e8 = Enemy(750,100, e1n_img, 1, 10)
        e9 = Enemy(850,100, e1n_img, 1, 10)
        e10 = Enemy(950,100, e1n_img, 1, 10)
        e11 = Enemy(100,200, e1n_img, 1, 10)
        e12 = Enemy(200,200, e1n_img, 1, 10)
        e13 = Enemy(300,200, e1n_img, 1, 10)
        e14 = Enemy(400,200, e1n_img, 1, 10)
        e15 = Enemy(500,200, e1n_img, 1, 10)
        e16 = Enemy(600,200, e1n_img, 1, 10)
        e17 = Enemy(700,200, e1n_img, 1, 10)
        e18 = Enemy(800,200, e1n_img, 1, 10)
        e19 = Enemy(900,200, e1n_img, 1, 10)
        enemies = Fleet(e1, e2, e3, e4, e5, e6, e7, e8, e9, e10,
                        e11, e12, e13, e14, e15, e16, e17, e18, e19)
    elif player.level == 2:
        e1 = Enemy(50,100, et1n_img, 3, 10)
        e2 = Enemy(150,100, et1n_img, 3, 10)
        e3 = Enemy(250,100, et1n_img, 3, 10)
        e4 = Enemy(350,100, et1n_img, 3, 10)
        e5 = Enemy(450,100, et1n_img, 3, 10)
        e6 = Enemy(550,100, et1n_img, 3, 10)
        e7 = Enemy(650,100, et1n_img, 3, 10)
        e8 = Enemy(750,100, et1n_img, 3, 10)
        e9 = Enemy(850,100, et1n_img, 3, 10)
        e10 = Enemy(950,100, et1n_img, 1, 10)
        e11 = Enemy(100,200, e1n_img, 1, 10)
        e12 = Enemy(200,200, e1n_img, 1, 10)
        e13 = Enemy(300,200, e1n_img, 1, 10)
        e14 = Enemy(400,200, e1n_img, 1, 10)
        e15 = Enemy(500,200, e1n_img, 1, 10)
        e16 = Enemy(600,200, e1n_img, 1, 10)
        e17 = Enemy(700,200, e1n_img, 1, 10)
        e18 = Enemy(800,200, e1n_img, 1, 10)
        e19 = Enemy(900,200, e1n_img, 1, 10)
        e20 = Enemy(250,250, e1n_img, 1, 10)
        e21 = Enemy(350,250, e1n_img, 1, 10)
        e22 = Enemy(450,250, e1n_img, 1, 10)
        e23 = Enemy(550,250, e1n_img, 1, 10)
        e24 = Enemy(650,250, e1n_img, 1, 10)
        e25 = Enemy(750,250, e1n_img, 1, 10)
        enemies = Fleet(e1, e2, e3, e4, e5, e6, e7, e8, e9, e10,
                        e11, e12, e13, e14, e15, e16, e17, e18,
                        e19, e20, e21, e22, e23, e24, e25)
    elif player.level == 3:
        e1 = Enemy(100,100, et1n_img, 3, 50)
        e2 = Enemy(200,100, et1n_img, 3, 50)
        e3 = Enemy(300,100, et1n_img, 3, 50)
        e4 = Enemy(400,100, et1n_img, 3, 50)
        e5 = Boss(500,100, b1n_img)
        e6 = Enemy(600,100, et1n_img, 3, 50)
        e7 = Enemy(700,100, et1n_img, 3, 50)
        e8 = Enemy(800,100, et1n_img, 3, 50)
        e9 = Enemy(900,100, et1n_img, 3, 50)
        e10 = Enemy(50,200, e1n_img, 1, 10)
        e11 = Enemy(100,200, e1n_img, 1, 10)
        e12 = Enemy(150,200, e1n_img, 1, 10)
        e13 = Enemy(200,200, e1n_img, 1, 10)
        e14 = Enemy(250,200, e1n_img, 1, 10)
        e15 = Enemy(300,200, e1n_img, 1, 10)
        e16 = Enemy(350,200, e1n_img, 1, 10)
        e17 = Enemy(400,200, e1n_img, 1, 10)
        e18 = Enemy(450,200, e1n_img, 1, 10)
        e19 = Enemy(500,200, e1n_img, 1, 10)
        e20 = Enemy(550,200, e1n_img, 1, 10)
        e21 = Enemy(600,200, e1n_img, 1, 10)
        e22 = Enemy(650,200, e1n_img, 1, 10)
        e23 = Enemy(700,200, e1n_img, 1, 10)
        e24 = Enemy(750,200, e1n_img, 1, 10)
        e25 = Enemy(800,200, e1n_img, 1, 10)
        e26 = Enemy(850,200, e1n_img, 1, 10)
        e27 = Enemy(900,200, e1n_img, 1, 10)
        e28 = Enemy(950,200, e1n_img, 1, 10)
        e29 = Enemy(75,250, e1n_img, 3, 50)
        e30 = Enemy(125,250, e1n_img, 1, 10)
        e31 = Enemy(175,250, e1n_img, 1, 10)
        e32 = Enemy(225,250, e1n_img, 1, 10)
        e33 = Enemy(275,250, e1n_img, 1, 10)
        e34 = Enemy(325,250, e1n_img, 1, 10)
        e35 = Enemy(375,250, e1n_img, 1, 10)
        e36 = Enemy(425,250, e1n_img, 1, 10)
        e37 = Enemy(475,250, e1n_img, 1, 10)
        e38 = Enemy(525,250, e1n_img, 1, 10)
        e39 = Enemy(575,250, e1n_img, 1, 10)
        e40 = Enemy(625,250, e1n_img, 1, 10)
        e41 = Enemy(675,250, e1n_img, 1, 10)
        e42 = Enemy(725,250, e1n_img, 1, 10)
        e43 = Enemy(775,250, e1n_img, 1, 10)
        e44 = Enemy(825,250, e1n_img, 1, 10)
        e45 = Enemy(875,250, e1n_img, 1, 10)
        e46 = Enemy(925,250, e1n_img, 1, 10)
        enemies = Fleet(e1, e2, e3, e4, e5, e6, e7, e8, e9, e10,
                        e11, e12, e13, e14, e15, e16, e17, e18,
                        e19, e20, e21, e22, e23, e24, e25, e26,
                        e27, e28, e29, e30, e31, e32, e33, e34,
                        e35, e36, e37, e38, e39, e40, e41, e42,
                        e43, e44, e45, e46)
    elif player.level == 4:
        make_random_enemies(14,7)

    elif player.level == 5:
        make_random_enemies(24,12)
    
    elif player.level == 6:
        make_random_enemies(35,20)
        e1 = Boss(500,100,b2n_img)
        enemies.add(e1)
        
    elif player.level == 7:
        e1 = Enemy(150,80, et3n_img, 3, 50)
        e2 = Enemy(200,100, et3n_img, 3, 50)
        e3 = Enemy(250,80, et3n_img, 3, 50)
        e4 = Enemy(100,100, e3n_img, 1, 10)
        e5 = Enemy(150,150, e3n_img, 1, 10)
        e6 = Enemy(200,180, e3n_img, 1, 10)
        e7 = Enemy(250,150, e3n_img, 1, 10)
        e8 = Enemy(300,100, e3n_img, 1, 10)
        
        e9 = Enemy(450,80, et3n_img, 3, 50)
        e10 = Enemy(500,100, et3n_img, 3, 50)
        e11 = Enemy(550,80, et3n_img, 3, 50)
        e12 = Enemy(400,100, e3n_img, 1, 10)
        e13 = Enemy(450,150, e3n_img, 1, 10)
        e14 = Enemy(500,180, e3n_img, 1, 10)
        e15 = Enemy(550,150, e3n_img, 1, 10)
        e16 = Enemy(600,100, e3n_img, 1, 10)
        
        e17 = Enemy(750,80, et3n_img, 3, 50)
        e18 = Enemy(800,100, et3n_img, 3, 50)
        e19 = Enemy(850,80, et3n_img, 3, 50)
        e20 = Enemy(700,100, e3n_img, 1, 10)
        e21 = Enemy(750,150, e3n_img, 1, 10)
        e22 = Enemy(800,180, e3n_img, 1, 10)
        e23 = Enemy(850,150, e3n_img, 1, 10)
        e24 = Enemy(900,100, e3n_img, 1, 10)
        
        enemies = Fleet(e1, e2, e3, e4, e5, e6, e7,
                        e8, e9, e10, e11, e12, e13,
                        e14, e15, e16, e17, e18,
                        e19, e20, e21, e22, e23, e24)
    elif player.level == 8:
        e1 = Enemy(150,80, et3n_img, 3, 50)
        e2 = Enemy(200,100, et3n_img, 3, 50)
        e3 = Enemy(250,80, et3n_img, 3, 50)
        e4 = Enemy(100,100, e3n_img, 1, 10)
        e5 = Enemy(150,150, e3n_img, 1, 10)
        e6 = Enemy(200,180, e3n_img, 1, 10)
        e7 = Enemy(250,150, e3n_img, 1, 10)
        e8 = Enemy(300,100, e3n_img, 1, 10)
        
        e9 = Enemy(450,80, et3n_img, 3, 50)
        e10 = Enemy(500,100, et3n_img, 3, 50)
        e11 = Enemy(550,80, et3n_img, 3, 50)
        e12 = Enemy(400,100, e3n_img, 1, 10)
        e13 = Enemy(450,150, e3n_img, 1, 10)
        e14 = Enemy(500,180, e3n_img, 1, 10)
        e15 = Enemy(550,150, e3n_img, 1, 10)
        e16 = Enemy(600,100, e3n_img, 1, 10)
        
        e17 = Enemy(750,80, et3n_img, 3, 50)
        e18 = Enemy(800,100, et3n_img, 3, 50)
        e19 = Enemy(850,80, et3n_img, 3, 50)
        e20 = Enemy(700,100, e3n_img, 1, 10)
        e21 = Enemy(750,150, e3n_img, 1, 10)
        e22 = Enemy(800,180, e3n_img, 1, 10)
        e23 = Enemy(850,150, e3n_img, 1, 10)
        e24 = Enemy(900,100, e3n_img, 1, 10)

        e25 = Enemy(450,280, et3n_img, 3, 50)
        e26 = Enemy(500,300, et3n_img, 3, 50)
        e27 = Enemy(550,280, et3n_img, 3, 50)
        e28 = Enemy(400,300, e3n_img, 1, 10)
        e29 = Enemy(450,350, e3n_img, 1, 10)
        e30 = Enemy(500,380, e3n_img, 1, 10)
        e31 = Enemy(550,350, e3n_img, 1, 10)
        e32 = Enemy(600,300, e3n_img, 1, 10)
        
        enemies = Fleet(e1, e2, e3, e4, e5, e6, e7,
                        e8, e9, e10, e11, e12, e13,
                        e14, e15, e16, e17, e18, e19,
                        e20, e21, e22, e23, e24, e25,
                        e26, e27, e28, e29, e30, e31, e32)
    elif player.level == 9:
        e1 = Enemy(150,80, et3n_img, 3, 50)
        e2 = Enemy(200,100, et3n_img, 3, 50)
        e3 = Enemy(250,80, et3n_img, 3, 50)
        e4 = Enemy(100,100, e3n_img, 1, 10)
        e5 = Enemy(150,150, e3n_img, 1, 10)
        e6 = Enemy(200,180, e3n_img, 1, 10)
        e7 = Enemy(250,150, e3n_img, 1, 10)
        e8 = Enemy(300,100, e3n_img, 1, 10)
        
        e9 = Enemy(450,130, et3n_img, 3, 50)
        e10 = Enemy(500,150, et3n_img, 3, 50)
        e11 = Enemy(550,130, et3n_img, 3, 50)
        e12 = Enemy(400,150, e3n_img, 1, 10)
        e13 = Enemy(450,200, e3n_img, 1, 10)
        e14 = Enemy(500,230, e3n_img, 1, 10)
        e15 = Enemy(550,200, e3n_img, 1, 10)
        e16 = Enemy(600,100, e3n_img, 1, 10)
        
        e17 = Enemy(750,80, et3n_img, 3, 50)
        e18 = Enemy(800,100, et3n_img, 3, 50)
        e19 = Enemy(850,80, et3n_img, 3, 50)
        e20 = Enemy(700,100, e3n_img, 1, 10)
        e21 = Enemy(750,150, e3n_img, 1, 10)
        e22 = Enemy(800,180, e3n_img, 1, 10)
        e23 = Enemy(850,150, e3n_img, 1, 10)
        e24 = Enemy(900,100, e3n_img, 1, 10)

        e25 = Enemy(450,280, et3n_img, 3, 50)
        e26 = Enemy(500,300, et3n_img, 3, 50)
        e27 = Enemy(550,280, et3n_img, 3, 50)
        e28 = Enemy(400,300, e3n_img, 1, 10)
        e29 = Enemy(450,350, e3n_img, 1, 10)
        e30 = Enemy(500,380, e3n_img, 1, 10)
        e31 = Enemy(550,350, e3n_img, 1, 10)
        e32 = Enemy(600,300, e3n_img, 1, 10)

        e33 = Enemy(150,280, et3n_img, 3, 50)
        e34 = Enemy(200,300, et3n_img, 3, 50)
        e35 = Enemy(250,280, et3n_img, 3, 50)
        e36 = Enemy(100,300, e3n_img, 1, 10)
        e37 = Enemy(150,350, e3n_img, 1, 10)
        e38 = Enemy(200,380, e3n_img, 1, 10)
        e39 = Enemy(250,350, e3n_img, 1, 10)
        e40 = Enemy(300,300, e3n_img, 1, 10)
        
        e41 = Enemy(450,480, et3n_img, 3, 50)
        e42 = Enemy(500,500, et3n_img, 3, 50)
        e43 = Enemy(550,480, et3n_img, 3, 50)
        e44 = Enemy(400,500, e3n_img, 1, 10)
        e45 = Enemy(450,550, e3n_img, 1, 10)
        e46 = Enemy(500,580, e3n_img, 1, 10)
        e47 = Enemy(550,550, e3n_img, 1, 10)
        e48 = Enemy(600,500, e3n_img, 1, 10)
        
        e49 = Enemy(750,280, et3n_img, 3, 50)
        e50 = Enemy(800,300, et3n_img, 3, 50)
        e51 = Enemy(850,280, et3n_img, 3, 50)
        e52 = Enemy(700,300, e3n_img, 1, 10)
        e53 = Enemy(750,350, e3n_img, 1, 10)
        e54 = Enemy(800,380, e3n_img, 1, 10)
        e55 = Enemy(850,350, e3n_img, 1, 10)
        e56 = Enemy(900,300, e3n_img, 1, 10)
        
        e57 = Boss(500, 50, b3n_img)
        enemies = Fleet(e1, e2, e3, e4, e5, e6, e7,
                        e8, e9, e10, e11, e12, e13,
                        e14, e15, e16, e17, e18, e19,
                        e20, e21, e22, e23, e24, e25,
                        e26, e27, e28, e29, e30, e31,
                        e32, e33, e34, e35, e36, e36,
                        e37, e38, e39, e40, e41, e42,
                        e43, e44, e45, e46, e47, e48,
                        e49, e50, e51, e52, e53, e54,
                        e55, e56, e57)
        
    lasers = pygame.sprite.Group()
    deathrays = pygame.sprite.Group()
#powerups
    x = random.randint(0, WIDTH)
    y = random.randrange(-3000, -1000)
    pl = ShieldPowerup (x, y, shieldpowerup_img)
    
    x = random.randint(0, WIDTH)
    y = random.randrange(-3000, -1000)
    p2 = LaserPowerup (x, y, laserpowerup_img)

    x = random.randint(0, WIDTH)
    y = random.randrange(-3000, -1000)
    p3 = InviciblityPowerup (x, y, invicpowerup_img)

    
    powerups = pygame.sprite.Group(pl, p2, p3)
#astroids
    x = random.randint(-500, WIDTH)
    y = random.randrange(-4000, -1000)    
    r1 = Fallingrocks(x, y, random.choice(rocks_img))
    
    x = random.randint(-500, WIDTH)
    y = random.randrange(-4000, -1000)    
    r2 = Fallingrocks(x, y, random.choice(rocks_img))
    
    x = random.randint(-500, WIDTH)
    y = random.randrange(-4000, -1000)    
    r3 = Fallingrocks(x, y, random.choice(rocks_img))
    
    x = random.randint(0, WIDTH)
    y = random.randrange(-4000, -1000)    
    r4 = Fallingrocks(x, y, random.choice(rocks_img))
    
    rockstorm = pygame.sprite.Group(r1, r2, r3, r4)
    
def display_stats():
    score_text = default_font.render("Score: " + str(player.score), True, WHITE)
    rect = score_text.get_rect()
    rect.top = 20
    rect.left = 20
    screen.blit(score_text, rect)

    level_text = default_font.render("Level: " + str(player.level), True, WHITE)
    rect = level_text.get_rect()
    rect.top = 20
    rect.right = WIDTH - 20
    screen.blit(level_text, rect)

    shield_text = default_font.render("Shield: " + str(ship.shield), True, WHITE)
    rect = shield_text.get_rect()
    rect.bottom = HEIGHT - 20
    rect.left = 20
    screen.blit(shield_text, rect)

def start_screen():
    screen.fill(BLACK)
    
    title_text = title_font.render(TITLE, True, WHITE)
    rect = title_text.get_rect()
    rect.centerx = WIDTH // 2
    rect.bottom = HEIGHT // 2
    screen.blit(title_text, rect)

    sub_text = default_font.render('Press 1-3 for easiest to ', True, WHITE)
    rect = sub_text.get_rect()
    rect.centerx = WIDTH // 2
    rect.top = HEIGHT // 2
    screen.blit(sub_text, rect)

    subsub_text = default_font.render('hardest difficulty', True, WHITE)
    rect = subsub_text.get_rect()
    rect.centerx = WIDTH // 2
    rect.top = HEIGHT // 2 + 50
    screen.blit(subsub_text, rect)
    
def end_screen():
    end_text = title_font.render("GAME OVER", True, WHITE)
    rect = end_text.get_rect()
    rect.centerx = WIDTH // 2
    rect.centery = HEIGHT // 2
    screen.blit(end_text, rect)

def win_screen():
    end_text = title_font.render("Yes", True, WHITE)
    rect = end_text.get_rect()
    rect.centerx = WIDTH // 2
    rect.centery = HEIGHT // 2
    screen.blit(end_text, rect)
    
# Game loop
new_game()
start_level()
stage = START
running = True

while running:
    # Input handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if stage == START:
                stage = PLAYING
                pygame.mixer.music.stop()
                if event.key == pygame.K_1:
                    difficulty = ('normal')
                    print ('normal')
                if event.key == pygame.K_2:
                    difficulty = ('hard')
                    print ('hard')
                if event.key == pygame.K_3:
                    difficulty = ('bullet hell')
                    print ('bullet')
            elif stage == PLAYING:
                if event.key == pygame.K_p:
                    stage = PAUSE
            elif stage == PAUSE:
                if event.key == pygame.K_p:
                    stage = PLAYING      
            elif stage == END or stage == WIN:
                if event.key == pygame.K_r:
                    new_game()
                    start_level()
                    stage = START

    if stage == PLAYING:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            ship.shoot()
        if pressed[pygame.K_a]:
            ship.move_left()
        elif pressed[pygame.K_d]:
            ship.move_right()

    
    # Game logic
    if stage != START and stage != PAUSE:
        lasers.update()
        deathrays.update()
        rockstorm.update()
        enemies.update()
        player.update()
        powerups.update()

    if len(enemies)== 0:
        if player.level == 9:
            stage = WIN
        else:
            player.level += 1
            start_level()
    elif len(player) == 0:
        stage = END
        pygame.mixer.music.stop()

    music_on = pygame.mixer.music.get_busy()
    if not music_on:
        if stage == START:
            play_random_track(start_music)
        elif stage == PLAYING:
            play_random_track(play_music)


        
    # Drawing code
    screen.blit(bg_img, [0,0])
    rockstorm.draw(screen)
    lasers.draw(screen)
    deathrays.draw(screen)
    player.draw(screen)
    enemies.draw(screen)
    powerups.draw(screen)
    display_stats()

    if stage == START:
        start_screen()
    elif stage == END:
        end_screen()
    elif stage == WIN:
        win_screen()

        
    # Update screen
    pygame.display.update()


    # Limit refresh rate of game loop 
    clock.tick(FPS)


# Close window and quit
pygame.quit()


