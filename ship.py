import pygame
from pygame.sprite import Sprite


class Ship(Sprite):


    def __init__(self, ai_settings, screen):
        """initialize the ship and set its starting position"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp') #returns the surface representing the ship
        self.rect = self.image.get_rect()#gives image's rectangle
        self.screen_rect = screen.get_rect() #gives screen's rectangle

        #start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx # x coordinate of ship center = x coordinate of screen center
        self.rect.bottom = self.screen_rect.bottom  #image's bottom aligned with screen's bottom


        #store a decimal value for the ship's centerx
        self.center = float(self.rect.centerx)


        #movement flag
        self.moving_right = False
        self.moving_left = False




    def update(self):
        """update the ship's position based on the movement flag."""
        #update the ship's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor #move the ship to the right.
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #update rect object from self.center.
        self.rect.centerx = self.center



    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image,self.rect)  #display the image on the screen at the position specified by self.rect


    def center_ship(self):
        """center the ship on the screen"""
        self.center = self.screen_rect.centerx
