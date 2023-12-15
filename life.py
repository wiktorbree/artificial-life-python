import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 500, 500

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Artificial Life")

clock = pygame.time.Clock()

particles = []

def draw(x, y, color, size):
    pygame.draw.circle(win, color, (x, y), size)

def particle(x, y, color):
    return {"x": x, "y": y, "vx": 0, "vy": 0, "color": color}

def random_pos():
    return random.randint(50, 450)

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

            if d > 0:
                F = g * 1/d
                fx += (F * dx)
                fy += (F * dy)
        
        a["vx"] = a["vx"] + fx
        a["vy"] = a["vy"] + fy
        a["x"] += a["vx"]
        a["y"] += a["vy"]


running = True

yellow = create(3, (255, 255, 0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    win.fill((0, 0, 0))
    rule(yellow, yellow, -1)
    for particle in particles:
        draw(int(particle['x']), int(particle['y']), particle['color'], 2)

    
    clock.tick(60)
    pygame.display.update()

pygame.quit()

    