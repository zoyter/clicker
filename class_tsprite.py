import random as rnd
import pygame as pyg
from pygame.locals import *
from common import *

class TSprite(pyg.sprite.Sprite):
    def __init__(self, fname,x = 10,y = 10):
        super().__init__()
        # Загрузка картинки
        self.image, self.rect = loadimg(fname)
        # Цвет текста под спрайтом
        self.text_color = rndcolor()
        # Количество жизней
        self.life = 10
        # Высота строки графического интерфейса (т.е. наш спрайт должен быть ниже этого интерфейса)
        self.GUI_Height = 30
        # Задаем шрифт, которым будет выводится информация
        self.font = pyg.font.Font("data/font/Ru.ttf", 12)
        # получаем экран, на котором будет рисоваться спрайт
        self.screen = pyg.display.get_surface()
        # Сброс позиции вывода спрайта
        self.rnd_pos()

    def  rnd_pos(self):
        """ Случайная позиция спрайта
        """
        self.rect.x = rnd.randint(self.GUI_Height, self.screen.get_width() - self.rect.width)
        self.rect.y = rnd.randint(0, self.screen.get_height() - self.rect.height)

    def print_life(self):
        # формируем текстовую строку с количеством жизней
        t = str(self.life)
        # генерируем картинку с текстом
        text = self.font.render(t,True,self.text_color)
        # позиционируем надпись под картинкой спрайта
        x = self.rect.x + self.rect.width //2 - text.get_width() //2
        y = self.rect.y + self.rect.height
        # отрисовываем текст
        self.screen.blit(text,[x,y])        

    def render(self):
        """ Отрисовка спрайта
        """
        # рисуем сам спрайт
        self.screen.blit(self.image,[self.rect.x,self.rect.y])
        # рисуем его жизни
        self.print_life()

    def update(self):
        """ Обновление состояния спрайта
            например, можно его тут подвигать и т.п.
        """
        # Это переменная в которой будет храниться результат анализа
        # r=0, значит, никто не наехал на спрайт и спрайт не улетел за границы окна
        # r=1, значит, на спрайт наехали мышкой
        # r=-1, значит, спрайт улетел за границы окна
        r = 0
        self.rect.y -= 5
        if self.isClicked() == True:
            self.rnd_pos()
            self.rect.y = self.screen.get_height()
            r = 1
        if self.rect.y + self.rect.height < 0:
            self.rnd_pos()
            self.rect.y = self.screen.get_height()
            r = -1
        return r
            

    def isClicked(self):
        """ Наехали мышкой на спрайт?
        """
        # Считаем, что не наехали
        flag = False
        # Получаем координаты мыши
        pos = pyg.mouse.get_pos()
        # Смотрим попал-ли курсор в спрайт
        lb = pos[0] >= self.rect.x
        rb = pos[0] <= self.rect.x+ self.rect.width
        tb = pos[1] >= self.rect.y
        bb = pos[1] <= self.rect.y+ self.rect.height        
        # Если попал, то    
        if lb and rb and tb and bb:
            # поднимает флаг того, что наехали на спрайт мышкой
            flag = True
        # возвращаем флаг
        return flag
