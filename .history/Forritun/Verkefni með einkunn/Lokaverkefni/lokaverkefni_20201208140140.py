"""
Show how to do enemies in a platformer

Artwork from: http://kenney.nl
Tiled available from: http://www.mapeditor.org/

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_enemies_in_platformer
"""
import random
import arcade
import os

SPRITE_SCALING = 0.5
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Enemies in a Platformer Example"

VIEWPORT_MARGIN = 40
RIGHT_MARGIN = 150

INSTRUCTIONS_PAGE_0 = 0
INSTRUCTIONS_PAGE_1 = 1
GAME_RUNNING = 2
GAME_OVER = 3

MOVEMENT_SPEED = 5
JUMP_SPEED = 14
GRAVITY = 0.5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """
        Initializer
        """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.wall_list = None
        self.enemy_list = None
        self.player_list = None
        self.coin_list = None
        self.score = None
        self.
        self.current_state = INSTRUCTIONS_PAGE_0

        self.player_sprite = None
        self.physics_engine = None
        self.view_left = 0
        self.view_bottom = 0
        self.game_over = False
        
        self.instructions = []
        texture = arcade.load_texture("C:\Git\Skoli-haust-2020\Forritun\Verkefni með einkunn\Lokaverkefni\Senur\instructions_0.png")
        self.instructions.append(texture)

    def setup(self):
        """ Set up the game and initialize the variables. """


        self.wall_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite("C:/Git/Skoli-haust-2020/Forritun/Verkefni með einkunn/Lokaverkefni/images/rpgTile019.png", SPRITE_SCALING)

            wall.bottom = 0
            wall.left = x
            self.wall_list.append(wall)

        # Draw the platform
        for x in range(SPRITE_SIZE * 3, SPRITE_SIZE * 8, SPRITE_SIZE):
            wall = arcade.Sprite("C:/Git/Skoli-haust-2020/Forritun/Verkefni með einkunn/Lokaverkefni/images/rpgTile019.png", SPRITE_SCALING)

            wall.bottom = SPRITE_SIZE * 3
            wall.left = x
            self.wall_list.append(wall)

        # Draw the crates
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE * 5):
            wall = arcade.Sprite("C:/Git/Skoli-haust-2020/Forritun/Verkefni með einkunn/Lokaverkefni/images/boxCrate_double.png", SPRITE_SCALING)

            wall.bottom = SPRITE_SIZE
            wall.left = x
            self.wall_list.append(wall)

        for i in range(50):

            # Create the coin instance
            coin = arcade.Sprite("C:\Git\Skoli-haust-2020\Forritun\Verkefni með einkunn\Lokaverkefni\images\coinGold.png", SPRITE_SCALING / 3)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)
        # -- Draw an enemy on the ground
        enemy = arcade.Sprite("C:/Git/Skoli-haust-2020/Forritun/Verkefni með einkunn/Lokaverkefni/images/character_zombie_idle.png", SPRITE_SCALING)

        enemy.bottom = SPRITE_SIZE
        enemy.left = SPRITE_SIZE * 2

        # Set enemy initial speed
        enemy.change_x = 2
        self.enemy_list.append(enemy)

        # -- Draw a enemy on the platform
        enemy = arcade.Sprite("C:/Git/Skoli-haust-2020/Forritun/Verkefni með einkunn/Lokaverkefni/images/character_zombie_idle.png", SPRITE_SCALING)

        enemy.bottom = SPRITE_SIZE * 4
        enemy.left = SPRITE_SIZE * 4

        # Set boundaries on the left/right the enemy can't cross
        enemy.boundary_right = SPRITE_SIZE * 8
        enemy.boundary_left = SPRITE_SIZE * 3
        enemy.change_x = 2
        self.enemy_list.append(enemy)

        # -- Set up the player
        self.player_sprite = arcade.Sprite("C:/Git/Skoli-haust-2020/Forritun/Verkefni með einkunn/Lokaverkefni/images/character1.png", SPRITE_SCALING)
        self.player_list.append(self.player_sprite)

        # Starting position of the player
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 270

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             gravity_constant=GRAVITY)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)


    def draw_game_over(self):
        """
        Draw "Game over" across the screen.
        """
        output = "Game Over"
        arcade.draw_text(output, 240, 400, arcade.color.WHITE, 54)

        output = "Click to restart"
        arcade.draw_text(output, 310, 300, arcade.color.WHITE, 24)
        
    def on_draw(self):
        arcade.start_render()

        if self.flag:
            arcade.set_background_color(arcade.color.BLUE)
            arcade.draw_text("Lárus Ármann Kjartansson\n Ýttu á Q til að hefja leik", 10, 300, arcade.color.WHITE, 24)
        elif self.score >=3 and self.flag==False:
            arcade.set_background_color(arcade.color.BUBBLES)
            arcade.draw_text("Leik lokið ",self.view_left+200,self.view_bottom+300, arcade.color.CHERRY, 44)
        else:
            arcade.set_background_color(arcade.color.AMAZON)
            self.wall_list.draw()
            self.player_list.draw()
            arcade.draw_text(f"stig: {self.score}", self.player_sprite.center_x-15,self.player_sprite.center_y+30, arcade.color.WHITE, 14)
            self.coin_list.draw()
            
    def draw_game(self):
        """
        Draw all the sprites, along with the score.
        """
        # Draw all the sprites.
        self.player_list.draw()
        self.coin_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        
    def on_key_press(self, key, modifiers):
        """
        Called whenever the mouse moves.
        """
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """
        Called when the user presses a mouse button.
        """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Update the player based on the physics engine
        if not self.game_over:
            # Move the enemies
            self.enemy_list.update()

            # Check each enemy
            for enemy in self.enemy_list:
                # If the enemy hit a wall, reverse
                if len(arcade.check_for_collision_with_list(enemy, self.wall_list)) > 0:
                    enemy.change_x *= -1
                # If the enemy hit the left boundary, reverse
                elif enemy.boundary_left is not None and enemy.left < enemy.boundary_left:
                    enemy.change_x *= -1
                # If the enemy hit the right boundary, reverse
                elif enemy.boundary_right is not None and enemy.right > enemy.boundary_right:
                    enemy.change_x *= -1

            # Update the player using the physics engine
            self.physics_engine.update()

            # See if the player hit a worm. If so, game over.
            if len(arcade.check_for_collision_with_list(self.player_sprite, self.enemy_list)) > 0:
                self.current_state = GAME_OVER
                self.set_mouse_visible(True)

                self.draw_game()
                self.draw_game_over()

def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()