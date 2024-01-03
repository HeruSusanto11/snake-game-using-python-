# mengimpor modul yang diperlukan
import pygame
import random

# menginisialisasi pygame
pygame.init()

# membuat layar permainan dengan lebar dan tinggi 600 piksel
screen = pygame.display.set_mode((600, 600))

# memberi judul dan ikon permainan
pygame.display.set_caption("Game Ular")
icon = pygame.image.load("ular.jpeg")
pygame.display.set_icon(icon)

# mendefinisikan warna yang akan digunakan
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# mendefinisikan ukuran blok ular dan makanan
BLOCK_SIZE = 20

# membuat objek ular dengan posisi awal di tengah layar
snake = pygame.sprite.Sprite()
snake.image = pygame.Surface([BLOCK_SIZE, BLOCK_SIZE])
snake.image.fill(GREEN)
snake.rect = snake.image.get_rect()
snake.rect.x = 300
snake.rect.y = 300

# membuat objek makanan dengan posisi acak di layar
food = pygame.sprite.Sprite()
food.image = pygame.Surface([BLOCK_SIZE, BLOCK_SIZE])
food.image.fill(RED)
food.rect = food.image.get_rect()
food.rect.x = random.randrange(0, 600, BLOCK_SIZE)
food.rect.y = random.randrange(0, 600, BLOCK_SIZE)

# membuat grup sprite untuk menyimpan ular dan makanan
snake_group = pygame.sprite.Group()
snake_group.add(snake)
food_group = pygame.sprite.Group()
food_group.add(food)

# membuat variabel untuk menyimpan arah gerak ular
direction = "right"

# membuat variabel untuk menyimpan skor permainan
score = 0

# membuat variabel untuk mengatur kecepatan permainan
clock = pygame.time.Clock()

# membuat variabel untuk mengontrol perulangan utama
running = True

# perulangan utama permainan
while running:
    # mengatur kecepatan permainan menjadi 15 fps
    clock.tick(15)

    # mengambil semua event yang terjadi
    for event in pygame.event.get():
        # jika event adalah klik tombol keluar, maka hentikan perulangan
        if event.type == pygame.QUIT:
            running = False
        # jika event adalah tekan tombol keyboard, maka ubah arah ular sesuai tombol yang ditekan
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
            if event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"
            if event.key == pygame.K_UP and direction != "down":
                direction = "up"
            if event.key == pygame.K_DOWN and direction != "up":
                direction = "down"

    # mengubah posisi ular sesuai arah geraknya
    if direction == "left":
        snake.rect.x -= BLOCK_SIZE
    if direction == "right":
        snake.rect.x += BLOCK_SIZE
    if direction == "up":
        snake.rect.y -= BLOCK_SIZE
    if direction == "down":
        snake.rect.y += BLOCK_SIZE

    # mengecek apakah ular keluar dari batas layar, jika ya maka hentikan perulangan
    if snake.rect.x < 0 or snake.rect.x > 580 or snake.rect.y < 0 or snake.rect.y > 580:
        running = False

    # mengecek apakah ular menabrak makanan, jika ya maka tambahkan skor dan pindahkan makanan ke posisi acak lainnya
    if pygame.sprite.spritecollide(snake, food_group, False):
        score += 1
        food.rect.x = random.randrange(0, 600, BLOCK_SIZE)
        food.rect.y = random.randrange(0, 600, BLOCK_SIZE)

    # mengisi layar dengan warna hitam
    screen.fill(BLACK)

    # menampilkan skor di pojok kiri atas layar
    font = pygame.font.SysFont("arial", 32)
    text = font.render("Skor: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))

    # menggambar ular dan makanan di layar
    snake_group.draw(screen)
    food_group.draw(screen)

    # memperbarui tampilan layar
    pygame.display.flip()

# keluar dari pygame
pygame.quit()
