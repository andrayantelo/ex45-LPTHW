# Piet's fantasy adventure

import sys
import textwrap
import time
from keywords import (SNIFF, LOOK, NOTHING, PLAY, DIG, BARK, ROLL, WALK,
                       RUN, STAND, FIND, SLEEP, SCRATCH, FIGHT, INSIDE, 
                       BACK, FORWARD, ITEMS, ENTER, TRAIL, SWORD, SWIM, 
                       BOAT, DRINK, HEALTH, ITEMS)
import string

def cool_print(text):
    for i in text: 
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.01)   
    print   
    
class Player(object):
    
    def __init__(self):
        self.items = []
        self.status = 3
        
    def health_status(self):
        heart = u'\u2764'
        empty_heart = u'\u2661'
        print "Your current health status is:"
        if self.status == 3:
            print heart, heart, heart
        if self.status == 2: 
            print heart, heart, empty_heart
        if self.status == 1:
            print heart, empty_heart, empty_heart
        if self.status == 0:
            print empty_heart, empty_heart, empty_heart
            print "Game over!"
            sys.exit()
    
    def obtain_item(self, thing):
        self.items.append(thing)
        return self.items
    
    def display_items(self):
        print "You currently have the following items:"
        print self.items
        

            
class Scene(object):
    
    def __init__(self):
        self.sniff_text = textwrap.dedent(""" Piet sniffs around a little bit.""")
        self.look_text = textwrap.dedent(""" Piet looks around and sees 
        nothing unusual.
        """)
        self.nothing_text = textwrap.dedent(""" Piet sits down and does
        nothing.
        """)
        self.play_text = textwrap.dedent(""" Now is not the time to be playing. 
        There are more important matters at hand!
        """)
        self.dig_text = textwrap.dedent(""" There is nowhere to dig.""")
        self.bark_text = textwrap.dedent(""" Piet barks three times 
        and receives no response.
        """)
        self.roll_text = textwrap.dedent(""" Piet rolls over but there 
        is no one around to scratch his tummy.
        """)
        self.walk_text = textwrap.dedent(""" Piet walks around in a circle.""")
        self.run_text = textwrap.dedent(""" Piet runs around chasing his
        tail. Then gets bored and sits down.""")
        self.stand_text = textwrap.dedent(""" Piet stands and wonders 
        about his owners.
        """)
        self.find_text = textwrap.dedent(""" \"Yes, yes. I need to find my
         owners!\" Piet thinks.
         """)
        self.sleep_text = textwrap.dedent(""" Piet curls up into a ball 
        and tries to fall asleep but is unable to because all he can think
        about are his owners.
        """)
        self.scratch_text = textwrap.dedent(""" There is nothing around 
        for Piet to scratch!
        """)
        self.fight_text = textwrap.dedent(""" There aren't any enemies 
        for Piet to fight.
        """)
        self.inside_text = textwrap.dedent(""" Piet is already inside.""")
        self.back_text = textwrap.dedent(""" It's too late to turn back now!""")
        self.forward_text = textwrap.dedent(""" Piet walks slowly forward.""")
        self.display_items_text = textwrap.dedent(""" Piet has the following
        items in his possesion: 
        """)
        self.enter_tunneltext = textwrap.dedent(""" No tunnel to be found
        around here!
        """)
        self.trail_text = textwrap.dedent(""" There isn't a trail in sight!""")
        self.use_sword = textwrap.dedent(""" Who said anything about a sword?""")
        self.swim_text = textwrap.dedent(""" There's nowhere to swim.""")
        self.use_boat = textwrap.dedent(""" Why would there be a boat around?""")
        self.drink_water = textwrap.dedent(""" Too bad there isn\'t any 
        water around to drink
        """)
        self.command_dictionary = {}
        
    def clean_text(self, sentence):
        sentence = ''.join(c for c in sentence if c not in string.punctuation)
        sentence = sentence.lower()
        words = sentence.split()
        
        stop_words = ['a','the','an','and','at']
        words = [w for w in words if w not in stop_words]
        
        return words
        
        
    def parse_command(self, sentence):
        words = self.clean_text(sentence)
        print "WORDS:", words
        
        #default action 
        action = none
        
        
        #word_list = sentence.split()
        #for word in word_list:
        #    if word in self.command_dictionary:
        #        return self.command_dictionary.get(word)
        
    
        
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
        
    def enter(self, player):
        cool_print(self.intro_text)
        
        print "To check health status type \"health status\""
        print "To check item inventory type \"display items\""
        print "To continue press 'Enter'"
        
        while True:
            command = str(raw_input("\n> "))
            
        
            self.parse_command(command)
        
        return 'living_room'
        
class LivingRoom(Scene):
    
    def __init__(self):
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
        the air and smells all sorts of wonderful smells. The decision was made.
        Piet walks back towards the wristwatch and picks it up gingerly with 
        his mouth. He nudges the wristwatch into a small dog purse that he 
        wears around his neck. Then he turns, sprints, and leaps out 
        the open window.
        """)
        self.sniff_text = textwrap.dedent(
        """ \n
        Piet sniffs around the living room and finds a med pack hidden
        behind the couch. He places it in his purse.
        """)
        
    def enter(self, player):
        print "this is the living room"
        player.health_status()
        player.display_items()
        
        cool_print(self.living_text)
    
class Backyard(Scene):
    
    def __init__(self):
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
        self.fight_text = textwrap.dedent(
        """ \n
        Piet may be small but he thinks he is the biggest dog in the world.
        'I can take that cat,' Piet thinks arrogantly to himself. Piet puffs 
        up his chest and lets out a loud bark. The cat looks at him incredulously,
        as if it's about to laugh. Then charges Piet, claws out. Piet lets 
        out a yelp and cowers, his tail between his legs. The cat screeches
        and continues to swipe at Piet with it's razor sharp claws. Eventually,
        the cat gets bored and leaves Piet alone to die.
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
        self.dig_text = textwrap.dedent(""" Piet digs a hole in the ground
        and sticks his nose in it.""")
        
    
class EnchantedForest(Scene):
    
    def __init__(self):
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
        Piet finds a med pack nestled in the dirt.""")
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
        self.dig_text = textwrap.dedent(""" Piet digs a hole in the ground
        and sticks his nose in it.""")
        
    
class Tunnel(Scene):
    
    def __init__(self):
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
        self.fight = textwrap.dedent(
        """ \n
        Piet had nothing useful to use as a weapon. Piet barks loudly 
        but the spider is unfazed. The spider begins to advance. Piet lunges
        forward and bites into one of the spider's legs. He clamps down with
        his jaws and does not let go. The spider shrieks in pain and tries
        to wrestle free. Piet shakes his head with the leg still in his mouth
        and manages to rip it off. The spider stares wildly at Piet with it's
        four eyes then scurries off before Piet can do any more damage. 
        'Wow, I can't believe I defeated a spider monster.' Piet thinks. Then
        he remembers that it was time to get out of this tunnel and he begins to
        sprint to the exit.
        """)
        self.dig_text = textwrap.dedent(""" Piet digs a hole in the ground
        and sticks his nose in it.""")
        
class EnchantedForestPartTwo(Scene):
    
    def __init__(self):
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
        self.sniff_text = textwrap.dedent(
        """ Piet sniffs around and finds a medpack hidden in the shrubs.""")
        self.dig_text = textwrap.dedent(""" Piet digs a hole in the ground
        and sticks his nose in it.""")
        
        
    
class River(Scene):
    
    def __init__(self):
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
        self.drink_water = textwrap.dedent(
        """ Piet takes a couple of sips of the fresh river water.""")
        self.dig_text = textwrap.dedent(""" Piet digs a hole in the ground
        and sticks his nose in it.""")
        
    
class DogPark(Scene):
    
    def __init__(self):
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
        self.dig_text = textwrap.dedent(""" Piet digs a hole in the ground
        and sticks his nose in it.""")
        
    
class Death(Scene):
    
    def __init__(self):
        self.death_text = textwrap.dedent(
        """ Unfortunately, the decisions Piet has made have led him to his
        death. Game over!
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
              'death': Death()
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
