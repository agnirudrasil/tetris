import pygame
import tools

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Make You own Textures!")
screen.fill((40, 40, 40))
gap = 640 // 40
canvas_holder = [[[255, 255, 255] for i in range(40)] for j in range(40)]
pencil = tools.Pencil()
marquee = tools.Marquee()
eraser = tools.Eraser()
hand = tools.Hand()
eyedropper = tools.Eyedropper()
gradient = tools.Gradient()
zoom = tools.Zoom()
toolbar = pygame.Surface((32, 720))
swatch = pygame.Surface((600, 720))
canvas = pygame.Surface((640, 640))
color = (0, 0, 0)


def draw_grid():
    for i in range(40):
        for j in range(40):
            pygame.draw.rect(canvas, canvas_holder[i][j], (i * (640 // 40), j * (640 // 40), 640 // 40, 640 // 40))
    for i in range(40):
        pygame.draw.line(canvas, (181, 181, 181), (i * gap, 0), (i * gap, 640))
        pygame.draw.line(canvas, (181, 181, 181), (0, i * gap), (640, i * gap))


def reset_display():
    screen.fill((40, 40, 40))
    toolbar.fill((83, 83, 83))
    swatch.fill((83, 83, 83))
    canvas.fill((255, 255, 255))
    draw_grid()
    pencil.draw(toolbar)
    eraser.draw(toolbar)
    marquee.draw(toolbar)
    zoom.draw(toolbar)
    gradient.draw(toolbar)
    hand.draw(toolbar)
    eyedropper.draw(toolbar)
    screen.blit(toolbar, (0, 0))
    screen.blit(canvas, (72, 40))
    screen.blit(swatch, (760, 0))


running = True

while running:
    count = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_pressed()[0]:
            pencil.selected(event.pos, eraser, hand, zoom, gradient, marquee, eyedropper)
            canvas_holder = pencil.function(event.pos, canvas_holder, color)
            canvas_holder = eraser.function(event.pos, canvas_holder)
            eraser.selected(event.pos, pencil, hand, zoom, gradient, marquee, eyedropper)
            marquee.selected(event.pos, eraser, pencil, hand, zoom, gradient, eyedropper)
            hand.selected(event.pos, eraser, pencil, zoom, gradient, eyedropper, marquee)
            eyedropper.selected(event.pos, eraser, pencil, zoom, gradient, hand, marquee)
            gradient.selected(event.pos, eraser, pencil, zoom, eyedropper, hand, marquee)
            zoom.selected(event.pos, eraser, pencil, gradient, eyedropper, hand, marquee)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL:
                if count == 0:
                    count += 1
                    color = eyedropper.function()
                    eyedropper.select = False
                    pencil.select = True
                    pencil.select_()
            eyedropper.unselect()
    reset_display()
    pygame.display.flip()

pygame.quit()
