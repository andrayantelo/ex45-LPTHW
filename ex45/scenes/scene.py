import sys
import textwrap
from ..keywords import (SNIFF, LOOK, NOTHING, PLAY, DIG, BARK, ROLL, WALK,
                       RUN, STAND, FIND, SLEEP, SCRATCH, FIGHT, INSIDE, 
                       BACK, FORWARD, ITEMS, ENTER, TRAIL, SWORD, SWIM, 
                       BOAT, DRINK, HEALTH, ITEMS, CONTINUE, JUMP, RETRIEVE,
                       GATHER, SWIPE, KICK, BITE, FIGHT,ATTACK, TUNNEL, QUIT,
                       TOWEL, MEDPACK, GIVE, EAT, HEADLAMP, BALL, CHEW, COUCH)
import string
from ..utils import cool_print

class Scene(object):
    
    def __init__(self):
        self.sniff_text = textwrap.dedent(""" Piet sniffs around a little bit.""")
        self.look_text = textwrap.dedent(""" 
        Piet looks around and sees nothing unusual.
        """)
        self.nothing_text = textwrap.dedent(""" 
        Piet sits down and does nothing.
        """)
        self.play_text = textwrap.dedent(""" 
        Now is not the time to be playing or chewing! There are more 
        important matters at hand!
        """)
        self.dig_text = textwrap.dedent(""" 
        Piet digs a hole in the ground and sticks his nose in it""")
        self.bark_text = textwrap.dedent(""" 
        Piet barks three times and receives no response.
        """)
        self.roll_text = textwrap.dedent("""
        Piet rolls over but there is no one around to scratch his tummy.
        """)
        self.jump_text = textwrap.dedent(""" 
        Piet jumps up and down and quickly gets bored.
        """)
        self.pickup_text = textwrap.dedent(""" 
        There's nothing around to pick up.
        """)
        self.walk_text = textwrap.dedent(""" Piet walks around in a circle.""")
        self.run_text = textwrap.dedent(""" 
        Piet runs around chasing his tail. Then gets bored and sits down.""")
        self.stand_text = textwrap.dedent(""" 
        Piet stands and wonders about his owners.
        """)
        self.find_text = textwrap.dedent(""" 
        \"Yes, yes. I need to find my owners!\" Piet thinks.
         """)
        self.sleep_text = textwrap.dedent(""" 
        Piet curls up into a ball and tries to fall asleep but is unable
        to because all he can think about are his owners.
        """)
        self.scratch_text = textwrap.dedent(""" 
        There is nothing around for Piet to scratch!
        """)
        self.fight_text = textwrap.dedent(""" 
        There aren't any enemies for Piet to fight.
        """)
        self.inside_text = textwrap.dedent(""" Piet is already inside.""")
        self.back_text = textwrap.dedent(""" It's too late to turn back now!""")
        self.forward_text = textwrap.dedent(""" Piet walks slowly forward.""")
        self.enter_text = textwrap.dedent(""" 
        There is nothing to enter.
        """)
        self.trail_text = textwrap.dedent(""" There isn't a trail in sight!""")
        self.use_sword = textwrap.dedent(""" Who said anything about a sword?""")
        self.swim_text = textwrap.dedent(""" There's nowhere to swim.""")
        self.use_boat = textwrap.dedent(""" Why would there be a boat around?""")
        self.drink_water = textwrap.dedent(""" 
        Too bad there isn\'t any water around to drink
        """)
        # is there a way to have the text say retrieve, fetch, or salvage depending on what the user inputs?
        self.retrieve_text = textwrap.dedent("""
        There is nothing to retrieve.""")
        self.gather_text = textwrap.dedent("""
        there is nothing here to pick up or gather.""")
        self.swipe_text = textwrap.dedent("""
        There is nothing to swipe at.""")
        self.kick_text = textwrap.dedent("""
        Piet kicks his hind legs into the air.""")
        self.bite_text = textwrap.dedent("""
        Piet has nothing to bite on.""")
        self.fight_text = textwrap.dedent("""
        There is no one around for Piet to fight with.""")
        self.attack_text = textwrap.dedent("""
        Piet attempts to attack himself but fails.""")
        self.tunnel_text = textwrap.dedent("""
        There is no tunnel here.""")
        self.quit_text = "Goodbye!"
        self.towel_text = textwrap.dedent("""
        Don't forget to bring your towel!""")
        self.give_text = textwrap.dedent("""
        Piet has nothing but love to give.""")
        self.chew_text = textwrap.dedent("""
        Piet chews on his paws.""")
        self.couch_text = textwrap.dedent("""
        Piet is not allowed on the couch.""")
        self.command_dictionary = {}
        
    def clean_text(self, sentence):
        sentence = ''.join(c for c in sentence if c not in string.punctuation)
        sentence = sentence.lower()
        words = sentence.split()
        
        stop_words = ['a','the','an','and','at','that', 'watch', 'on', 'up',
                      'off','down', 'the', 'around', 'out', 'window', 'with']
        words = [w for w in words if w not in stop_words]
        
        return words
        

                            
    def parse_command(self, sentence):
        words = self.clean_text(sentence)
        print words 
        
        verb_dictionary = { 'look': LOOK, 
                    'nothing': NOTHING, 
                    'pick': GATHER,
                    'grab': GATHER, 
                    'lift': GATHER, 
                    'gather': GATHER,
                    'sniff': SNIFF, 
                    'smell': SNIFF, 
                    'scent': SNIFF,
                    'inhale': SNIFF, 
                    'chew': CHEW, 
                    'play': PLAY, 
                    'dig': DIG, 
                    'bark': BARK, 
                    'roll': ROLL, 
                    'rollover': ROLL,
                    'walk': WALK, 
                    'stroll': WALK, 
                    'step': WALK, 
                    'march': WALK,
                    'run': RUN, 
                    'sprint': RUN, 
                    'race': RUN, 
                    'stand': STAND, 
                    'find': FIND, 
                    'track': FIND, 
                    'inside': INSIDE,
                    'indoors': INSIDE,
                    'return': BACK, 
                    'retreat': BACK, 
                    'back': BACK,
                    'onward': FORWARD, 
                    'forward': FORWARD, 
                    'ahead': FORWARD,
                    'items': ITEMS, 
                    'display': ITEMS, 
                    'enter': ENTER, 
                    'in': ENTER, 
                    'trail': TRAIL, 
                    'path': TRAIL, 
                    'footpath': TRAIL, 
                    'pathway': TRAIL,
                    'sword': SWORD, 
                    'weapon': SWORD,
                    'boat': BOAT, 
                    'ship': BOAT, 
                    'raft': BOAT, 
                    'drink': DRINK,
                    'sip': DRINK, 
                    'taste': DRINK,
                    'health': HEALTH, 
                    'status': HEALTH, 
                    'jump': JUMP, 
                    'hop': JUMP,
                    'spring': JUMP, 
                    'leap': JUMP, 
                    'continue': CONTINUE, 
                    'retrieve': RETRIEVE, 
                    'fetch': RETRIEVE, 
                    'salvage': RETRIEVE, 
                    'punch': SWIPE, 
                    'swipe': SWIPE, 
                    'hit': SWIPE,
                    'kick': KICK, 
                    'bite': BITE, 
                    'fight': FIGHT, 
                    'attack': ATTACK, 
                    'tunnel': TUNNEL, 
                    'towel': TOWEL, 
                    'quit': QUIT,
                    'medpack': MEDPACK, 
                    'give': GIVE, 
                    'deliver': GIVE, 
                    'present': GIVE, 
                    'gift': GIVE, 
                    'eat': EAT, 
                    'treat': EAT, 
                    'gobble': EAT, 
                    'gorge': EAT, 
                    'headlamp': HEADLAMP, 
                    'swim': SWIM, 
                    'ball': BALL,
                    'couch': COUCH}
        for word in words:
            
            action = verb_dictionary.get(word)
     
            
        print action
        return action
        
    def process_action(self, command, player):
        action = self.parse_command(command)
        
        if action == LOOK:
            cool_print(self.look_text)
        elif action == NOTHING:
            cool_print(self.nothing_text)
        elif action == SNIFF:
            cool_print(self.sniff_text)
        elif action == PLAY:
            cool_print(self.play_text)
        elif action == DIG:
            cool_print(self.dig_text)
        elif action == BARK:
            cool_print(self.bark_text)
        elif action == ROLL:
            cool_print(self.roll_text)
        elif action == WALK:
            cool_print(self.walk_text)
        elif action == RUN:
            cool_print(self.run_text)
        elif action == STAND:
            cool_print(self.stand_text)
        elif action == FIND:
            cool_print(self.find_text)
        elif action == INSIDE:
            cool_print(self.inside_text)
        elif action == BACK:
            cool_print(self.back_text)
        elif action == FORWARD:
            cool_print(self.forward_text)
        elif action == ITEMS:
            player.display_items()
        elif action == ENTER:
            cool_print(self.enter_text)
        elif action == TRAIL:
            cool_print(self.trail_text)
        elif action == SWORD:
            cool_print(self.use_sword)
        elif action == BOAT:
            cool_print(self.use_boat)
        elif action == DRINK:
            cool_print(self.drink_water)
        elif action == HEALTH:
            player.health_status()
        elif action == JUMP:
            cool_print(self.jump_text)
        elif action == RETRIEVE:
            cool_print(self.retrieve_text)
        elif action == CONTINUE:
            print "You have typed 'continue'."
        elif action == GATHER:
            cool_print(self.gather_text)
        elif action == SWIPE:
            cool_print(self.swipe_text)
        elif action == KICK:
            cool_print(self.kick_text)
        elif action == BITE:
            cool_print(self.bite_text)
        elif action == FIGHT:
            cool_print(self.fight_text)
        elif action == ATTACK:
            cool_print(self.attack_text)
        elif action == TUNNEL:
            cool_print(self.tunnel_text)
        elif action == QUIT:
            sys.exit()
        elif action == TOWEL:
            cool_print(self.towel_text)
        elif action == MEDPACK:
            player.use_medpack()
        elif action == GIVE:
            cool_print(self.give_text)
        elif action == EAT:
            player.eat_treat()
        elif action == HEADLAMP:
            player.use_headlamp()
        elif action == BALL:
            player.use_ball()
        elif action == CHEW:
            cool_print(self.chew_text)
        elif action == COUCH:
            cool_print(self.couch_text)
        elif action == 'None':
            print "Try another command."
            
    def enter(self, player):
        player.player_in_dark = False
        player.health_status()
        player.display_items()

