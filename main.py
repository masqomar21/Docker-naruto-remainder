from pygame import *
from src.game import *


init()

timer = time.Clock()
# Initialize the screen

display.set_caption("remaider game")
# mouse.set_visible(False)

game = Game()
# time.set_timer(USEREVENT, 1000)

while game.running :
    timer.tick(game.FPS)
    game.SCREEN.fill(game.BLACK)


    event_list = event.get()
    for even in event_list :
        if even.type == QUIT:
            game.running = False
    if game.playing :
        game.update(event_list)
    else :
        if game.game_over :
            game.cur_menu = game.game_over_page
        game.cur_menu.update(event_list)

    display.update()
    display.flip()
quit()