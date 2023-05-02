import pygame
import random
import os


# Define constants
WIDTH = 800
HEIGHT = 600
FPS = 60

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroids")

# Set clock
clock = pygame.time.Clock()


# Load images
background_image = pygame.image.load(os.path.join("assets", "background.png")).convert()
player_image = pygame.image.load(os.path.join("assets", "player.png")).convert_alpha()
player_engine_image = pygame.image.load(os.path.join("assets", "player_engine.png")).convert_alpha()
asteroid_images = [
    pygame.image.load(os.path.join("assets", "asteroid.png")).convert_alpha(),
    pygame.image.load(os.path.join("assets", "asteroid.png")).convert_alpha(),
    pygame.image.load(os.path.join("assets", "asteroid.png")).convert_alpha(),
]

# Load sounds
shoot_sound = pygame.mixer.Sound(os.path.join("assets", "shoot.wav"))
explosion_sound = pygame.mixer.Sound(os.path.join("assets", "explosion.wav"))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speed = 0
        self.angle = 0

    def update(self):
        # Handle rotation
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.angle += 4
        elif keystate[pygame.K_RIGHT]:
            self.angle -= 4

        # Rotate the player image
        self.image = pygame.transform.rotate(player_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        screen.blit(self.image, self.rect)

        # Handle movement
        direction = pygame.Vector2(0, -1).rotate(-self.angle)
        if keystate[pygame.K_UP]:
            self.speed += 1
        elif keystate[pygame.K_DOWN]:
            self.speed -= 0.2
        else:
            if self.speed > 0:
                self.speed -= 0.02
        self.speed = max(0, min(5, self.speed))
        self.rect.move_ip(direction * self.speed)

        # Check if player is out of bounds and wrap around to opposite side
        if self.rect.left > WIDTH:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = WIDTH
        elif self.rect.top > HEIGHT:
            self.rect.bottom = 0
        elif self.rect.bottom < 0:
            self.rect.top = HEIGHT

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.centery)
        bullet.set_angle(self.angle)
        all_sprites.add(bullet)
        bullets.add(bullet)
        shoot_sound.play()



class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = random.choice(asteroid_images)
        self.original_image = pygame.transform.scale(self.original_image,
                                                     (random.randint(40, 90), random.randint(40, 90)))
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()

        # Новые атрибуты
        self.rotation_speed = random.randint(-1, 1)  # Случайная скорость вращения
        self.angle = 0  # Начальный угол поворота

        # Случайно выбираем одну из граней экрана и генерируем координаты вдоль неё
        side = random.choice(['left', 'right', 'top', 'bottom'])
        if side == 'left':
            self.rect.x = 0 - self.rect.width
            self.rect.y = random.randrange(0, HEIGHT - self.rect.height)
            self.speedx = random.randrange(1, 4)
            self.speedy = random.randrange(-2, 2)
        elif side == 'right':
            self.rect.x = WIDTH
            self.rect.y = random.randrange(0, HEIGHT - self.rect.height)
            self.speedx = random.randrange(-4, -1)
            self.speedy = random.randrange(-2, 2)
        elif side == 'top':
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = 0 - self.rect.height
            self.speedx = random.randrange(-2, 2)
            self.speedy = random.randrange(1, 4)
        else:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = HEIGHT
            self.speedx = random.randrange(-2, 2)
            self.speedy = random.randrange(-4, -1)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Изменяем угол поворота на основе скорости вращения
        self.angle += self.rotation_speed

        # Поворачиваем астероид вокруг центра оси
        rotated_image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = rotated_image.get_rect(center=self.rect.center)
        self.image = rotated_image

        # Если астероид вышел за границы экрана, переносим его на противоположную грань
        if self.rect.right < 0:
            self.rect.left = WIDTH
        elif self.rect.left > WIDTH:
            self.rect.right = 0
        elif self.rect.bottom < 0:
            self.rect.top = HEIGHT
        elif self.rect.top > HEIGHT:
            self.rect.bottom = 0


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(WHITE)
        self.original_image = self.image.copy()  # сохраняем оригинальное изображение
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = 10
        self.angle = 0

    def update(self):
        direction = pygame.Vector2(0, -1).rotate(-self.angle)
        self.rect.move_ip(direction * self.speed)
        if self.rect.bottom < 0:
            self.kill()
        # поворот изображения пули
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)



    def set_angle(self, angle):
        self.angle = angle
        direction = pygame.Vector2(0, -1).rotate(-self.angle)
        self.speedx = direction.x * self.speed
        self.speedy = direction.y * self.speed

# Create game objects
all_sprites = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

for i in range(8):
    asteroid = Asteroid()
    all_sprites.add(asteroid)
    asteroids.add(asteroid)

# Start game loop
running = True

while running:
    # Set clock
    clock.tick(FPS)

    # Process input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # Update game state
    all_sprites.update()

    # Check for collisions
    hits = pygame.sprite.groupcollide(asteroids, bullets, True, True)
    for hit in hits:
        explosion_sound.play()
        asteroid = Asteroid()
        all_sprites.add(asteroid)
        asteroids.add(asteroid)

    hits = pygame.sprite.spritecollide(player, asteroids, False)
    if hits:
        player.kill()
        explosion_sound.play()
        running = False

    # Draw graphics
    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    # Flip display
    pygame.display.flip()

pygame.quit()



