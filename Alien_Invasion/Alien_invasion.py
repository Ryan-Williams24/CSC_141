import pygame
from settings import Settings
from ship import Ship
from game_functions import GameFunctions
from game_stats import GameStats
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    clock = pygame.time.Clock()  # Add this
    ship = Ship(ai_settings, screen)
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    game_functions = GameFunctions(ai_settings, screen, ship, stats, sb)

    while True:
        game_functions.check_events()
        if stats.game_active:
            ship.update()
            game_functions.update_bullets()
            game_functions.update_aliens()
        game_functions.update_screen()
        clock.tick(60)  # Limit the game to 60 frames per second

if __name__ == '__main__':
    run_game()