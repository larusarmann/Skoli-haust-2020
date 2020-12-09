import random #Importar
import arcade #Importar
import os #Importar

SPRITE_SCALING = 0.5 # setur stærðina
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING) # margfaldar stærð með skalanum

SCREEN_WIDTH = 800 #lengd skjáar
SCREEN_HEIGHT = 600 #hæð skjáar
SCREEN_TITLE = "Lárus" #Titill á skjá

VIEWPORT_MARGIN = 40 #
RIGHT_MARGIN = 150

MOVEMENT_SPEED = 5 #hraði leiks
JUMP_SPEED = 14 #hopphraði
GRAVITY = 0.5 #Þyngdarafl


class MyGame(arcade.Window): #býr til Klasa
    def __init__(self):#initalizar klasan
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lokaverkefni Lárus")
        self.coin_list = None # peninga listi
        self.player_list = None # player listi
        self.wall_list = None # veggja listi
        self.flag = True # setur Flagið default á True
        self.score = 0 #setur byrjunar score = 0
        self.player_sprite = None 
        self.physics_engine = None 
        self.view_left = 0
        self.view_bottom = 0 #

    def setup(self):
        self.wall_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite("C:/Git/Skoli-haust-2020/Forritun/Verkefni með einkunn/Lokaverkefni/images/rpgTile019.png", SPRITE_SCALING) #kallar í myndina

            wall.bottom = 0 
            wall.left = x
            self.wall_list.append(wall)

        # Draw the platform
        for x in range(SPRITE_SIZE * 3, SPRITE_SIZE * 8, SPRITE_SIZE):
            wall = arcade.Sprite("C:/Git/Skoli-haust-2020/Forritun/Verkefni með einkunn/Lokaverkefni/images/rpgTile019.png", SPRITE_SCALING)#kallar í myndina

            wall.bottom = SPRITE_SIZE * 3
            wall.left = x
            self.wall_list.append(wall)

        # Draw the crates
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE * 5): #teiknar kassana
            wall = arcade.Sprite("C:/Git/Skoli-haust-2020/Forritun/Verkefni með einkunn/Lokaverkefni/images/boxCrate_double.png", SPRITE_SCALING)#kallar í myndina

            wall.bottom = SPRITE_SIZE
            wall.left = x
            self.wall_list.append(wall)

        for i in range(7):

            # Býr til peningin
            coin = arcade.Sprite("C:\Git\Skoli-haust-2020\Forritun\Verkefni með einkunn\Lokaverkefni\images\coinGold.png", SPRITE_SCALING / 2)#kallar í myndina

            # staðsetur myntina
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(600)

            # setur peningin í listan
            self.coin_list.append(coin)

        # -- setur upp karakterin
        self.player_sprite = arcade.Sprite("C:/Git/Skoli-haust-2020/Forritun/Verkefni með einkunn/Lokaverkefni/images/character1.png", SPRITE_SCALING)#kallar í myndina
        self.player_list.append(self.player_sprite)

        # setur byrjunarstaðsetningu karakterins
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 270

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             gravity_constant=GRAVITY)

        # setur bakrunn
        arcade.set_background_color(arcade.color.SKY_BLUE)
        
    def on_draw(self):
        arcade.start_render()# renderar inn leikin

        if self.flag: #intro skjárinn
            arcade.set_background_color(arcade.color.RED)
            arcade.draw_text(" Lárus Ármann Kjartansson\n Náðu fimm peningum til að vinna leikin \n Ýttu á Q til að hefja leik", 10,300, arcade.color.WHITE, 24)
            arcade.draw_text("Lárus Ármann ",self.view_left+10,self.view_bottom+10, arcade.color.CHERRY, 14)#setur nafnið mitt 
        elif self.score >=5 and self.flag==False: #endaskjárinn
            arcade.set_background_color(arcade.color.BUBBLES)
            arcade.draw_text("Leik lokið ",self.view_left+200,self.view_bottom+300, arcade.color.CHERRY, 44)
            arcade.draw_text("Lárus Ármann ",self.view_left+10,self.view_bottom+10, arcade.color.CHERRY, 14)
        else:#aðal leikurinn
            arcade.set_background_color(arcade.color.AMAZON)
            self.wall_list.draw()
            self.player_list.draw()
            arcade.draw_text(f"stig: {self.score}", self.player_sprite.center_x-15,self.player_sprite.center_y+30, arcade.color.WHITE, 14)
            arcade.draw_text("Lárus Ármann ",self.view_left+10,self.view_bottom+10, arcade.color.CHERRY, 14)
            self.coin_list.draw()
            
    def draw_game(self):
        # dregur sprit-in
        self.player_list.draw()
        self.coin_list.draw()

        # prentar Stigin fyrir ofan karakterin
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        
    def on_key_press(self, key, modifiers):
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


       
        changed = False

        # Scrollar vinstri
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scrollar hægri
        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scrollar upp
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scrollar niður
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

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