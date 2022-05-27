import pygame
from pygame import *
from abc import ABC, abstractmethod, ABCMeta


class Menu( ABC):
    def __init__ (self, game) :


        self.sky_blue = (135, 206, 250)
        self.game = game
        self.min_width = self.game.WIDTH / 2
        self.min_height = self.game.HEIGTH / 2
        self.font_color = self.game.BLACK
        self.state = 'main'


        self.logo_game = image.load("assets/images/logo_game.png")
        self.title_bg = image.load("assets/images/icons/title_bg.png")
        self.Btn = image.load("assets/images/icons/BTN.png")

    def get_rect(self, rect, posx, posy) :
        Rect = rect.get_rect(midtop = (posx, posy))
        return Rect

    def blit_menu(self, text, tetx_rect) :
        self.game.SCREEN.blit(text, tetx_rect)

    def blit_screen(self):
        display.update()

    def draw_rect(self,color, posx, posy, w, h, border_raduis) :
        return draw.rect(self.game.SCREEN, color, (posx, posy, w, h), border_radius= border_raduis)

    def put_title_game(self) :
        posx, posy = (self.game.WIDTH) / 2, 0
        self.logo_rect = self.get_rect(self.logo_game, posx, posy)
        self.game.SCREEN.blit(self.logo_game, self.logo_rect)


class Main_menu(Menu) :
    def __init__(self, game) :
        Menu.__init__(self, game)
        self.w, self.h = 120, 120
        self.off = self.w / 2

        self.startx, self.starty = self.min_width - 60, self.min_height + 5
        self.themex, self.themey = self.min_width, 525
        self.quitx, self.quity = self.min_width , 585

        self.play_btn = image.load("assets/images/icons/play_btn.png")

    def draw_menu(self) :
        self.game.draw_background()

        self.put_title_game()
        # text
        main_menu = self.game.font_title.render("Main Menu", True, (7,5,111))
        theme = self.game.font_content.render("Theme", True, self.font_color)
        quit_game = self.game.font_content.render("Quit", True, self.font_color)


        #rect 
        main_menu_rect = self.get_rect(main_menu, self.min_width, 237)
        title_bg_rect = self.get_rect(self.title_bg, self.min_width -85, 190)
        play_btn_rect = self.get_rect(self.play_btn, self.min_width, 265)
        self.start_rect = self.draw_rect((255,255,255), self.startx, self.starty, self.w, self.h, 100 )
        self.theme_rect = self.get_rect(self.Btn, self.themex, self.themey)
        self.quit_rect = self.get_rect(self.Btn, self.quitx, self.quity)
        theme_text_rect = theme.get_rect(center = self.theme_rect.center)
        quit_text_rect = quit_game.get_rect(center = self.quit_rect.center)


        #blit
        self.blit_menu(self.play_btn, play_btn_rect)
        self.blit_menu(self.title_bg, title_bg_rect)
        self.blit_menu(main_menu, main_menu_rect)
        self.blit_menu(self.Btn, self.theme_rect)
        self.blit_menu(self.Btn, self.quit_rect)
        self.blit_menu(theme, theme_text_rect)
        self.blit_menu(quit_game, quit_text_rect)
     

    
    def input_menu(self, event_list) :
        for event in event_list :
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                if self.start_rect.collidepoint(mouse.get_pos()) :
                    self.game.btn_click.play()
                    self.state = 'game'
                elif self.theme_rect.collidepoint(mouse.get_pos()) :
                    self.game.btn_click.play()
                    self.state = "theme"
                elif self.quit_rect.collidepoint(mouse.get_pos()) :
                    self.game.btn_click.play()
                    self.state = "quit"
                self.cek_state(event_list)

    def cek_state(self, event_list) :
        if self.state == 'game' and self.game.game_over :
            self.state = 'main'
        if self.state == 'theme' :
            self.game.cur_menu = self.game.theme_menu
        elif self.state == 'game' :
            self.game.playing = True
            self.game.game_over = False
        elif self.state == 'quit' :
            self.game.playing = False
            self.game.running = False

    def update(self, event_list) :
        self.draw_menu()
        self.input_menu(event_list)

class theme(Menu):
    def __init__(self, game) :
        Menu.__init__(self, game)
        self.game = game
        # rect pos
        self.rect_color = self.game.WHITE
        self.w, self.h = 150, 150
        self.theme1x = self.min_width - 200
        self.theme2x = self.min_width + 65
        # quit pos
        self.quitx, self.quity = self.min_width , 585

    def draw_menu(self) :
        self.game.draw_background()

        self.put_title_game()
        #icon
        icon_theme1 = image.load("assets/images/theme1.png")
        icon_theme2 = image.load("assets/images/theme2.jpg")

        # text
        game_theme = self.game.font_title.render("Game Theme", True, (7,5,111))
        quit = self.game.font_content.render("Quit", True, self.font_color)

        #rect
        game_theme_rect = self.get_rect(game_theme, self.min_width, 237)
        title_bg_rect = self.get_rect(self.title_bg, self.min_width -85, 190)
        self.theme1_rect = self.draw_rect(self.rect_color, self.theme1x, self.min_height, self.w, self.h, 8 )
        self.theme2_rect = self.draw_rect(self.rect_color, self.theme2x, self.min_height, self.w, self.h, 8 )
        self.quit_rect = self.get_rect(self.Btn, self.quitx, self.quity)
        quit_text_rect = quit.get_rect(center = self.quit_rect.center)

        #blit
        self.blit_menu(self.title_bg, title_bg_rect)
        self.blit_menu(game_theme, game_theme_rect)
        self.blit_menu(icon_theme1, self.theme1_rect)
        self.blit_menu(icon_theme2, self.theme2_rect)
        self.blit_menu(self.Btn, self.quit_rect)
        self.blit_menu(quit, quit_text_rect)


    def input_menu(self, event_list) :
        for event in event_list :
            if event.type == pygame.MOUSEBUTTONDOWN :
                if Rect(self.theme1_rect).collidepoint(event.pos) :
                    self.game.btn_click.play()
                    self.game.cek_theme = 1
                elif Rect(self.theme2_rect).collidepoint(event.pos) :
                    self.game.btn_click.play()
                    self.game.cek_theme = 2
                if Rect(self.quit_rect).collidepoint(event.pos) :
                    self.game.btn_click.play()
                    self.game.cur_menu = self.game.main_menu
                self.game.cur_menu = self.game.main_menu
                
                self.game.check_theme()
                if self.game.theme_update :
                    self.game.get_background()

    def update(self,event_list) :
        self.draw_menu()
        self.input_menu(event_list)

class Game_Over(Menu):
    def __init__(self, game) :
        Menu.__init__(self, game)
        self.game_over_image = image.load("assets/images/game_over.png")
        self.game_over_posx, self.game_over_posy = self.min_width, 170

        self.quitx, self.quity = self.min_width , 585

    def draw_menu(self) :
        self.game.draw_background()

        self.put_title_game()
        # text
        score = self.game.font_title.render("Score    :    {}".format(self.game.end_score_game), True, self.font_color)
        level = self.game.font_title.render("Level    :    {}".format(self.game.end_level_game), True, self.font_color)
        info = self.game.font_content.render("quit to main menu", True, self.font_color)
        quit = self.game.font_content.render("quit", True, self.font_color)

        #rect
        game_over_rect = self.get_rect(self.game_over_image, self.min_width, self.game_over_posy)
        score_rect = self.get_rect(score, self.min_width, self.game_over_posy + 190)
        level_rect = self.get_rect(level, self.min_width, self.game_over_posy + 240)
        info_rect = self.get_rect(info, self.quitx, self.quity-30)
        self.btn = self.get_rect(self.Btn, self.quitx, self.quity)
        self.quit_rect = quit.get_rect(center = self.btn.center)

        #blit
        self.blit_menu(self.game_over_image, game_over_rect)
        self.blit_menu(score, score_rect)
        self.blit_menu(level, level_rect)
        self.blit_menu(info, info_rect)
        self.blit_menu(self.Btn, self.btn)
        self.blit_menu(quit, self.quit_rect)

    def input_menu(self, event_list) :
        for event in event_list :
            if event.type == pygame.MOUSEBUTTONDOWN :
                if Rect(self.btn).collidepoint(event.pos) :
                    self.game.btn_click.play()
                    self.game.game_over = False
                    self.game.cur_menu = self.game.main_menu

    def update(self, event_list) :
        self.draw_menu()
        self.input_menu(event_list)
