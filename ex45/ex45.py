# Piet's fantasy adventure

import time
import scenes as sc
from characters import Player, Villain
    
class Map(object):
    scenes = {'introduction': sc.Introduction(),
              'living_room': sc.LivingRoom(),
              'living_room2': sc.LivingRoom2(),
              'backyard': sc.Backyard(),
              'enchantedforest': sc.EnchantedForest(),
              'clearing' : sc.Clearing(),
              'trail' : sc.Trail(),
              'tunnel': sc.Tunnel(),
              'inside_tunnel' : sc.InsideTunnel(),
              'enchantedforest_2': sc.EnchantedForestPartTwo(),
              'river': sc.River(),
              'dogpark': sc.DogPark(),
              'death': sc.Death(),
              'fight': sc.Fight(),
              'home': sc.Home()
              }
              
    def __init__(self, start_scene):
        self.start_scene = start_scene
      
    def next_scene(self, next_scene):
        return self.scenes.get(next_scene)
        
    def opening_scene(self):
        return self.scenes.get(self.start_scene)
    
class Engine(object):
    
    def __init__(self, game_map):
        self.game_map = game_map
        
    def play(self, player):
        current_scene = self.game_map.opening_scene()
        
        while True:
            #if current_scene not in self.game_map.scenes:
             #   raise ValueError("Scene did not return a valid next scene!")
            next_scene_name = current_scene.enter(player)
            current_scene = self.game_map.next_scene(next_scene_name)
            
if __name__ == "__main__":
    piet = Player()
    a_map = Map('introduction')
    a_game = Engine(a_map)
    a_game.play(piet)

#intro = a_map.scenes.get('introduction')
#print type(intro)
