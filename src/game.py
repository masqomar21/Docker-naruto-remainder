from os import *
from time import *
from random import *
import cv2

import pygame
from pygame import *

from src.cards import *
from src.menu import *
from src.music import *


class Game:
    def __init__(self):
        #font family
        self.WIDTH, self.HEIGTH = 1180, 700

        self.FPS = 24
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGTH))

        self.font_title = font.Font("assets/font/njnaruto.ttf", 44)
        self.font_content = font.Font("assets/font/njnaruto.ttf", 24)

        # leveling and score
        self.level = 1
        self.__score = 0
        self.score_adding = 10
        self.level_complete = False
        self.game_over = False
        self.playing, self.running = False, True
        self.end_score_game = 0
        self.end_level_game = self.level
       
       #theme
        self.cek_theme = 1
        self.cek_start = False
    
        #card position
        self.img_w, self.img_h = 100, 100
        self.pad = 15
        self.margin_top = 160
        self.cols = 4
        self.rows = 2

        #flip & timing
        self.flipped = []
        self.frame_count = 0
        self.block_game = False

        #countdown time
        self.time = self.level * 30
        self.back_up_time = 1 * 30
        self.time_counter = 0
        self.end_time = False
        
        self.get_background()
        self.theme_update = False

        #color
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GRY = (128, 128, 128)

        #menu
        self.main_menu = Main_menu(self)
        self.theme_menu = theme(self)
        self.game_over_page = Game_Over(self)
        self.cur_menu = self.main_menu

        #music
        self.bg_music = Music("assets/sounds/bg-music.mp3")
        self.bg_music.volchange(0.3)

        #sound effect
        self.btn_click = sound_effect("assets/sounds/btn/4.wav")
        self.false_cards = sound_effect("assets/sounds/btn/6.mp3")
        self.true_cards = sound_effect("assets/sounds/btn/5.wav")
        self.level_complete_sound = sound_effect("assets/sounds/btn/next_level.mp3")
        self.game_over_sound = sound_effect("assets/sounds/gameover.mp3")
        self.start_level = sound_effect("assets/sounds/katon.mp3")
        

        self.time_reset()

        self.cek = False
        self.h = 240
        self.w = 470

        self.img_level_complete = pygame.image.load("assets/images/level_complete.png")
        self.cek_page_complete = False

    def add_score(self):
        self.__score += self.score_adding

    def min_score(self):
        if self.__score <= 0 :
            self.__score = 0
        else :
            self.__score -= 1

    def view_score(self):
        return self.__score

    def game_init(self):
        self.check_theme()
        #card
        self.card_list = [f for f in listdir("assets/images/"+self.theme+"/cards") if path.join("assets/images/"+self.theme+"/cards", f)]
        self.card_grup = pygame.sprite.Group()
        self.generete_level(self.level)
     
    def update(self, event_list):
        if self.level == 1 and not self.cek_start :
            self.game_init()
            self.start_level.play()
            self.cek_start = True
        self.draw()
        self.check_theme()
        self.input_user(event_list)
        self.cek_complete(event_list)
        
    def cek_complete(self, event_list):
        if not self.end_time :
            self.coundown()
            if not self.block_game :
                for event in event_list :
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        for card in self.card_grup :
                            if card.rect.collidepoint(event.pos)  :
                                if self.cek_page_complete :
                                    self.cek_page_complete = False
                                else :
                                    self.btn_click.play()
                                    
                                    if not card.shown :
                                        self.flipped.append(card.name)
                                        card.show()
                                        if len(self.flipped) == 2 :
                                            if self.flipped[0] != self.flipped[1] :
                                                self.block_game = True
                                            else :
                                                self.add_score()
                                                self.flipped = [] 
                                                for card in self.card_grup :
                                                    if card.shown :
                                                        self.level_complete = True
                                                        self.cek = True
                                                        self.time_reset()
                                                    else :
                                                        self.level_complete = False
                                                        self.cek = False
                                                        break
                                                if self.level_complete :
                                                    self.level_complete_sound.play()
            else :
                self.frame_count += 1
                if self.frame_count == self.FPS :
                    self.min_score()
                    self.false_cards.play()
                    self.frame_count = 0
                    self.block_game = False

                    for card in self.card_grup :
                        if card.name in self.flipped :
                            card.hide()
                    self.flipped = []
                else :
                    for event in event_list :
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                            for card in self.card_grup :
                                if card.rect.collidepoint(event.pos)  :
                                    if not card.shown :
                                        self.min_score()
                                        self.false_cards.play()
                                        self.frame_count = 0
                                        self.block_game = False

                                        for card in self.card_grup :
                                            if card.name in self.flipped :
                                                card.hide()
                                        self.flipped = []
        else :
            self.end_score_game = self.view_score()
            self.end_level_game = self.level
            self.game_over = True
            self.playing = False
            self.game_reset()

    def game_reset(self):
        self.level = 1
        self.__score = 0
        self.level_complete = False
        self.playing, self.running = False, True
        self.end_time = False
        self.game_init()
        
        
    def input_user(self,event_list):
        for event in event_list :
            if event.type == pygame.MOUSEBUTTONDOWN :
                if self.btn_rect.collidepoint(event.pos) :
                    #fungsi sementara (langsung game over)
                    self.end_score_game = self.view_score()
                    self.end_level_game = self.level
                    self.game_over = True
                    self.playing = False
                    self.game_reset()
                if self.level_complete :
                    if self.btn_next_level.collidepoint(event.pos) :
                        self.cek = True
                        self .time_reset()
                        self.level += 1
                        self.time = self.level * 30
                        self.start_level.play()
                        if self.level > 5 :
                            self.level = 1
                            self.game_reset()
                        self.generete_level(self.level)
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE and self.level_complete :
                    self.playing = False
        # self.coundown()

    def generete_level(self, level):
        self.card = self.random_select_card(self.level)
        self.level_complete = False
        self.rows = self.level +1
        self.cols= 4
        self.generate_card(self.card)
    
    def generate_card(self, cards):
        self.cols = self.rows = self.cols if self.cols >= self.rows else self.rows
        
        CARD_W = (self.img_w * self. cols + self.pad *(self.cols - 1))
        LEFT_MARGIN = RIGHT_MARGIN = (self.WIDTH - CARD_W) // 2

        self.card_grup.empty()
        
        for i in range(len(cards)) :
            posx = LEFT_MARGIN + ((self.img_w + self.pad) * (i % self.cols))
            posy = self.margin_top + (i // self.rows * (self.img_h + self.pad))
            card  = Cards(cards[i], posx, posy, self.theme)
            self.card_grup.add(card)
 


    def random_select_card(self, level):
        card = sample(self.card_list, (self.level + self.level +2))
        copy_card = card.copy()
        card.extend(copy_card)
        shuffle(card)
        return card

    def coundown(self):
        self.time_counter += 1
        if not self.level_complete :
            if self.time_counter % self.FPS == 0 :
                self.time -= 1
                mins, secs = divmod(self.time, 60)
                self.time_format = "%02d:%02d" % (mins, secs)
                print("time left : ",self.time_format, end = "\r")
                self.time_counter = 0
                if self.time == 0 :
                    self.time_counter = 0
                    self.end_time = True
                    self.time = self.back_up_time

    def time_reset(self):
        self.time_counter = 0
        self.time_format = "%02d:%02d" % (0, 0)
        self.end_time = False

       
    def check_theme(self) :
        self.theme_update = False
        if self.cek_theme == 1 :
            self.theme = "jhutsu"
            self.theme_update = True
        elif self.cek_theme == 2 :
            self.theme = "ciby"
            self.theme_update = True


    def get_background(self):
        self.check_theme()
        self.img = cv2.imread("assets/images/"+self.theme+"/bg.png")
        self.img = cv2.resize(self.img,dsize=(self.WIDTH, self.HEIGTH))
        self.success = True
        self.shape = self.img.shape[1::-1]


    def draw_background(self):
        if self.success :
            self.SCREEN.blit(image.frombuffer(self.img.tobytes(), self.shape, 'BGR'), (0, 0))
        else :
            self.get_background()


    def level_complete_page(self):
        # self.nex_level_sound()
        posx, posy = self.WIDTH // 2, 50
        self.level_complete_page_rect = self.img_level_complete.get_rect(midtop = (posx, posy))
        self.btn_next_level = draw.rect(self.SCREEN, (0, 0, 0), ((self.WIDTH // 2)-150, (self.HEIGTH // 2) + 85, 135, 60), border_radius=15)
        self.SCREEN.blit(self.img_level_complete, self.level_complete_page_rect)

    def draw (self):
        if self.cek :
            if self.level == 2 :
                self.h = 350
            elif self.level == 3 :
                self.h = 465
            elif self.level == 4 :
                self.w = 580
            elif self.level == 5 :
                self.w = 690

            print(self.level)
            self.cek = False

        self.draw_background()
        self.Btn = image.load("assets/images/icons/BTN.png")
        self.title_bg = image.load("assets/images/icons/title_bg.png")
        self.benner = image.load("assets/images/icons/benner.png")

        self.card_backgrund = draw.rect(self.SCREEN, self.GRY, ((self.WIDTH - self.w)/2, 150, self.w, self.h), border_radius= 15)
        #text
        title_bg_rect  = self.title_bg.get_rect(midtop = ((self.WIDTH - 60) // 2, 0))
        benner_rect = self.benner.get_rect(midtop = (self.WIDTH -141, 17))

        level_text = self.font_content.render("Level: ", True, (self.BLACK))
        level_rect = level_text.get_rect(midtop = (self.WIDTH -141, 97))
        level_value = self.font_content.render(str(self.level), True, (self.BLACK))
        level_value_rect = level_value.get_rect(midtop = (self.WIDTH -141, 129))

        time_text = self.font_title.render(self.time_format, True, (self.BLACK))
        time_rect = time_text.get_rect(midtop = (self.WIDTH // 2 , 40))

        score_text = self.font_content.render("Score: ", True, (self.BLACK))
        score_rect = score_text.get_rect(midtop = (self.WIDTH -141, 195))
        score_value = self.font_content.render(str(self.__score), True, (self.BLACK))
        score_value_rect = score_value.get_rect(midtop = (self.WIDTH - 141, 225))

        self.btn_rect = self.Btn.get_rect(topleft = (9, 9))
        quit_text = self.font_content.render("Quit", True, (self.BLACK))
        quit_rect = quit_text.get_rect(center = self.btn_rect.center)
        
        # self.SCREEN.blit(title_text, title_rect)
        self.SCREEN.blit(self.Btn, self.btn_rect)
        self.SCREEN.blit(quit_text, quit_rect)
        self.SCREEN.blit(self.title_bg, title_bg_rect)
        self.SCREEN.blit(self.benner, benner_rect)
        self.SCREEN.blit(level_text, level_rect)
        self.SCREEN.blit(level_value, level_value_rect)
        self.SCREEN.blit(time_text, time_rect)
        self.SCREEN.blit(score_text, score_rect)
        self.SCREEN.blit(score_value, score_value_rect)
        # self.SCREEN.blit(info_text, info_rect)

        if self.level == 5 :
            self.img_level_complete = image.load("assets/images/level_complete.png")

        #draw card
        self.card_grup.draw(self.SCREEN)
        # self.card_backgrund = draw.rect(self.SCREEN, self.GRY, ((self.WIDTH - self.w)/2, 150, self.w, self.h), border_radius= 15)
        self.card_grup.update()

        if self.level_complete :
            # self.nex_level_sound()
            self.level_complete_page()
            self.cek_page_complete = True

