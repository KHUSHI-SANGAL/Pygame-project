import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    # initialize game and create a screen object called surface (each element in the game is a surface like alien , ships all are surface)
    pygame.init() #initialize pygame, settings and scree object
    ai_settings = Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  #to create display window called screen with dimensions width x height in pixels
    pygame.display.set_caption("Alien Invasion")


    #make the play button
    play_button = Button(ai_settings, screen, "Play")

    #create an instance to store game statistics and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #make a ship
    ship = Ship(ai_settings, screen)

    #make a group to bullets and aliens
    bullets = Group()
    aliens = Group()

    #create the fleet of aliens
    gf.create_fleet(ai_settings, screen,ship, aliens)



    #start the main loop for the run_game
    while True:

        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen,stats, sb, ship, aliens,  bullets)
            gf.update_aliens(ai_settings,screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)




run_game()
