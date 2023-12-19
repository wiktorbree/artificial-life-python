import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 800, 800

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Artificial Life")

clock = pygame.time.Clock()

particles = []

def draw(x, y, color, size):
    pygame.draw.circle(win, color, (x, y), size)

def particle(x, y, color):
    return {"x": x, "y": y, "vx": 0, "vy": 0, "color": color}

def random_pos():
    return random.randint(50, 750)

def create(number, color):
    group = []
    for i in range(number):
        x, y = random_pos(), random_pos()
        group.append(particle(x, y, color))
        particles.append(group[i])
    return group

def rule(particles1, particles2, g):
    for a in particles1:
        fx, fy = 0, 0
        for b in particles2:
            dx = a["x"]-b["x"]
            dy = a["y"]-b["y"]
            d = math.sqrt(dx*dx + dy*dy)

            if 0 < d < 80:
                F = g * 1/d
                fx += (F * dx)
                fy += (F * dy)
        
        a["vx"] = (a["vx"] + fx) * 0.5
        a["vy"] = (a["vy"] + fy) * 0.5
        a["x"] += a["vx"]
        a["y"] += a["vy"]

        if a["x"] <= 0 or a["x"] >=  800:
            a["vx"] *= -1
        if a["y"] <= 0 or a["y"] >=  800:
            a["vy"] *= -1

yellow = create(300, (255, 255, 0))
red = create(300, (255, 0, 0))
green = create(200, (0, 255, 0))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    win.fill((0, 0, 0))

    rule(red, red, -0.1)
    rule(yellow, red, 0.15)
    rule(green, green, -0.7)
    rule(green, red, -0.2)
    rule(red, green, -0.1)

    for particle in particles:
        draw(int(particle['x']), int(particle['y']), particle['color'], 4)

    clock.tick(60)
    pygame.display.update()

pygame.quit()
