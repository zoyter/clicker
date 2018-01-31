# -*- coding: utf-8 -*-
import pygame as pyg
import random as rnd
from pygame.locals import *
from class_twindow import *
from class_tsprite import *

def main():
    # Инициализация
    pyg.init()
    pyg.font.init()
    # Создаем окно
    window = TWindow([800,600])
    # Загружаем фон
    window.load_image("data/img/bg01.jpg")
    # Добавляем спрайты
    window.sprites.append(TSprite("data/img/01.png"))
    window.sprites.append(TSprite("data/img/02.png"))

    # Основной цикл игры
    size = [800,600]
    while window.isGame:
        # Обрабатываем события клавиатуры
        for e in pyg.event.get():
            if e.type == QUIT:
                window.isGame = False
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    window.isGame = False
                if e.key == K_1:
                    window.toggle_fullscreen()
                # Переход в состояние паузы и выход из нее
                if e.key == K_p:
                    if window.state == 0:
                        window.state = 2
                    elif window.state == 2:
                        window.state = 0
        # Очистка окна
        window.clear()
        # Обновление всего и вся в окне
        window.update()
        # Визуализация содержимого окна
        window.render()
        # Отображение на экране содержимого окна
        pyg.display.flip()
        # Пауза
        window.clock.tick(60)

    # Выход из pygame
    pyg.quit()
    print("G A M E O V E R")
    # выход из python
    quit()

if __name__ == "__main__":
    main()
