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
recolor = tools.Recolor()
reset = tools.Reset()
eyedropper = tools.Eyedropper()
gradient = tools.Gradient()
toolbar = pygame.Surface((32, 720))
swatch = pygame.Surface((600, 720))
canvas = pygame.Surface((640, 640))
canvas_pos = [72, 40]
rect = [0, 0, 0, 0]
color = (0, 0, 0)


def draw_grid():
    for i in range(40):
        for j in range(40):
            pygame.draw.rect(canvas, canvas_holder[i][j], (i * gap, j * gap, gap, 640 // 40))
    for i in range(40):
        pygame.draw.line(canvas, (181, 181, 181), (i * gap, 0), (i * gap, 640))
        pygame.draw.line(canvas, (181, 181, 181), (0, i * gap), (640, i * gap))


def reset_display():
    screen.fill((40, 40, 40))
    toolbar.fill((83, 83, 83))
    swatch.fill((83, 83, 83))
    canvas.fill((255, 255, 255))
    draw_grid()
    pygame.draw.rect(canvas, (43, 43, 43), rect, 2)
    pencil.draw(toolbar)
    eraser.draw(toolbar)
    reset.draw(toolbar)
    marquee.draw(toolbar)
    recolor.draw(toolbar)
    gradient.draw(toolbar)
    hand.draw(toolbar)
    eyedropper.draw(toolbar)
    screen.blit(canvas, canvas_pos)
    screen.blit(toolbar, (0, 0))
    screen.blit(swatch, (760, 0))


running = True

while running:
    count = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pencil.selected(event.pos, eraser, hand, gradient, marquee, eyedropper, recolor)
                recolor.selected(event.pos, pencil, eraser, hand, gradient, marquee, eyedropper)
                eraser.selected(event.pos, pencil, hand, gradient, marquee, eyedropper, recolor)
                marquee.selected(event.pos, eraser, pencil, hand, gradient, eyedropper, recolor)
                if reset.select is not None:
                    canvas_pos = reset.selected(event.pos, canvas_pos, pencil,
                                                eraser, hand, gradient, marquee, eyedropper, recolor)

                hand.selected(event.pos, eraser, pencil, gradient, eyedropper, marquee, recolor)
                eyedropper.selected(event.pos, eraser, pencil, gradient, hand, marquee, recolor)
                gradient.selected(event.pos, eraser, pencil, eyedropper, hand, marquee, recolor)
                if marquee.select is True:
                    marquee.set_initial(event.pos, canvas_pos)
                if hand.select is True:
                    hand.set_initial(event.pos)
        if pygame.mouse.get_pressed()[0]:

            canvas_holder = pencil.function(event.pos, canvas_holder, canvas_pos, color)
            if gradient.select is True:
                canvas_holder = gradient.function()
            canvas_holder = eraser.function(event.pos, canvas_holder)

            if marquee.select is True:
                rect = marquee.function(event.pos, canvas_pos)
            if hand.select is True:
                canvas_pos = hand.function(event.pos)
                canvas_size = [640, 640]
                gap = canvas_size[0] // 40
                canvas = pygame.Surface(canvas_size)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL:
                if count == 0:
                    count += 1
                    color = eyedropper.function()
                    eyedropper.select = False
                    pencil.select = True
                    pencil.select_()
            eyedropper.unselect()
            if event.key == pygame.K_BACKSPACE:
                marquee.color_selection(color, canvas_holder)
                rect = [0, 0, 0, 0]
            if event.key == pygame.K_DELETE:
                marquee.color_selection(color, canvas_holder, True)
                rect = [0, 0, 0, 0]
        if pygame.key.get_pressed()[pygame.K_LSHIFT] and pygame.key.get_pressed()[pygame.K_d]:
            marquee.unselect_()
            rect = [0, 0, 0, 0]
    reset_display()
    pygame.display.flip()

pygame.quit()
