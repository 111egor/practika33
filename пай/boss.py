import pygame
from pygame.sprite import Sprite

class Boss(Sprite):
    """A class to represent the boss alien."""
    
    def __init__(self, ai_settings, screen):
        super(Boss, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        self.image = pygame.image.load('bosss.png')  
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        self.health = 10  
        self.speed = ai_settings.alien_speed_factor * 0.5  
        
        self.direction = 1  
        
    def check_edges(self):
        """Return True if boss hits edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        return False
        
    def update(self):
        """Update the boss's position."""
        self.x += (self.speed * self.direction)
        self.rect.x = self.x
        
        if self.check_edges():
            self.direction *= -1
            self.y += 20  
            self.rect.y = self.y
            
    def blitme(self):
        """Draw the boss at its current location."""
        self.screen.blit(self.image, self.rect)
