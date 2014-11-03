# Piet's fantasy adventure

import sys
import textwrap
import time
from keywords import (SNIFF, LOOK, NOTHING, PLAY, DIG, BARK, ROLL, WALK,
                       RUN, STAND, FIND, SLEEP, SCRATCH, FIGHT, INSIDE, 
                       BACK, FORWARD, ITEMS, ENTER, TRAIL, SWORD, SWIM, 
                       BOAT, DRINK, HEALTH, ITEMS, CONTINUE, JUMP, RETRIEVE,
                       GATHER, SWIPE, KICK, BITE, FIGHT,ATTACK, TUNNEL, QUIT,
                       TOWEL, MEDPACK, GIVE, EAT, HEADLAMP, BALL)
import string
import random

def cool_print(text):
    for i in text: 
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0)   
    print   
 
    
class Map(object):
    scenes = {'introduction': Introduction(),
              'living_room': LivingRoom(),
              'living_room2': LivingRoom2(),
              'backyard': Backyard(),
              'enchantedforest': EnchantedForest(),
              'clearing' : Clearing(),
              'trail' : Trail(),
              'tunnel': Tunnel(),
              'inside_tunnel' : InsideTunnel(),
              'enchantedforest_2': EnchantedForestPartTwo(),
              'river': River(),
              'dogpark': DogPark(),
              'death': Death(),
              'fight': Fight(),
              'home': Home()
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
