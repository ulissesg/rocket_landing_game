#!/usr/bin/python

import pygame as pg
import sys, os

pg.init()

DEFAULT_WIDTH = 400
DEFAULT_HEIGHT = 300
WHITE = (255, 255, 255)
background_color = WHITE



'''
Int, Int, [Color] -> screen
Cria screen base do aplicativo.
'''
def create_base_screen(width, height, background=WHITE):
    screen = pg.display.set_mode((width, height))
    screen.fill(background)
    global background_color
    background_color = background
    return screen

screen = create_base_screen(DEFAULT_WIDTH, DEFAULT_HEIGHT)

Font = pg.font.SysFont
Color = pg.color.Color


def big_bang(inic,
             screen=screen,
             on_tick=lambda e: e,
             framerate=28,
             to_draw=lambda e: screen.blit(text("NADA A MOSTRAR. VERIFIQUE SE VOCÊ PASSOU A FUNÇÃO DE DESENHHAR PARA O BIG-BANG", Font("monospace",30),
                                                Color("red"), screen.get_width()), (0, screen.get_height()//2)),
             on_key=lambda e, k: e, \
             on_key_release=lambda e, k: e, \
             on_mouse=lambda e, x, y, ev: e, \
             stop_when=lambda e: False,\
             debug_mode=False,
             debug_font_size = 15):

    # pg.init()
    state = inic
    clock = pg.time.Clock()

    while True:

        pg.display.flip()

        if stop_when(state):
            print(state)
            sys.exit(0)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                print(state)
                sys.exit(0)

            if event.type == pg.KEYDOWN:
                state = on_key(state, event.key)
            elif event.type == pg.KEYUP:
                state = on_key_release(state, event.key)
            elif event.type in [pg.MOUSEBUTTONDOWN, pg.MOUSEBUTTONUP, pg.MOUSEMOTION]:
                x, y = pg.mouse.get_pos()
                state = on_mouse(state, x, y, event.type)

        state = on_tick(state)

        screen.fill(background_color)
        to_draw(state)
        if debug_mode:
            print_state(state, debug_font_size)

        clock.tick(framerate)


def animate(on_tick, framerate=28):
    clock = pg.time.Clock()
    i = 0
    while True:
        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                print(i)
                sys.exit(0)

        screen.fill(WHITE)
        on_tick(i)
        i += 1

        clock.tick(framerate)

# def animate2(on_tick, framerate=28):
#     while True:
#         on_tick(i)
#
#         clock.tick(framerate)


# def print_state(state, screen, debug_font_size):
#     myfont = pg.font.SysFont("monospace", debug_font_size)
#     # text = str(state).split(',')
#     import re
#     text = re.findall('\[[^\]]*\]|\([^\)]*\)|\"[^\"]*\"|\S+', str(state))
#
#     counter = debug_font_size
#     for line in text:
#         label = myfont.render(line, 1, (255, 0, 0))
#         screen.blit(label, (5, counter))
#         counter += debug_font_size
#

def print_state(state, font_size):
    text_img = text(str(state), Font("monospace", font_size), Color("red"), screen.get_width()//2)
    screen.blit(text_img, (5,5))

'''
FUNÇÕES PARA CRIAÇÃO DE TEXTOS
'''

'''
String, Font, Color, Int -> Surface
'''
def text(str, font, color, width):
    def wrap_text(text, font, width):
        """Wrap text to fit inside a given width when rendered.
        :param text: The text to be wrapped.
        :param font: The font the text will be rendered in.
        :param width: The width to wrap to.
        """
        text_lines = text.replace('\t', '    ').split('\n')
        if width is None or width == 0:
            return text_lines

        wrapped_lines = []
        for line in text_lines:
            line = line.rstrip() + ' '
            if line == ' ':
                wrapped_lines.append(line)
                continue

            # Get the leftmost space ignoring leading whitespace
            start = len(line) - len(line.lstrip())
            start = line.index(' ', start)
            while start + 1 < len(line):
                # Get the next potential splitting point
                next = line.index(' ', start + 1)
                if font.size(line[:next])[0] <= width:
                    start = next
                else:
                    wrapped_lines.append(line[:start])
                    line = line[start + 1:]
                    start = line.index(' ')
            line = line[:-1]
            if line:
                wrapped_lines.append(line)
        return wrapped_lines

    def render_text_list(lines, font, colour=(255, 255, 255)):
        """Draw multiline text to a single surface with a transparent background.
        Draw multiple lines of text in the given font onto a single surface
        with no background colour, and return the result.
        :param lines: The lines of text to render.
        :param font: The font to render in.
        :param colour: The colour to render the font in, default is white.
        """
        rendered = [font.render(line, True, colour).convert_alpha()
                    for line in lines]

        line_height = font.get_linesize()
        width = max(line.get_width() for line in rendered)
        tops = [int(round(i * line_height)) for i in range(len(rendered))]
        height = tops[-1] + font.get_height()

        surface = pg.Surface((width, height)).convert_alpha()
        surface.fill((0, 0, 0, 0))
        for y, line in zip(tops, rendered):
            surface.blit(line, (0, y))

        return surface

    lines = wrap_text(str, font, width)
    return render_text_list(lines, font, color)



'''
FUNÇÕES PARA CRIAÇÃO DE IMAGENS E FIGURAS GEOMÉTRICAS
'''

'''
Int, Int, Color -> Surface
'''
def ellipse(width, height, color):
    img = pg.Surface((width, height), pg.SRCALPHA)  # empty image
    pg.draw.ellipse(img, color, (0, 0, width, height))
    return img

'''
Int, Int, Color -> Surface
'''
def rectangle(width, height, color):
    img = pg.Surface((width, height), pg.SRCALPHA)  # empty image
    pg.draw.rect(img, color, (0, 0, width, height))
    return img

'''
Int, Color -> Surface
'''
def circle(radius, color):
    img = pg.Surface((radius*2, radius*2), pg.SRCALPHA)  # empty image
    pg.draw.circle(img, color, (radius, radius), radius)
    return img

'''
Int, Color -> Surface
'''
def square(side, color):
    return rectangle(side, side, color)

# TODO
# def poligono(lista_de_pontos, color):
#     return

'''
Int, Int -> Surface
'''
def transparent_frame(width, height):
    frame = pg.Surface((width, height), pg.SRCALPHA)
    return frame

'''
Surface, Int, Int -> Surface
'''
def scale(img, width, height):
    return pg.transform.scale(img, (width, height))


def rotate(img, angle):
    return pg.transform.rotate(img, angle)

'''
String, [Int, Int, Surface] -> Surface
Carrega imagem de arquivo. Se não for possível carregar, insere uma imagem substituta.
'''
def load_image(file_name, width=100, height=None, replacer=None):
    try:
        img = pg.image.load(file_name)
        if width and height:
            img = scale(img, width, height)
        return img
    except:
        img = replacer if replacer \
                else text("Não foi possível carregar imagem", Font("monospace", 15), Color("red"), width)
        return img

'''
Surface, Surface -> Surface
Coloca uma imagem ao beside da outra
'''
def beside(img1, img2):
    background = transparent_frame(img1.get_width() + img2.get_width(),
                                    max(img1.get_height(), img2.get_height()))
    place_image(img1, background, img1.get_width()//2, background.get_height()//2)
    place_image(img2, background, img1.get_width() + img2.get_width()//2, background.get_height()//2)
    return background


'''
Surface, Surface -> Surface
Coloca uma imagem acima da outra
'''
def above(img1, img2):
    background = transparent_frame(max(img1.get_width(), img2.get_width()),
                               img1.get_height() + img2.get_height())
    place_image(img1, background, background.get_width()//2, img1.get_height()//2)
    place_image(img2, background, background.get_width()//2, img1.get_height() + img2.get_height()//2)
    return background

'''
Surface, Surface -> Surface
Sobrepõe imagens, de modo a facilitar a geração de imagens.
'''
def overlay(img1, img2):
    max_height = max(img1.get_height(), img2.get_height())
    max_width = max(img1.get_width(), img2.get_width())
    background = transparent_frame(max_width, max_height)
    background = place_image(img2, background, max_width//2, max_height//2)
    background = place_image(img1, background, max_width//2, max_height//2)
    return background


def image_width(img):
    return img.get_width()

def image_height(img):
    return img.get_height()

'''
FUNÇÕES DE CRIAÇÃO DE screen E SOBREPOSIÇÕES
'''


'''
Surface, Surface, Int, Int -> Surface		
Coloca uma imagem (tipo pg.Surface) sobre outra na posição x e y, considerando 
a posição da imagem como seu centro.
'''
def place_image(img1, img2, x, y):
    img2.blit(img1, (x - img1.get_width()//2, y - img1.get_height()//2))
    return img2


def display(draw_function, *args):
    '''
    :param draw_function: Funcao que retorna imagem
    :param args:
    :return:
    '''
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit(0)
        pg.display.flip()
        draw_function(*args)

'''
Surface, Int, Int -> void
'''
def place_image_on_screen_and_display(img, x, y):
    display(place_image, img, screen, x, y)



