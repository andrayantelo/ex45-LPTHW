# Piet's fantasy adventure

import sys
import textwrap
import time
from keywords import (SNIFF, LOOK, NOTHING, PLAY, DIG, BARK, ROLL, WALK,
                       RUN, STAND, FIND, SLEEP, SCRATCH, FIGHT, INSIDE, 
                       BACK, FORWARD, ITEMS, ENTER, TRAIL, SWORD, SWIM, 
                       BOAT, DRINK, HEALTH, ITEMS, CONTINUE, JUMP, RETRIEVE,
                       GATHER, SWIPE, KICK, BITE, FIGHT,ATTACK)
import string

def cool_print(text):
    for i in text: 
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0)   
    print   
 
class Character(object):
    
    def __init__(self):
        self.items = []
        self.status = 3
        self.fight_scene_count = []
        self.name = 'name'
        
    def health_status(self):
        heart = u'\u2764'
        empty_heart = u'\u2661'
        print "%s\'s current health status:" % self.name
        if self.status == 3:
            print heart, heart, heart
        if self.status == 2: 
            print heart, heart, empty_heart
        if self.status == 1:
            print heart, empty_heart, empty_heart
        if self.status == 0:
            print empty_heart, empty_heart, empty_heart
        
class Player(Character):
    
    def __init__(self):
        super(Player, self).__init__()
        self.items = []
        self.status = 3
        self.fight_scene_count = []
        self.name = 'Piet'
    
    def obtain_item(self, thing):
        self.items.append(thing)
        return self.items
    
    def display_items(self):
        print "You currently have the following items:"
        print self.items
        
    def attack(self, villain):
        print "attack method worked"
        if villain.status > 1:
            villain.status = villain.status - 1
        elif villain.status == 1:
            villain.status = villain.status - 1
            print "You have slain the villain!"
        print "villain's health status:"
        villain.health_status()
        
    def use_medpack(self, medpack):
        medpack = 'medpack'
        if medpack in self.items and self.status != 3:
            print "Piet uses a medpack."
            self.status = self.status + 1
        elif self.status == 3:
            print "Health status is full."
        elif medpack not in self.items:
            print "%s has no medpacks." % self.name
        
class Villain(Character):
     
    def __init__(self):
        super(Villain, self).__init__()
        self.name = 'name'
        
    def name_villain(self, name):
        self.name = name
        

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
        self.enter_tunneltext = textwrap.dedent(""" 
        No tunnel to be found around here!
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
        self.command_dictionary = {}
        
    def clean_text(self, sentence):
        sentence = ''.join(c for c in sentence if c not in string.punctuation)
        sentence = sentence.lower()
        words = sentence.split()
        
        stop_words = ['a','the','an','and','at','that', 'watch', 'sword',
                      'medpack', 'headlamp']
        words = [w for w in words if w not in stop_words]
        
        return words
        
        
    def parse_command(self, sentence):
        words = self.clean_text(sentence)
        #print "WORDS:", words
        
        #default action 
        action = None
        
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
                                       'ahead')):
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
            cool_print(self.enter_tunneltext)
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
        elif action == None:
            print "Try another command."
            
            
        
        
class Introduction(Scene):
    
    def __init__(self):
        super(Introduction, self).__init__()
        self.intro_text = textwrap.dedent(
        """\n\n
        Once upon a time there lived a little black and white dog
        named Piet. He was a small poodle/schnauzer mix with soft curly
        fur and a big heart. He had two lovely owners who loved him very
        much. Piet was very protective of his owners and his friends. He 
        was a very loyal dog. Some say, he was the most loyal dog in the 
        world.""")
        self.dig_text = textwrap.dedent("""
        There is nowhere to dig.""")
        
    def enter(self, player):
        cool_print(self.intro_text)
        
        print "To check health status type \"health status\""
        print "To check item inventory type \"display items\""
        print "Type 'continue' to continue"
        
        while True:
            command = str(raw_input("\n> "))
            
        
            action = self.parse_command(command)
            self.process_action(command, player)
            if action == CONTINUE:
                return 'living_room'
        
class LivingRoom(Scene):
    
    def __init__(self):
        super(LivingRoom, self).__init__()
        self.living_text = textwrap.dedent(
        """ \n
        One lovely Sunday morning, Piet was napping peacefully 
        in his dog bed dreaming about the dog park. He jolted awake when 
        he heard the sound of house keys jingling and ran towards
        the front door. The door clicked shut softly just as he got there
        and Piet knew that his owners had just left him home alone. Despite
        having several rooms, the only room available to Piet in the house
        is the living room. Piet stared at the front door for a bit and
        then noticed that his owner had forgotten his wristwatch.
        """)
        self.gather_text = textwrap.dedent(
        """ 
        The only thing around to pick up is the wristwatch. Piet gingerly
        grasps it in his mouth and places it in his dog purse which he
        wears around his neck.
        """)
        self.sleep_text = textwrap.dedent(
        """ \n
        Piet whimpered at the door a little bit. Then he curled up into
        a little ball and shut his eyes. 'Maybe if I go to sleep the time
        will go faster and when I wake up they will be home,' he thought as
        he drifted off to sleep.
        """)
        self.play_text = textwrap.dedent(
        """ \n
        Piet attacks his chew toy and plays with it a little. Then
        he gets bored and looks back at the front door.
        """)
        self.scratch_text = textwrap.dedent(
        """ \n
        Piet scratches at the door but gets tired of it quickly. He
        already knew that didn't bring his owners back.
        """)
        self.look_text = textwrap.dedent(
        """ \n
        Piet looks around the living room and notices that the window
        looking out at the backyard is open. Piet's ears perk up as he runs
        over to the window. He stops short in front of the window and looks 
        out hesitantly. A soft cool breeze beckons him and he could hear birds
        chirping in the trees and leaves rustling in the wind. He sniffs
        the air and smells all sorts of wonderful smells. 
        """)
        self.sniff_text = textwrap.dedent(
        """ \n
        Piet sniffs around the living room and finds a med pack hidden
        behind the couch. He places it in his purse.
        """)
        self.jump_text = textwrap.dedent("""
        Piet goes and retrieves his dog purse then
        he turns to face the window. He musters up all of his strength and sprints
        forward leaping out the open window.
        """)
        self.dig_text = textwrap.dedent("""
        There is nowhere to dig!"""
        )
        self.items = ['medpack', 'wristwatch']
        
    def enter(self, player):
        player.health_status()
        player.display_items()
        
        cool_print(self.living_text)
        
        while True:
            command = str(raw_input("Type a command.\n> "))
            
        
            action = self.parse_command(command)
            self.process_action(command, player)
            if action == SNIFF:
                player.items.append('medpack')
            elif action == GATHER:
                player.items.append('wristwatch')
            elif action == JUMP:
                return 'backyard'
    
class Backyard(Scene):
    
    def __init__(self):
        super(Backyard, self).__init__()
        self.backyard_text = textwrap.dedent(
        """ \n
        Piet lands clumsily on his four paws and looks back up at the
        open window. The window is low enough to the ground that he could
        easily go back inside if he wanted to. Piet feels reassured at this
        thought as he turns around to face the backyard. The backyard is 
        quite large. Much bigger than the living room. The lawn is overgrown
        and there is a gigantic cracked bird fountain in the middle.  Piet 
        begins to march forward sniffing at the ground but stops short when
        he hears a loud noise. 
        'HISSSSSSSSSSS'
        Piet looks up. A large spotted cat eyes him menacingly. This was the 
        largest cat Piet had ever seen in his entire life. The cat has the look
        of a seasoned war veteran. There were scars etched in the fur of its
        face and it had a few bald spots. The cat arches its back and stares
        at Piet with wide eyes.
        """)
        self.fight_text = textwrap.dedent("""
        Piet decides he can fight this cat.
        """)
        self.run_text = textwrap.dedent(
        """ \n
        Piet decides to run past the cat. Piet is one of the fastest 
        dogs in the neighborhood, frequently outrunning other dogs at the
        dog park. His owners also liked to take him jogging with them which
        kept Piet in tip top shape! Piet began to run towards the cat, which 
        catches the cat off gaurd. The cat freezes in place mid-swipe. Just 
        as Piet is about to crash into the cat he veers left and flies past
        it towards the back fence. Piet takes a literal leap of faith and flies
        over the fence landing on the other side. The cat speeds off to 
        the neighbor's yard.
        """)
        self.inside_text = textwrap.dedent(
        """ \n
        Piet jumps back inside through the open window. The cat looks 
        at Piet for a minute safely inside then curls up and lays down in 
        the grass staring at Piet. Piet realizes the cat was going to stay
        there all day waiting for him. 
        """
        )
        self.nothing_text = textwrap.dedent(
        """ \n
        Piet stands in front of the cat frozen in fear. The cat swipes
        at Piet with its claws. Piet yelps as the cat continues to swipe.
        Eventually, the cat leaves Piet alone to die.
        """)
        self.look_text = textwrap.dedent("""
        Piet looks around but sees nothing he could use as a weapon.""")
        self.sniff_text = textwrap.dedent("""
        Piet sniffs the air but can only smell cat.""")
        self.play_text = textwrap.dedent(""" 
        Piet attemps to play with the cat but the cat swipes at him with it's
        claws and barely misses Piet's face.""")
        self.bark_text = textwrap.dedent("""
        Piet barks loudly but the cat is unfazed.""")
        self.items = []
        self.number_of_fights = []
        
    def enter(self, player):
        player.health_status()
        player.display_items()
        cool_print(self.backyard_text)
        
        while True:
            command = str(raw_input("Type a command.\n> "))
            
        
            action = self.parse_command(command)
            self.process_action(command, player)
            if action == RUN:
                return 'enchanted_forest'
            elif action == NOTHING:
                return 'death'
            elif action == FIGHT:
                return 'fight'
                
class Fight(Scene):
    
    def __init__(self):
        super(Fight, self).__init__()
        self.swipe_text = textwrap.dedent("""
        Piet takes a swipe at his enemy.""")
        self.kick_text = textwrap.dedent("""
        Piet kicks at his enemy with his hind legs.""")
        self.bite_text = textwrap.dedent("""
        Piet sinks his teeth into one of his enemy's limbs and doesn\'t 
        let go.
        """)
        self.fight_text = textwrap.dedent("""
        Piet punches his enemy in the face.""")
        self.attack_text = textwrap.dedent("""
        Piet lunges forward to attack.""")
        self.backyard_fight_text = textwrap.dedent("""
        Piet may be small but he thinks he is the biggest dog in the world.
        \"I can take that cat,\" Piet thinks arrogantly to himself. Piet puffs 
        up his chest and lets out a loud bark. The cat looks at him incredulously,
        as if it's about to laugh. Then charges Piet, claws out.
        """)
        self.tunnel_fight_text = textwrap.dedent("""
        Piet barks loudly but the spider is unfazed. The spider begins to advance.
        """)
        self.enemy = Villain()

        
    #def parse_command(self, command):
     #   super(Fight, self).parse_command(command)
     #   
     #   if any(w in words for w in ('attack', 'strike', 'charge', 'rush')):
     ##       action = ATTACK
      #  return action
        
    #def process_action(self, command, player):
    #    super(Fight, self).process_action(command, player)
    #    
    #    if any(w in action for w in (FIGHT, SWIPE, KICK, BITE, ATTACK)):
    #        player.attack(self.cat)
                
    def enter(self, player):
        player.health_status()
        player.display_items()
        player.fight_scene_count.append(1)
        
        if len(player.fight_scene_count) == 1:
            cool_print(self.backyard_fight_text)
            self.enemy.name_villain('Cat')
        elif len(player.fight_scene_count) == 2:
            cool_print(self.tunnel_fight_text)
            self.enemy.name_villain('Spider')
        
        while True:
            command = str(raw_input("Type a command.\n> "))
            
            action = self.parse_command(command)
            self.process_action(command, player)
            
            
            if self.enemy.status == 0:
                print "You have defeated the enemy!"
                return 'enchantedforest'
            elif player.status == 0:
                return 'death'
            elif any(w in action for w in (ATTACK, FIGHT, BITE, SWIPE, KICK)):
                player.attack(self.enemy)
            
        
    
    
class EnchantedForest(Scene):
    
    def __init__(self):
        super(EnchantedForest, self).__init__()
        self.enchanted_text = textwrap.dedent(
        """ \n
        On the other side of the fence Piet finds himself at the border
        of the Enchanted Forest. All the dogs referred to the forest as The
        Enchanted Forest on account of all the strange things that happened
        to the dogs that dared to enter it alone, but he had often heard 
        his owners refer to it with the words 'The Greenbelt'. Piet stops at 
        the edge of the woods and contemplates his options. He could go back
        into the yard now that the cat was gone, but his owners weren't 
        there and he needed to bring them their forgotten wristwatch!
        """)
        self.back_text = textwrap.dedent(
        """ \n
        Piet turns around and heads back inside like a coward. The cat
        was no longer in the yard. Who knew where his owners were. Piet 
        sat down and cried.
        """)
        self.forward_text = textwrap.dedent(
        """ \n
        'I will find my owners!' Piet thinks to himself, determined to
        find them. Piet enters the Enchanted Forest and walks along the dirt
        past trees and shrubs. Eventually he reaches a large clearing.
        """)
        self.sniff_text = textwrap.dedent(
        """ 
        Piet finds a medpack nestled in the dirt.
        """)
        self.look_text = textwrap.dedent(
        """ \n
        Piet notices something shiny near some rocks. It's a small
        sword with a handle shaped perfectly to be held in a dog's mouth.
        """)
        self.bark_text = textwrap.dedent(
        """ \n
        Piet barks three times and waits. At first he does not hear 
        anything and then he hears a loud hissing. His barking has attracted
        a large Coral Snake!
        """)
        self.items = ['medpack', 'sword']
        
    def enter(self, player):
        player.health_status()
        player.display_items()
        cool_print(self.enchanted_text)
    
class Tunnel(Scene):
    
    def __init__(self):
        super(Tunnel, self).__init__()
        self.tunnel_text = textwrap.dedent(
        """ \n
        The clearing is large and covered in dirt and shrubs. Piet sees
        a small tunnel to the left and a dirt trail on the right.
        """)
        self.enter_tunneltext = textwrap.dedent(
        """ \n
        Piet walks over to the entrance of a tunnel. A loud squawk sound
        makes Piet freeze in his tracks. A large hawk swoops down and blocks
        the tunnel entrance. Piet swallows audibly and takes a
        step back. 'If you wish to use the tunnel you must correctly solve 
        this riddle.' the Hawk screeches. Piet nods slowly.
        
        'What gets wetter and wetter the more it dries?' The hawk cackles 
        as Piet looks at it stumped.
        """)
        self.trail_text = textwrap.dedent(
        """ \n
        Piet heads over to the trail and begins to follow it. He 
        sniffs the ground as he walks but does not smell anything familiar. All 
        the smells were very interesting, of course, but nothing smelled
        remotely like his owners. Piet trudged along for what seemed like 
        hours. Suddenly, Piet noticed that the sun was going down. 
        'Is it really that late already?' he whimpered. Piet laid down to 
        sleep and slept like a log. The next morning he awoke to the sounds 
        of birds chirping in the trees. Piet looked around. Yes, he was still
        in The Enchanted Forest. Piet could either go forward or he could go 
        back the way he came.
        """)
        self.correct_guess = textwrap.dedent(
        """ \n
        The hawk squealed in excitement. 'That's a first!' He squawked
        as he tossed something at Piet. Piet sniffed at it. It was a small 
        head lamp, and it fit perfectly around Piet's head. 'Thanks, Mr. 
        Hawk,' Piet said politely. The Hawk rolled it's eyes and stepped 
        aside so that Piet could enter the dark tunnel. 
        """)
        self.wrong_guess = textwrap.dedent(
        """ \n
        'Sorry, Dog, that's the wrong answer!' The hawk cackles. Then 
        he swoops in and grabs Piet with his enormous claws. Piet shrieks
        as the hawk carries him off to a large nest where hungry baby hawks
        are waiting.
        """)
        
        self.inside_tunnel = textwrap.dedent(
        """ \n
        Piet switches on his headlamp and advances into the tunnel. It 
        was pitch black in there. Piet felt relieved that the hawk had given
        him the lamp. He walks cautiously inside the tunnel but did not see 
        much besides a couple of rocks. Slowly, Piet begins to run a little bit. 
        'There doesn't seem to be anything in here anyway! Maybe I can sprint
        to the end' So, Piet begins to sprint, dodging a couple of stones here and there. 
        Suddenly, Piet can see a light at the end of the tunnel. It was still a 
        little distant but it was not far now. With a burst of adrenaline, 
        Piet began to run just a little faster. Then, without warning, a 
        large object blocks the view of the light at the end of the tunnel. 
        Piet stops running abruptly. He shines his head lamp onto the object.
        It's a giant monster with eight spindly legs. A giant spider monster!
        Piet looks at it in horror.
        """)
        self.use_sword = textwrap.dedent(
        """ \n
        Piet pulls out his sword and grips it in his mouth. He takes
        a swipe at the spider and cuts off one of the spider's legs. With
        renewed confidence Piet swipes left and right with the sword. The 
        spider did not know what to make of it. A dog with a sword? It had
        never seen such a thing. It scurried off before Piet could cut off
        any of it's other legs. Piet slashed at the air in triumph. Then he 
        put the sword away and sprinted like his life depended on it to the 
        end of the tunnel.""")
        self.fight_text = textwrap.dedent("""
        Piet decides to fight.""")
        self.items = ['head lamp']
        
class EnchantedForestPartTwo(Scene):
    
    def __init__(self):
        super(EnchantedForestPartTwo, self).__init__()
        self.forward_text = textwrap.dedent(
        """ \n
        Piet decides to continue following the trail. Piet walks and 
        walks all day long. At one point he passes a small creek he gets
        a drink of water. Suddenly, Piet hears running footsteps.
        He could tell they were human. Piet runs towards the sound and comes
        across a man running. 'Whoa!' the man exclaims in surprise at the
        sight of Piet. Piet jumps up on the man and cries excitedly. 'Hey,
        there, Puppy! Where are your owners?' The man asks gently. The man 
        picks Piet up and takes a look at his collar. 'Don't worry, boy, 
        I'll get you home soon.' The man takes Piet home and gives him some 
        food. The man had a dog at home too and Piet was excited to play. 
        After a couple of hours there is a knock at the door. When the man 
        opens the door Piet hears a familiar sound. 'It's my owner!' Piet 
        sprints to the door and leaps into his owner's arms. He lickes his face
        all over. 'Piet, where have you been!' His owner exclaimed. Piet
        barked excitedly and spun around in a circle. He was going home.
        """)
        self.back_text = textwrap.dedent(
        """ \n
        Piet turns around and heads back. Who knows how long that trail 
        would go for. He couldn't even smell his owners on it anyway.
        """)
        self.sniff_text = textwrap.dedent("""
        Piet sniffs around and finds a medpack hidden in the shrubs.""")
        self.items = ['medpack']
        
    
class River(Scene):
    
    def __init__(self):
        super(River, self).__init__()
        self.river_text = textwrap.dedent(
        """ \n
        Piet emerges from the tunnel into the blinding sunlight. He shuts
        his headlamp off and puts it away in his purse. He has emerged into a
        very small clearing with a river right in front of him.
        """)
        self.swim_text = textwrap.dedent(
        """ \n
        Piet leaps into the water and begins to swim across. The current
        was really strong and Piet struggled to swim to the other side. Eventually,
        Piet had no strength left and he let the river carry him far far away.
        Piet was never to be seen or heard of again. 
        """)
        self.look_text = textwrap.dedent(
        """ \n
        Piet looks around and finds a small dog size boat anchored to 
        the river bed.
        """)
        self.use_boat = textwrap.dedent(
        """ \n
        Piet leaps into the boat pulls up the anchor. Then he grabs a 
        paddle with his mouth and begins to paddle across the river.
        """)
        self.drink_water = textwrap.dedent("""
        Piet takes a couple of sips of the fresh river water.
        """)
        
        
    
class DogPark(Scene):
    
    def __init__(self):
        super(DogPark, self).__init__()
        self.dogpark_text = textwrap.dedent(
        """ \n
        Piet arrives on the other side of the river and sees that he has
        reached his favorite dog park in the whole wide world. He could see dogs
        running around playing with their owners. In his excitement, he jumps 
        out of the boat before anchoring it. The boat floats away but Piet
        was too distracted by all the other dogs to notice or care.
        """)
        self.play_text = textwrap.dedent(
        """ \n
        Piet sniffs at the nearest dogs and begins to play with them. 
        He is having so much fun he forgets all about his owners. Eventually, 
        the humans begin to notice that Piet is there all by himself. One 
        human takes it upon herself to make sure Piet gets home. She takes a 
        look at his collar. About half an hour later Piet hears a familiar sound.
        "Piet!" Piet whips his head around and sure enough it's his owner calling
        him. Piet sprints towards his owner and leaps into his arms. He
        was so happy to finally have found him. He takes the wristwatch out
        of his purse and drops it in front of his owner. "Oh good boy! I 
        thought I had lost this forever!' Piet's owner puts his wristwatch on, 
        then he picks Piet up and they go back home.
        """)
        self.look_text = textwrap.dedent(
        """ \n
        Piet looks around and sees a dog treat nestled in the grass.
        He gobbles it up hungrily.
        """)
        
    
class Death(Scene):
    
    def __init__(self):
        self.death_text = textwrap.dedent("""
        Unfortunately, the decisions Piet has made have led him to his
        untimely death. Game over!
        """)
        
        def enter(self):
            cool_print(self.death_text)
            sys.exit()
    
class Map(object):
    scenes = {'introduction': Introduction(),
              'living_room': LivingRoom(),
              'backyard': Backyard(),
              'enchantedforest': EnchantedForest(),
              'tunnel': Tunnel(),
              'enchantedforest_2': EnchantedForestPartTwo(),
              'river': River(),
              'dogpark': DogPark(),
              'death': Death(),
              'fight': Fight()
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
