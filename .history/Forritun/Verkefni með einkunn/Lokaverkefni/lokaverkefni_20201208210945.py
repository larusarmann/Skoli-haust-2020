import random #Importar
import arcade #Importar
import os #Importar

SPRITE_SCALING = 0.5
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Lárus"

VIEWPORT_MARGIN = 40
RIGHT_MARGIN = 150

MOVEMENT_SPEED = 5
JUMP_SPEED = 14
GRAVITY = 0.5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """
        Initializer
        """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lokaverkefni Lárus")

        # Sprite lists
        self.coin_list = None
        self.player_list = None
        self.wall_list = None
        self.flag=True
        self.score = 0

        # Set up the player
        self.player_sprite = None

        # This variable holds our simple "physics engine"
        self.physics_engine = None

        # Manage the view port
        self.view_left = 0
        self.view_bottom = 0

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

        for i in range(7):

            # Create the coin instance
            coin = arcade.Sprite("C:\Git\Skoli-haust-2020\Forritun\Verkefni með einkunn\Lokaverkefni\images\coinGold.png", SPRITE_SCALING / 2)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(600)

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
        
    def on_draw(self):
        arcade.start_render()

        if self.flag:
            arcade.set_background_color(arcade.color.RED)
            arcade.draw_text(" Lárus Ármann Kjartansson\n Náðu fimm peningum til að vinna leikin \n Ýttu á Q til að hefja leik", 10,300, arcade.color.WHITE, 24)
            arcade.draw_text("Lárus Ármann ",self.view_left+10,self.view_bottom+10, arcade.color.CHERRY, 14)
        elif self.score >=5 and self.flag==False:
            arcade.set_background_color(arcade.color.BUBBLES)
            arcade.draw_text("Leik lokið ",self.view_left+200,self.view_bottom+300, arcade.color.CHERRY, 44)
            arcade.draw_text("Lárus Ármann ",self.view_left+10,self.view_bottom+10, arcade.color.CHERRY, 14)
        else:
            arcade.set_background_color(arcade.color.AMAZON)
            self.wall_list.draw()
            self.player_list.draw()
            arcade.draw_text(f"stig: {self.score}", self.player_sprite.center_x-15,self.player_sprite.center_y+30, arcade.color.WHITE, 14)
            arcade.draw_text("Lárus Ármann ",self.view_left+10,self.view_bottom+10, arcade.color.CHERRY, 14)
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
        if key == arcade.key.Q:
            self.flag=False
        else:
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
        self.physics_engine.update()
        self.coin_list.update()
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        if len(hit_list)>0:
            for pening in hit_list:
                pening.remove_from_sprite_lists()
                self.score=self.score+1


        # --- Manage Scrolling ---

        # Keep track of if we changed the boundary. We don't want to call the
        # set_viewport command if we didn't change the view port.
        changed = False

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        # Make sure our boundaries are integer values. While the view port does
        # support floating point numbers, for this application we want every pixel
        # in the view port to map directly onto a pixel on the screen. We don't want
        # any rounding errors.
        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        # If we changed the boundary values, update the view port to match
        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left - 1,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom - 1)

def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()