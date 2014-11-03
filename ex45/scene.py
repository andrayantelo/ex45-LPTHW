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
        self.command_dictionary = {}
        
    def clean_text(self, sentence):
        sentence = ''.join(c for c in sentence if c not in string.punctuation)
        sentence = sentence.lower()
        words = sentence.split()
        
        stop_words = ['a','the','an','and','at','that', 'watch']
        words = [w for w in words if w not in stop_words]
        
        return words
        
        
    def parse_command(self, sentence):
        words = self.clean_text(sentence)
        print "WORDS:", words
        
        #default action 
        action = 'None'
        
        if 'look' in words:
            action = LOOK
        elif 'nothing' in words:
            action = NOTHING
        elif any(w in words for w in ('pick', 'grab', 'lift', 'gather')):
            action = GATHER
        elif any(w in words for w in ('sniff', 'smell', 'scent', 'inhale')):
            action = SNIFF
        elif any(w in words for w in ('chew', 'play')):
            action = PLAY
        elif 'dig' in words:
            action = DIG
        elif 'bark' in words:
            action = BARK
        elif any(w in words for w in ('roll', 'rollover')):
            action = ROLL
        elif any(w in words for w in ('walk', 'stroll', 'step', 'march',
                                       'hike')):
            action = WALK
        elif any(w in words for w in ('run', 'sprint', 'race', 'dash')):
            action = RUN
        elif 'stand' in words:
            action = STAND
        elif any(w in words for w in ('find', 'track down')):
            action = FIND
        elif any(w in words for w in ( 'inside', 'indoors')):
            action = INSIDE
        elif any(w in words for w in ('return', 'retreat',
                                        'back')):
            action = BACK
        elif any(w in words for w in ('onward', 'forward',
                                       'ahead', 'on')):
            action = FORWARD
        elif any(w in words for w in ('items', 'display')):
            action = ITEMS
        elif any(w in words for w in ('enter', 'in')):
            action = ENTER
        elif any(w in words for w in ('trail', 'path', 'footpath', 'pathway')):
            action = TRAIL
        elif any(w in words for w in ('sword', 'weapon')):
            action = SWORD
        elif any(w in words for w in ('boat', 'ship', 'raft')):
            action = BOAT
        elif any(w in words for w in ('drink', 'sip', 'taste')):
            action = DRINK
        elif any(w in words for w in ('health', 'status')):
            action = HEALTH
        elif any(w in words for w in ('jump', 'hop', 'spring', 'leap')):
            action = JUMP
        elif 'continue' in words:
            action = CONTINUE
        elif any(w in words for w in ('retrieve', 'fetch', 'salvage')):
            action = RETRIEVE
        elif any(w in words for w in ('punch', 'swipe', 'hit')):
            action = SWIPE
        elif 'kick' in words:
            action = KICK
        elif 'bite' in words:
            action = BITE
        elif 'fight' in words:
            action = FIGHT
        elif 'attack' in words:
            action = ATTACK
        elif 'tunnel' in words:
            action = TUNNEL
        elif 'quit' in words:
            action = QUIT
        elif 'towel' in words:
            action = TOWEL
        elif 'medpack' in words:
            action = MEDPACK
        elif any(w in words for w in ('give', 'deliver', 'present', 'gift')):
            action = GIVE
        elif any(w in words for w in ('eat', 'treat', 'gobble', 'gorge')):
            action = EAT
        elif 'headlamp' in words:
            action = HEADLAMP
        elif 'swim' in words:
            action = SWIM
        elif 'ball' in words:
            action = BALL
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
        elif action == 'None':
            print "Try another command."
            
    def enter(self, player):
        player.player_in_dark = False
        player.health_status()
        player.display_items()
