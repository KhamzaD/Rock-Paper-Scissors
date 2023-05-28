import pygame
import random
import math

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
razmer = (1000, 700)
ecran = pygame.display.set_mode(razmer)
pygame.display.set_caption("My Game")

pygame.mixer.music.load("guts.mp3")
pygame.mixer.music.play(-1)

finally_sound = pygame.mixer.Sound("finally_sound.ogg")
fSound = True

new_razmer_1 = 50
new_razmer_2 = 50

konan = pygame.image.load("konan.png")
skala = pygame.image.load("skala.png")
nozh = pygame.image.load("nozh.png")

new_razmer_3 = 300
new_razmer_4 = 300

small_konan = pygame.transform.scale(konan, (new_razmer_1, new_razmer_2))
small_skala = pygame.transform.scale(skala, (new_razmer_1, new_razmer_2))
small_nozh = pygame.transform.scale(nozh, (new_razmer_1, new_razmer_2))

small_konan_end = pygame.transform.scale(konan, (new_razmer_3, new_razmer_4))
small_skala_end = pygame.transform.scale(skala, (new_razmer_3, new_razmer_4))
small_nozh_end = pygame.transform.scale(nozh, (new_razmer_3, new_razmer_4))

kok = (0, 0, 255)
aq = (255, 255, 255)
qyzyl = (255, 0, 0)

objects = []

num_konan = random.randint(5, 10)
num_skala = random.randint(5, 10)
num_nozh = random.randint(5, 10)

for i in range(num_konan):
    obj = {
        'image': small_konan.copy(),
        'type': 'konan',
        'x': random.randint(0, razmer[0] - new_razmer_1),
        'y': random.randint(0, razmer[1] - new_razmer_2),
        'dir_x': random.choice([-1, 1]),
        'dir_y': random.choice([-1, 1])
    }
    objects.append(obj)

for i in range(num_skala):
    obj = {
        'image': small_skala.copy(),
        'type': 'skala',
        'x': random.randint(0, razmer[0] - new_razmer_1),
        'y': random.randint(0, razmer[1] - new_razmer_2),
        'dir_x': random.choice([-1, 1]),
        'dir_y': random.choice([-1, 1])
    }
    objects.append(obj)

for i in range(num_nozh):
    obj = {
        'image': small_nozh.copy(),
        'type': 'nozh',
        'x': random.randint(0, razmer[0] - new_razmer_1),
        'y': random.randint(0, razmer[1] - new_razmer_2),
        'dir_x': random.choice([-1, 1]),
        'dir_y': random.choice([-1, 1])
    }
    objects.append(obj)

uaqyt = pygame.time.Clock()
V = 70
width, height = small_konan.get_size()

def check_collision(x1, y1, w1, h1, x2, y2, w2, h2):
    if (x1 < x2 + w2 and x1 + w1 > x2 and y1 < y2 + h2 and y1 + h1 > y2):
        return True
    return False

def get_winner(obj1, obj2):
    if obj1['type'] == 'konan':
        if obj2['type'] == 'skala':
            return obj1
        elif obj2['type'] == 'nozh':
            return obj2
    elif obj1['type'] == 'skala':
        if obj2['type'] == 'konan':
            return obj2
        elif obj2['type'] == 'nozh':
            return obj1
    elif obj1['type'] == 'nozh':
        if obj2['type'] == 'konan':
            return obj1
        elif obj2['type'] == 'skala':
            return obj2

def calculate_speed_direction(x1, y1, x2, y2, speed):
    dx = x2 - x1
    dy = y2 - y1
    distance = max(math.sqrt(dx**2 + dy**2), 1)  # Используем max чтобы избежать деления на 0
    direction_x = dx / distance
    direction_y = dy / distance
    new_speed_x = direction_x * speed
    new_speed_y = direction_y * speed
    return new_speed_x, new_speed_y

def transform_object(obj, winner):
    old_type = obj['type']
    new_type = winner['type']
    obj['image'] = winner['image'].copy()
    obj['type'] = new_type

    # Обновление счетчиков команд
    team_counts[old_type] -= 1
    team_counts[new_type] += 1

team_counts = {
    'konan': num_konan,
    'skala': num_skala,
    'nozh': num_nozh
}

font = pygame.font.Font(None, 36)

running = True
while running:
    ecran.fill(aq)
    uaqyt.tick(V)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for obj in objects:
        image = obj['image']
        x, y = obj['x'], obj['y']
        dir_x, dir_y = obj['dir_x'], obj['dir_y']
        speed = 1  # Задаем базовую скорость

        ecran.blit(image, (x, y))

        x += dir_x * speed
        y += dir_y * speed

        if x + new_razmer_1 >= razmer[0] or x < 0:
            dir_x *= -1
        if y + new_razmer_2 >= razmer[1] or y < 0:
            dir_y *= -1

        obj['x'], obj['y'] = x, y
        obj['dir_x'], obj['dir_y'] = dir_x, dir_y

        for other_obj in objects:
            if obj != other_obj:
                if check_collision(x, y, width, height, other_obj['x'], other_obj['y'], width, height):
                    if obj['type'] != other_obj['type']:
                        winner = get_winner(obj, other_obj)
                        if winner:
                            x1, y1 = x, y
                            x2, y2 = other_obj['x'], other_obj['y']
                            new_speed_x, new_speed_y = calculate_speed_direction(x1, y1, x2, y2, speed)
                            obj['dir_x'] = -new_speed_x
                            obj['dir_y'] = -new_speed_y
                            transform_object(obj, winner)
                            team_counts[winner['type']] += 1
                            team_counts[obj['type']] -= 1
                    else:
                        x1, y1 = x, y
                        x2, y2 = other_obj['x'], other_obj['y']
                        new_speed_x, new_speed_y = calculate_speed_direction(x1, y1, x2, y2, speed)
                        obj['dir_x'] = -new_speed_x
                        obj['dir_y'] = -new_speed_y

    team_scores_text = []
    for team, count in team_counts.items():
        team_scores_text.append(f"{team}: {count}")
    scores_text = ", ".join(team_scores_text)

    text = font.render(scores_text, True, kok)
    ecran.blit(text, (10, 10))

    # Проверяем условие, когда счетчики двух команд равны 0
    if team_counts['konan'] == 0 and team_counts['skala'] == 0:
        pygame.mixer.music.pause()
        if (fSound):
            finally_sound.play(0)
            fSound = False
        winner_team = 'Эдвард руки-ножницы'
        winner_text = "Игра окончена! Победитель: " + winner_team
        text = font.render(winner_text, True, qyzyl)
        text_rect = text.get_rect(center=(razmer[0] // 2, razmer[1] // 3))
        ecran.blit(small_nozh_end, (350, 270))
        ecran.blit(text, text_rect)
    elif team_counts['konan'] == 0 and team_counts['nozh'] == 0:
        pygame.mixer.music.pause()
        if (fSound):
            finally_sound.play(0)
            fSound = False
        winner_team = 'Skala Джонсон'
        winner_text = "Игра окончена! Победитель: " + winner_team
        text = font.render(winner_text, True, qyzyl)
        text_rect = text.get_rect(center=(razmer[0] // 2, razmer[1] // 3))
        ecran.blit(small_skala_end, (350, 270))
        ecran.blit(text, text_rect)
    elif team_counts['skala'] == 0 and team_counts['nozh'] == 0:
        pygame.mixer.music.pause()
        if (fSound):
            finally_sound.play(0)
            fSound = False
        winner_team = 'КОНАН'
        winner_text = "Игра окончена! Победитель: " + winner_team
        text = font.render(winner_text, True, qyzyl)
        text_rect = text.get_rect(center=(razmer[0] // 2, razmer[1] // 3))
        ecran.blit(small_konan_end, (350, 270))
        ecran.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()
