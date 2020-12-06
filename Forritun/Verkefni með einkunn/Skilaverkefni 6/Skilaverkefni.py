import random
import arcade

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_COIN2 = 0.2
SPRITE_SCALING_LASER = 0.3
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_SPEED = 10


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lárus Ármann Kjartansson")

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.coin2_list = None
        self.bullet_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BURLYWOOD)

    def setup(self):

        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.coin2_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        # Set up the player
        self.score = 0

        # Image from kenney.nl
        self.player_sprite = arcade.Sprite("C:\Git\Skoli-haust-2020\Forritun\Verkefni með einkunn\Skilaverkefni 6\img\character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite("C:\Git\Skoli-haust-2020\Forritun\Verkefni með einkunn\Skilaverkefni 6\img\coin_01.png", SPRITE_SCALING_COIN)
            coin2 = arcade.Sprite("C:\Git\Skoli-haust-2020\Forritun\Verkefni með einkunn\Skilaverkefni 6\img\coin_02.png", SPRITE_SCALING_COIN2)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(120, SCREEN_HEIGHT)

            coin2.center_x = random.randrange(SCREEN_WIDTH)
            coin2.center_y = random.randrange(120, SCREEN_HEIGHT)
            # Add the coin to the lists
            self.coin_list.append(coin)
            self.coin2_list.append(coin2)

        # Set the background color
        arcade.set_background_color(arcade.color.BURLYWOOD)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.coin_list.draw()
        self.coin2_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()

        # Render the text
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        self.player_sprite.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """

        # Create a bullet
        bullet = arcade.Sprite("C:\Git\Skoli-haust-2020\Forritun\Verkefni með einkunn\Skilaverkefni 6\img\kula.png", SPRITE_SCALING_LASER)

        # Position the bullet
        bullet.center_x = self.player_sprite.center_x
        bullet.bottom = self.player_sprite.top

        # Add the bullet to the appropriate lists
        self.bullet_list.append(bullet)

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.coin_list.update()
        self.coin2_list.update()
        self.bullet_list.update()

        # Loop through each bullet
        for bullet in self.bullet_list:

            # Check this bullet to see if it hit a coin
            hit_list = arcade.check_for_collision_with_list(bullet, self.coin_list)
            hit_list = arcade.check_for_collision_with_list(bullet, self.coin2_list)

            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            # For every coin we hit, add to the score and remove the coin
            for coin in hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1
                
            for coin2 in hit_list:
                coin2.remove_from_sprite_lists()
                self.score += 5
            # If the bullet flies off-screen, remove it.
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()